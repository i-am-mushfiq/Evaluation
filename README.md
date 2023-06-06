Q1.1

I'll switch to the "Scripting" workspace. Now, I'll create a new Python script. In an empty script file, I will write the simple example of creating a Sphere:

import bpy

bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

mesh = bpy.data.meshes.new("SphereMesh")
obj = bpy.data.objects.new("Sphere", mesh)

scene = bpy.context.scene
scene.collection.objects.link(obj)

bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=(0, 0, 0))

Q1.2

In Blender's Python API, the bpy module is a fundamental part that provides access to Blender's functionality and allows me to interact with the 3D scene. It serves as a bridge between Python and Blender, enabling me to automate tasks and manipulate various aspects of the scene.

To manipulate object transformations in a 3D scene using the bpy module, I can use the bpy.context and bpy.data attributes along with the object's properties.

Q3.1

    Renderer: An instance of THREE.WebGLRenderer to create and display the output on the screen.
    Scene: An instance of THREE.Scene to hold all the objects, lights, and cameras in the 3D scene.
    Camera: An instance of THREE.PerspectiveCamera.
    Geometry: A geometry object, either a pre-defined geometry like THREE.BoxGeometry or a custom geometry created with THREE.Geometry or THREE.BufferGeometry.
    Material: A material object, such as THREE.MeshBasicMaterial or THREE.MeshPhongMaterial, to define the appearance of the objects in the scene.
    Mesh: A mesh object created with THREE.Mesh, combining a geometry and a material to render objects in the scene.

Q3.2

To import and use a 3D model created in Blender within a Three.js application, the following steps can be followed:

    Export the model from Blender in .glTF or .glb format.
    Use the GLTFLoader in Three.js to import the model.
    Add the loaded model to the scene using scene.add().
    Set up lighting, materials, position, and rotation as required.
