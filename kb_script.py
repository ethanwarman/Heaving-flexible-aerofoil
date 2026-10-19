import numpy as np
import math

rho_s = 100      # solid density
rho_f = 1        # fluid density
L = 1            # chord length
# h = 0.0814       # average width of NACA0012 airfoil
h = 0.0381     # average width of falcon

rho_star = rho_s / rho_f  # density ratio

U = 1            # flow velocity
b = 1            # thickness of airfoil
I = (b * h**3) / 12  # moment of inertia

# Material parameters
K_B = 40

# Young's modulus
E = (K_B * rho_f * U**2 * L**3) / I

nu = 0.3         # Poisson's ratio

# Shear modulus
M = E / (2 * (1 + nu))

# Bulk modulus
K = E / (3 * (1 - 2 * nu))

D_1 = 2 / K

C_10 = M / 2

print(f"Density ratio (rho_star): {rho_star}")
print(f"Young's modulus (E): {E}")
print(f"Shear modulus (M): {M}")
print(f"Bulk modulus (K): {K}")
print(f"First invariant coefficient (D_1): {D_1}")
print(f"First invariant coefficient (C_10): {C_10}")
