import bpy

class Dynaremesh_PT_Panel(bpy.types.Panel):
    bl_idname = "Dynaremesh_PT_Panel"
    bl_label = "DynaRemesh"
    bl_category = "Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout

        row = layout.row()
        row.prop(context.object, "dynaremesh_res", expand=True)

        row = layout.row()
        row.prop(context.object, "dynaremesh_smooth", expand=True)

        row = layout.row()
        row.prop(context.object, "dynaremesh_decimate", expand=True)

        row = layout.row()
        row.operator('view3d.dynaremesh_operator', text='DynaRemesh')
