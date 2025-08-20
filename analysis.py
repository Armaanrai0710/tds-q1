# 24ds2000041@ds.study.iitm.ac.in
# Marimo interactive notebook demo

import marimo as mo

# Cell 1: Define an interactive slider
# This slider will control the number of data points to simulate
slider = mo.ui.slider(start=10, stop=100, value=50, step=10)
slider
python
Copy
Edit
# Cell 2: Generate data based on slider value
# Data flow: slider.value → size of dataset
import numpy as np

n_points = slider.value  # dependency on slider
data = np.random.normal(loc=0, scale=1, size=n_points)
f"Generated {n_points} random data points."
python
Copy
Edit
# Cell 3: Dynamic Markdown output based on widget state
# Data flow: slider.value → Markdown visualization
mo.md(f"""
### Interactive Report  
Number of samples: **{slider.value}**

{"🟢" * (slider.value // 10)}
""")
python
Copy
Edit
# Cell 4: Simple statistics on generated data
# Data flow: data → mean and std dev
mean_val = data.mean()
std_val = data.std()

f"Mean: {mean_val:.3f}, Std Dev: {std_val:.3f}"
