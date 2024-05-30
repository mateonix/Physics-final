import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
c = 3.00e8       # Speed of light, m/s
M_sun = 1.989e30 # Solar mass, kg
parsec = 3.086e16 # Parsec, m

# Parameters
m1 = 1.4 * M_sun  # Mass of the first neutron star in kg avg for a neutron star
m2 = 1.4 * M_sun  # Mass of the second neutron star in kg
d = 40 * 1e6 * parsec  # Around the distance to first merger discovered
chirp_mass = ((m1 * m2) ** (3/5)) / ((m1 + m2) ** (1/5)) # looked at a lot on this 
# it is basically a combination of the masses which helps determine the rate at which two
# neutron stars are moving toward each other which can help with predicting
# how the gravitational waves are changing 

# Time array (before merger)
t = np.linspace(-0.2, 0, 1000)  # Time from -0.2 to 0 seconds

# Post-Newtonian waveform calculation (Inspiral phase) this is somewhat very simplified but I tried
# The inspiral phase is the early stage of a binary merger event and the duration in which we can detect gravitational waves
def post_newtonian_waveform(t, chirp_mass, d):
    f_initial = 20  # Initial frequency in Hz
    f_merge = 400  # Approximate merger frequency in Hz
    tau = 0.1  # Time constant for the merger
    h_0 = 4 * G * chirp_mass / (c**2 * d)  # Amplitude scaling factor
    
    # Gravitational wave strain for inspiral
    f = f_initial * (1 - t / tau) ** (-3/8)
    phase = 2 * np.pi * np.cumsum(f) * np.mean(np.diff(t))
    h = h_0 * (f ** (2/3)) * np.cos(phase)
    
    # Apply tapering to simulate merger and ringdown
    merger_taper = np.exp(-(t + tau)**2 / (2 * tau**2))
    h *= merger_taper
    
    return h

# Calculate waveform
h = post_newtonian_waveform(t, chirp_mass, d)

# Plot the waveform
plt.figure(figsize=(15, 8))
plt.plot(t, h, label='Gravitational Wave Strain')
plt.xlabel('Time (s)')
plt.ylabel('h/Strain')
plt.title('Gravitational Wave from Neutron Star Merger (Inspiral Phase)')
plt.legend()
plt.grid(True)
plt.show()
