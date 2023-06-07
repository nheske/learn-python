##prompt: write python program to generate a cylinder 6 in long and 1 inch in radius using pyvista library and saved to stl file and also visually renders it
# can render STL file in https://3dviewer.net/
#pip install pyvista
import pyvista as pv

# Dimensions in inches
radius = 1.0
height = 6.0
file_path = "chatgpt/stl/cylinder.stl"

# Generate cylinder
cylinder = pv.Cylinder(center=(0, 0, 0), direction=(0, 0, 1), radius=radius, height=height)

# Save cylinder as STL file
cylinder.save(file_path)

# Visualize the cylinder
plotter = pv.Plotter()
plotter.add_mesh(cylinder, color='white')
plotter.show()
