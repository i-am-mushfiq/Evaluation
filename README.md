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
