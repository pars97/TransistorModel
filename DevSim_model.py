import sys
import os

# Add DevSim to the Python path if necessary
# Replace '/path/to/devsim' with the actual path to the DevSim library
sys.path.append('c:/users/philippe arsenault/appdata/local/programs/python/python312/lib/site-packages')

# Import DevSim
#import mkl
import devsim

# Verify the DevSim version
print(devsim.get_version())

# Start using DevSim
devsim.set_parameter(name="debug_level", value=1)  # Example of setting a global parameter


# Define a simple 1D mesh
devsim.create_1d_mesh(mesh="simple_mesh")
devsim.add_1d_mesh_line(mesh="simple_mesh", pos=0.0, ps=1e-7)
devsim.add_1d_mesh_line(mesh="simple_mesh", pos=1e-6, ps=1e-7)
devsim.finalize_mesh(mesh="simple_mesh")

# Create a region
devsim.add_region(mesh="simple_mesh", material="Si", region="simple_region")

# Specify parameters
devsim.set_parameter(name="Permittivity", value=11.7)
devsim.set_parameter(name="ElectronCharge", value=1.60219e-19)

# Solve for electric potential
devsim.solve(type="dc", absolute_error=1e-10, relative_error=1e-5, maximum_iterations=30)

# Retrieve and print results
potential = devsim.get_node_model_values(region="simple_region", name="Potential")
print("Node potentials:", potential)
