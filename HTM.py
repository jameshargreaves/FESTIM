
import h_transport_materials as htm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Query data from HTM
filtered_diffusivity = (
    htm.diffusivities.filter(material=['tungsten'])
    .filter(author=['byeon', 'esteban', 'fernandez', 'frauenfelder', 'heinola', 'holzner', 'ikeda', 'johnson', 'liu', 'moore', 'otsuka', 'ryabchikov', 'zakharov', 'zhao', 'zhou'])
    .filter(isotope=['h', 'd', 't'])
    .filter(year=np.arange(1957, 2024, step=1).tolist())
)

# Plot data
htm.plotting.plot(filtered_diffusivity)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xlabel("1/T (K$^{-1}$)")
plt.ylabel("Diffusivity (m$^{2}$ s$^{-1}$)")
plt.yscale("log")
plt.title("H/D/T diffusion in W")
plt.show()