"""
Tabular heave amplitude for the CalculiX/PrePoMax reference point
(preCICE notes, Section 4.3.2 "Motion Assignment").

Heave law:   h(t) = h0 * sin(omega * t)
Reduced frequency:  kappa = omega * c / (2 * U_inf)  ->  omega = 2 * kappa * U_inf / c

Output: two columns (time [s], displacement [m]) with no header, ready to
paste into PrePoMax: Amplitudes -> Tabular -> Data points.
In the Displacement/Rotation BC, keep U2 = 1 m so the table value is the
actual heave displacement in metres.
"""

import numpy as np
import pandas as pd

# ---------------- inputs ----------------
c      = 1.0       # chord [m]
U_inf  = 1.0       # free-stream velocity [m/s]
kappa  = 6.0       # reduced frequency, kappa = omega*c/(2*U_inf)
h0     = 0.1667     # heave amplitude [m]  <-- CHANGE to your case's amplitude
n_cyc  = 10        # number of cycles
dt     = 0.0001   # time step [s] (must match OpenFOAM deltaT / preCICE window)
t_end  = 5.236     # end time [s] (10 cycles = 10*pi/6 = 5.23599 s)
out    = f"amp-k{kappa:g}_h-{h0:g}_deltaT-{dt:g}.xlsx"
# ----------------------------------------

omega = 2.0 * kappa * U_inf / c          # angular frequency [rad/s] -> 12
T     = 2.0 * np.pi / omega              # period [s]                -> 0.5236
print(f"omega = {omega:.4f} rad/s, f = {omega/(2*np.pi):.4f} Hz, T = {T:.6f} s")
print(f"{n_cyc} cycles = {n_cyc*T:.6f} s (t_end used: {t_end} s)")

# Integer step count avoids floating-point drift from np.arange
n_steps = int(round(t_end / dt))
time = np.arange(n_steps + 1) * dt       # 0, dt, 2dt, ..., t_end
disp = h0 * np.sin(omega * time)

df = pd.DataFrame({"time": np.round(time, 6), "amplitude": np.round(disp, 8)})
df.to_excel(out, index=False, header=False)
df.to_csv(out.replace(".xlsx", ".csv"), index=False, header=False)

print(f"rows = {len(df)}, last time = {df['time'].iloc[-1]}")
print(f"written: {out}")
