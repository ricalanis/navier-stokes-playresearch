"""Spectral Navier-Stokes solver module."""

from .spectral_ns import SpectralNSSolver
from .initial_conditions import taylor_green, kida_vortex, perturbed_burgers
from .rescaling import TypeIIRescaler
