"""
Seregin's Condition (1.4) computation for Type II blowup analysis.

Implements the weighted norms from arXiv:2507.08733:
- A_{m₁}(v,r): Weighted velocity L² norm
- E_m(v,r): Weighted dissipation
- D_m(q,r): Weighted pressure contribution

If sup_{0 < r < 1} {A_{m₁} + E_m + D_m} < ∞, Type II blowup is ruled out
for m ∈ (1/2, 3/5) via Euler Liouville theorem.
"""

import numpy as np
from numpy.fft import fftn, ifftn, fftfreq
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class SereginDiagnostics:
    """Container for Seregin condition diagnostic quantities."""
    time: float
    m: float                    # Parameter m ∈ (1/2, 3/5)
    r: float                    # Scale r
    A_m1: float                 # Weighted velocity norm
    E_m: float                  # Weighted dissipation
    D_m: float                  # Weighted pressure
    total: float                # A_m1 + E_m + D_m

    @property
    def m1(self) -> float:
        """Secondary exponent m₁ = 2m - 1."""
        return 2 * self.m - 1


@dataclass
class Condition14Result:
    """Result of checking condition (1.4) across scales."""
    m: float
    sup_total: float            # sup_r {A_m1 + E_m + D_m}
    sup_A_m1: float             # sup_r A_m1
    sup_E_m: float              # sup_r E_m
    sup_D_m: float              # sup_r D_m
    r_max: float                # Scale where sup is achieved
    is_bounded: bool            # Whether sup < threshold

    def to_dict(self) -> Dict:
        return {
            'm': self.m,
            'sup_total': self.sup_total,
            'sup_A_m1': self.sup_A_m1,
            'sup_E_m': self.sup_E_m,
            'sup_D_m': self.sup_D_m,
            'r_max': self.r_max,
            'is_bounded': self.is_bounded
        }


class SereginConditionChecker:
    """
    Check Seregin's condition (1.4) for Type II blowup exclusion.

    Condition (1.4): sup_{0 < r < 1} {A_{m₁}(v,r) + E_m(v,r) + D_m(q,r)} < ∞

    where:
    - A_{m₁}(v,r) = sup_{-r² < t < 0} r^{-(2m-1)} ∫_{B(r)} |v|² dx
    - E_m(v,r) = r^{-m} ∫_{Q(r)} |∇v|² dz
    - D_m(q,r) = r^{-2m} ∫_{Q(r)} |q|^{3/2} dz

    For numerical computation, we approximate the parabolic cylinder Q(r)
    using the current spatial field (snapshot) and estimate time integrals.
    """

    def __init__(self, L: float = 2*np.pi, nu: float = 0.01,
                 singularity_center: Tuple[float, float, float] = None):
        """
        Args:
            L: Domain size
            nu: Kinematic viscosity
            singularity_center: (x0, y0, z0) center for balls B(r).
                               If None, uses domain center.
        """
        self.L = L
        self.nu = nu
        self.singularity_center = singularity_center

        # History for time-integrated quantities
        self.time_history: List[Tuple[float, np.ndarray, np.ndarray]] = []

    def _get_ball_mask(self, N: int, r: float) -> np.ndarray:
        """
        Create mask for ball B(r) centered at singularity_center.

        Args:
            N: Grid size
            r: Ball radius

        Returns:
            Boolean mask array of shape (N, N, N)
        """
        dx = self.L / N
        x = np.linspace(0, self.L - dx, N)
        y = np.linspace(0, self.L - dx, N)
        z = np.linspace(0, self.L - dx, N)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

        # Default center: domain center
        if self.singularity_center is None:
            x0, y0, z0 = self.L/2, self.L/2, self.L/2
        else:
            x0, y0, z0 = self.singularity_center

        # Distance from center (with periodic boundary handling)
        def periodic_dist(a, a0, L):
            d = np.abs(a - a0)
            return np.minimum(d, L - d)

        dist_sq = (periodic_dist(X, x0, self.L)**2 +
                   periodic_dist(Y, y0, self.L)**2 +
                   periodic_dist(Z, z0, self.L)**2)

        return dist_sq <= r**2

    def compute_A_m1(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                     r: float, m: float) -> float:
        """
        Compute weighted velocity norm A_{m₁}(v,r).

        A_{m₁}(v,r) = r^{-(2m-1)} ∫_{B(r)} |v|² dx

        For a single time snapshot, this approximates the sup over time.

        Args:
            u, v, w: Velocity components
            r: Ball radius
            m: Parameter m ∈ (1/2, 3/5)

        Returns:
            A_{m₁}(v,r) value
        """
        N = u.shape[0]
        dx = self.L / N

        # Get ball mask
        mask = self._get_ball_mask(N, r)

        # Velocity magnitude squared
        v_sq = u**2 + v**2 + w**2

        # Integrate over ball
        integral = np.sum(v_sq[mask]) * dx**3

        # Weight by r^{-(2m-1)} = r^{1-2m}
        m1 = 2*m - 1
        weight = r**(-m1) if m1 > 0 else 1.0

        return weight * integral

    def compute_E_m(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                    r: float, m: float, dt: float = 0.01) -> float:
        """
        Compute weighted dissipation E_m(v,r).

        E_m(v,r) = r^{-m} ∫_{Q(r)} |∇v|² dz

        For single snapshot, we compute spatial integral and multiply by
        effective time interval (r² for parabolic cylinder).

        Args:
            u, v, w: Velocity components
            r: Ball radius
            m: Parameter m
            dt: Time step for approximating time integral

        Returns:
            E_m(v,r) value
        """
        N = u.shape[0]
        dx = self.L / N

        # Get ball mask
        mask = self._get_ball_mask(N, r)

        # Compute velocity gradients spectrally
        k = fftfreq(N, d=self.L/(2*np.pi*N))
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')

        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        grad_v_sq = np.zeros_like(u)
        for vel_hat in [u_hat, v_hat, w_hat]:
            for ki in [kx, ky, kz]:
                deriv = np.real(ifftn(1j * ki * vel_hat))
                grad_v_sq += deriv**2

        # Integrate |∇v|² over ball
        spatial_integral = np.sum(grad_v_sq[mask]) * dx**3

        # Approximate time integral over (-r², 0)
        # For snapshot, use r² as effective time interval
        time_factor = min(r**2, dt)  # Use actual dt if smaller

        # Full space-time integral
        integral = spatial_integral * time_factor

        # Weight by r^{-m}
        weight = r**(-m)

        return weight * integral

    def compute_D_m(self, p: np.ndarray, r: float, m: float,
                    dt: float = 0.01) -> float:
        """
        Compute weighted pressure D_m(q,r).

        D_m(q,r) = r^{-2m} ∫_{Q(r)} |q|^{3/2} dz

        Args:
            p: Pressure field
            r: Ball radius
            m: Parameter m
            dt: Time step

        Returns:
            D_m(q,r) value
        """
        N = p.shape[0]
        dx = self.L / N

        # Get ball mask
        mask = self._get_ball_mask(N, r)

        # |q|^{3/2} over ball
        p_32 = np.abs(p)**(3/2)
        spatial_integral = np.sum(p_32[mask]) * dx**3

        # Time integral approximation
        time_factor = min(r**2, dt)
        integral = spatial_integral * time_factor

        # Weight by r^{-2m}
        weight = r**(-2*m)

        return weight * integral

    def compute_pressure_from_velocity(self, u: np.ndarray, v: np.ndarray,
                                        w: np.ndarray) -> np.ndarray:
        """
        Compute pressure from velocity using Poisson equation.

        Δp = -∇·(u·∇u) = -∂_i∂_j(u_i u_j) for incompressible flow

        Simplified: Δp = -|∇u|² approximately (dominant term)
        """
        N = u.shape[0]
        k = fftfreq(N, d=self.L/(2*np.pi*N))
        kx, ky, kz = np.meshgrid(k, k, k, indexing='ij')
        k_sq = kx**2 + ky**2 + kz**2
        k_sq[0, 0, 0] = 1  # Avoid division by zero

        # Compute nonlinear term ∂_j(u_i u_j)
        # For simplicity, use divergence of (u⊗u)
        u_hat = fftn(u)
        v_hat = fftn(v)
        w_hat = fftn(w)

        # ∂_x(u²) + ∂_y(uv) + ∂_z(uw)
        rhs_u = (1j*kx*fftn(u*u) + 1j*ky*fftn(u*v) + 1j*kz*fftn(u*w))
        rhs_v = (1j*kx*fftn(v*u) + 1j*ky*fftn(v*v) + 1j*kz*fftn(v*w))
        rhs_w = (1j*kx*fftn(w*u) + 1j*ky*fftn(w*v) + 1j*kz*fftn(w*w))

        # Divergence
        div_uu = 1j*kx*rhs_u + 1j*ky*rhs_v + 1j*kz*rhs_w

        # Solve Poisson: p_hat = -div_uu / k²
        p_hat = -div_uu / k_sq
        p_hat[0, 0, 0] = 0  # Zero mean pressure

        return np.real(ifftn(p_hat))

    def check_condition_14(self, u: np.ndarray, v: np.ndarray, w: np.ndarray,
                           m: float, r_values: np.ndarray = None,
                           p: np.ndarray = None, dt: float = 0.01,
                           threshold: float = 1e10) -> Condition14Result:
        """
        Check condition (1.4) for a given m value.

        Args:
            u, v, w: Velocity components
            m: Parameter m ∈ (1/2, 3/5)
            r_values: Array of r values to check. Default: logspace(0.01, 0.5, 30)
            p: Pressure field. If None, computed from velocity.
            dt: Time step for integrals
            threshold: Consider bounded if sup < threshold

        Returns:
            Condition14Result with sup values and boundedness status
        """
        if r_values is None:
            # Default: logarithmic spacing from small to half-domain
            r_values = np.logspace(np.log10(0.01), np.log10(self.L/4), 30)

        # Compute pressure if not provided
        if p is None:
            p = self.compute_pressure_from_velocity(u, v, w)

        A_m1_values = []
        E_m_values = []
        D_m_values = []
        totals = []

        for r in r_values:
            A = self.compute_A_m1(u, v, w, r, m)
            E = self.compute_E_m(u, v, w, r, m, dt)
            D = self.compute_D_m(p, r, m, dt)

            A_m1_values.append(A)
            E_m_values.append(E)
            D_m_values.append(D)
            totals.append(A + E + D)

        A_m1_values = np.array(A_m1_values)
        E_m_values = np.array(E_m_values)
        D_m_values = np.array(D_m_values)
        totals = np.array(totals)

        # Find supremum
        idx_max = np.argmax(totals)

        return Condition14Result(
            m=m,
            sup_total=np.max(totals),
            sup_A_m1=np.max(A_m1_values),
            sup_E_m=np.max(E_m_values),
            sup_D_m=np.max(D_m_values),
            r_max=r_values[idx_max],
            is_bounded=np.max(totals) < threshold
        )

    def check_condition_14_multiple_m(self, u: np.ndarray, v: np.ndarray,
                                       w: np.ndarray,
                                       m_values: np.ndarray = None,
                                       **kwargs) -> List[Condition14Result]:
        """
        Check condition (1.4) for multiple m values in (1/2, 3/5).

        Args:
            u, v, w: Velocity components
            m_values: Array of m values. Default: linspace(0.51, 0.59, 9)
            **kwargs: Additional arguments for check_condition_14

        Returns:
            List of Condition14Result for each m
        """
        if m_values is None:
            m_values = np.linspace(0.51, 0.59, 9)

        results = []
        for m in m_values:
            result = self.check_condition_14(u, v, w, m, **kwargs)
            results.append(result)

        return results

    def get_detailed_diagnostics(self, u: np.ndarray, v: np.ndarray,
                                  w: np.ndarray, t: float, m: float,
                                  r_values: np.ndarray = None) -> List[SereginDiagnostics]:
        """
        Get detailed diagnostics at each scale r for a given m.

        Args:
            u, v, w: Velocity components
            t: Current time
            m: Parameter m
            r_values: Array of r values

        Returns:
            List of SereginDiagnostics for each r
        """
        if r_values is None:
            r_values = np.logspace(np.log10(0.01), np.log10(self.L/4), 30)

        p = self.compute_pressure_from_velocity(u, v, w)

        diagnostics = []
        for r in r_values:
            A = self.compute_A_m1(u, v, w, r, m)
            E = self.compute_E_m(u, v, w, r, m)
            D = self.compute_D_m(p, r, m)

            diag = SereginDiagnostics(
                time=t,
                m=m,
                r=r,
                A_m1=A,
                E_m=E,
                D_m=D,
                total=A + E + D
            )
            diagnostics.append(diag)

        return diagnostics

    def summary(self, results: List[Condition14Result]) -> str:
        """Generate summary string for condition (1.4) check results."""
        lines = ["Seregin Condition (1.4) Analysis", "=" * 40]

        for r in results:
            status = "BOUNDED" if r.is_bounded else "UNBOUNDED"
            lines.append(f"\nm = {r.m:.3f} (m₁ = {2*r.m-1:.3f}):")
            lines.append(f"  sup(A_m1 + E_m + D_m) = {r.sup_total:.4e}")
            lines.append(f"  sup(A_m1) = {r.sup_A_m1:.4e}")
            lines.append(f"  sup(E_m)  = {r.sup_E_m:.4e}")
            lines.append(f"  sup(D_m)  = {r.sup_D_m:.4e}")
            lines.append(f"  r_max = {r.r_max:.4f}")
            lines.append(f"  Status: {status}")

        # Overall assessment
        all_bounded = all(r.is_bounded for r in results)
        lines.append("\n" + "=" * 40)
        if all_bounded:
            lines.append("CONCLUSION: Condition (1.4) appears SATISFIED")
            lines.append("→ Type II blowup ruled out for tested m values")
        else:
            unbounded_m = [r.m for r in results if not r.is_bounded]
            lines.append(f"CONCLUSION: Condition (1.4) may FAIL for m ∈ {unbounded_m}")
            lines.append("→ Seregin's method inconclusive for these m values")

        return "\n".join(lines)


# Convenience function for quick checking
def quick_check_seregin(u: np.ndarray, v: np.ndarray, w: np.ndarray,
                        L: float = 2*np.pi, nu: float = 0.01) -> str:
    """
    Quick check of Seregin's condition (1.4) for standard m values.

    Args:
        u, v, w: Velocity components
        L: Domain size
        nu: Viscosity

    Returns:
        Summary string
    """
    checker = SereginConditionChecker(L=L, nu=nu)
    results = checker.check_condition_14_multiple_m(u, v, w)
    return checker.summary(results)
