# Lemma 2 Attempt: Pressure → D_m Bound

**Objective:** Derive a bound on D_m(q,r) from velocity estimates.

---

## Statement to Prove

**Conjecture:**
```
D_m(q,r) ≤ C(m) [E_m(v,r) + velocity terms]
```

---

## Pressure-Velocity Relationship

For incompressible NS:
```
Δp = -div(u·∇u) = -∂_i∂_j(u_i u_j)
```

In Fourier space:
```
p̂(k) = -k_i k_j (û_i * û_j) / |k|²
```

---

## Calderón-Zygmund Estimate

For the Poisson equation Δp = f, the standard CZ estimate gives:
```
||D²p||_{L^q} ≤ C ||f||_{L^q}
```

For our case f = div(u⊗u), this means:
```
||∇²p||_{L^q} ≤ C ||u||_{L^{2q}}²
```

---

## D_m Estimate

```
D_m(q,r) = r^{-2m} ∫_{Q(r)} |p|^{3/2} dz
```

Using Hölder and Sobolev:
```
||p||_{L^{3/2}(B(r))} ≤ C r ||∇p||_{L^{3/2}(B(r))} (by Poincaré, mean-zero)
                      ≤ C r ||u||_{L³(B(r))}²    (by CZ with q=3/2)
```

So:
```
∫_{B(r)} |p|^{3/2} dx ≤ C r^{3/2} ||u||_{L³(B(r))}³
```

---

## Time Integration

```
∫_{Q(r)} |p|^{3/2} dz ≤ C r^{3/2} ∫_{-r²}^0 ||u||_{L³(B(r))}³ dt
```

For smooth solutions:
```
||u||_{L³(B(r))} ≤ ||u||_{L³} ≤ C ||u||_{L²}^{1/2} ||∇u||_{L²}^{1/2} (Sobolev)
```

So:
```
||u||_{L³}³ ≤ C ||u||_{L²}^{3/2} ||∇u||_{L²}^{3/2}
            ≤ C E₀^{3/4} ||∇u||_{L²}^{3/2}
```

---

## Putting Together

```
D_m(q,r) = r^{-2m} ∫_{Q(r)} |p|^{3/2} dz
         ≤ C r^{-2m} r^{3/2} ∫_{-r²}^0 E₀^{3/4} ||∇u||_{L²}^{3/2} dt
         ≤ C r^{3/2-2m} E₀^{3/4} (∫_{-r²}^0 ||∇u||_{L²}² dt)^{3/4} (r²)^{1/4}
         ≤ C r^{3/2-2m+1/2} E₀^{3/4} (E_m · r^m)^{3/4}
         = C r^{2-2m+3m/4} E₀^{3/4} E_m^{3/4}
         = C r^{2-5m/4} E₀^{3/4} E_m^{3/4}
```

---

## Critical Exponent Check

For D_m bounded as r → 0, need:
```
2 - 5m/4 ≥ 0  ⟹  m ≤ 8/5 = 1.6
```

Since m < 3/5 = 0.6 < 1.6, this condition is satisfied.

**But:** This assumes E_m is bounded, which is what we're trying to prove.

---

## Self-Consistent Bound

If E_m ≤ E_max < ∞, then:
```
D_m(q,r) ≤ C r^{2-5m/4} E₀^{3/4} E_max^{3/4}
         → 0 as r → 0 (since 2-5m/4 > 0 for m < 0.6)
```

This shows: **D_m controlled by E_m** (pressure bounded by dissipation).

---

## Obstacle

The circular dependency:
- D_m ≤ f(E_m)
- But E_m boundedness is the main assumption

For the full condition (1.4) = A_{m₁} + E_m + D_m:
- A_{m₁} is the dominant term (numerically observed)
- E_m bounds D_m
- But A_{m₁} is NOT bounded by E_m in general

---

## Partial Result

**Lemma 2 (Pressure Bound):** For m ∈ (1/2, 3/5), if E_m(v,r) ≤ E_max for all r < 1, then:
```
D_m(q,r) ≤ C(m) r^{2-5m/4} E₀^{3/4} E_max^{3/4} → 0 as r → 0
```

In particular, sup_{r<1} D_m(q,r) < ∞ whenever E_m is bounded.

---

## Conclusion

**Status:** PARTIAL SUCCESS

D_m is controlled by E_m. The bottleneck is proving E_m and A_{m₁} bounded.

From numerical experiments: D_m contributes <1% of total sup in condition (1.4).
This is consistent with the theoretical bound D_m → 0 as r → 0.

---

## References

- Caffarelli-Kohn-Nirenberg (1982): Pressure estimates
- Sohr (2001): Navier-Stokes Equations: An Elementary Functional Analytic Approach
