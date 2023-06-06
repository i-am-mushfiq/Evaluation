import bpy
import os

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

def create_pyramid(height):
    # Create mesh and object
    mesh = bpy.data.meshes.new('PyramidMesh')
    obj = bpy.data.objects.new('Pyramid', mesh)

    scene = bpy.context.scene
    scene.collection.objects.link(obj)

    vertices = [
        (1, 1, 0),
        (-1, 1, 0),
        (-1, -1, 0),
        (1, -1, 0),
        (0, 0, height)
    ]

    faces = [
        (0, 1, 4),
        (1, 2, 4),
        (2, 3, 4),
        (3, 0, 4)
    ]

    mesh.from_pydata(vertices, [], faces)
    mesh.update()
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

    return obj

pyramid_height = 2.5
pyramid = create_pyramid(pyramid_height)

# Get the current script's directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Go up two levels to the desired export directory
export_dir = os.path.abspath(os.path.join(script_directory, '..','..', 'models'))

# Create the export filename
export_filename = 'pyramid.gltf'
export_path = os.path.join(export_dir, export_filename)

os.makedirs(export_dir, exist_ok=True)

# Export the pyramid in GLTF format (GLTF_SEPARATE)
bpy.ops.export_scene.gltf(
    filepath=export_path,
    export_format='GLTF_SEPARATE',
    use_selection=True
)
