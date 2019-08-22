import bpy

class Dynaremesh_PT_Panel(bpy.types.Panel):
    bl_idname = "Dynaremesh_PT_Panel"
    bl_label = "DynaRemesh"
    bl_category = "Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout

        # REMESH RESOLUTION
        layout.label(text="Remesh Resolution:")
        row = layout.row()
        row.prop(context.scene, "dynaremesh_res", expand=True)

        # SMOOTH
        row = layout.row()
        layout.label(text="Smooth Mesh:")
        row = layout.row()
        row.prop(context.scene, "dynaremesh_smooth", expand=True)

        # DECIMATE
        row = layout.row()
        layout.label(text="Decimate After Remesh:")
        row = layout.row(align=True)
        row.prop(context.scene, "dynaremesh_decimate", expand=True)
        row.prop(context.scene, "dynaremesh_decimate_ratio", expand=True)

        # OPERATOR BUTTON
        row = layout.row()
        row.operator('view3d.dynaremesh_operator', text='DynaRemesh')
