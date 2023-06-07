#prompt: write python program to generate a cylinder 6 in long and 1 inch in radius using pyvista library and saved to stl file and also visually renders it
#thats good. make the cylinder rise above a 5x5 cube
#  can render STL file in https://3dviewer.net/
import pyvista as pv

# Dimensions in inches
radius = 1.0
height = 6.0
cube_size = 5.0
file_path = "cylinder_on_cube.stl"

# Generate cylinder and cube
cylinder = pv.Cylinder(center=(0, 0, height/2), direction=(0, 0, 1), radius=radius, height=height)
cube = pv.Cube(center=(0, 0, 0), x_length=cube_size, y_length=cube_size, z_length=cube_size)

# Combine cylinder and cube
combined_geometry = cylinder + cube

# Save combined geometry as STL file
combined_geometry.save(file_path)

# Visualize the combined geometry
plotter = pv.Plotter()
plotter.add_mesh(combined_geometry, color='white')
plotter.show()