import bpy

class Dynaremesh_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.dynaremesh_operator"
    bl_label = "DynaRemesh Operator"
    bl_description = "Join selected meshes and remesh"

    #resolution: bpy.props.IntProperty(name="Resolution", default=8, min=1, max=10)

    #res = 3

    def execute(self,context):
        print("hello world")
        print(context.object.dynaremesh_res)
        print(context.object.dynaremesh_smooth)
        print(context.object.dynaremesh_decimate)
        #print(self.res)
        return {'FINISHED'}