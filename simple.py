import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 3.00e8       # Speed of light, m/s
M_sun = 1.989e30 # Solar mass, kg
parsec = 3.086e16 # Parsec, m

# Parameters
m1 = 1.4 * M_sun  # Mass of the first neutron star in kg
m2 = 1.4 * M_sun  # Mass of the second neutron star in kg
d = 40 * 1e6 * parsec  # Distance to the merger in meters

# Time array
t = np.linspace(-0.1, 0.1, 1000)  # Time from -0.1 to 0.1 seconds

# Simplified waveform calculation (Toy model)
def gravitational_waveform(t, m1, m2, d):
    f_0 = 100  # Frequency of the waveform in Hz (simplified)
    tau = 0.01  # Damping timescale (simplified)
    h_0 = 1e-21  # Amplitude scaling factor (arbitrary)
    
    # Gravitational wave strain
    h = h_0 * (np.sin(2 * np.pi * f_0 * t) * np.exp(-t**2 / (2 * tau**2)))
    return h

# Calculate waveform
h = gravitational_waveform(t, m1, m2, d)

# Plot the waveform
plt.figure(figsize=(10, 6))
plt.plot(t, h, label='Gravitational Wave Strain')
plt.xlabel('Time (s)')
plt.ylabel('Strain')
plt.title('Gravitational Wave from Neutron Star Merger')
plt.legend()
plt.grid(True)
plt.show()
