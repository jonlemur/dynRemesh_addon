import bpy
import bmesh
import os

class Dynaremesh_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.dynaremesh_operator"
    bl_label = "DynaRemesh Operator"
    bl_description = "Join selected meshes and remesh"

    def execute(self,context):
        #print(context.object.dynaremesh_smooth)
        #print(context.object.dynaremesh_decimate)
        #print(self.res)

        scene = bpy.context.scene
        view_layer = bpy.context.view_layer

        #pprint(dir(scene))

        # make sure we're in object modes
        bpy.ops.object.mode_set(mode='OBJECT', toggle=False)

        selected_objects = bpy.context.selected_objects
        #bpy.context.area.type = "VIEW_3D"

        # wash selection to only have mesh-type objects
        selected_meshes = []
        for obj in selected_objects:
            if obj.type == "MESH":
                selected_meshes.append(obj)

        # make sure a mesh is selected        
        if len(selected_meshes) > 0:

            # if many meshes are selected
            if len(selected_meshes) > 1:

                bpy.ops.object.select_all(action='DESELECT')                
                
                # join meshes with each other using the boolean modefier
                for i in range(1, len(selected_meshes)):
                    view_layer.objects.active = selected_meshes[0]        
                    
                    bpy.ops.object.modifier_add(type='BOOLEAN')
                    bpy.context.object.modifiers["Boolean"].operation = 'UNION'
                    bpy.context.object.modifiers["Boolean"].object = selected_meshes[i]
                    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")
                    
                    bpy.data.objects[selected_meshes[i].name].select_set(True)
                    bpy.ops.object.delete()

            
            # select the joined mesh
            bpy.data.objects[selected_meshes[0].name].select_set(True)
            
            # if the smooth checkbox was selected
            if context.scene.dynaremesh_smooth == True:
                bpy.ops.object.modifier_add(type='SUBSURF')
                bpy.context.object.modifiers["Subdivision"].levels = 2
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subdivision")
     

            # duplicate the mesh
            # for use with the shinkwrap later
            bpy.data.objects[selected_meshes[0].name].select_set(True)
            retopo_model = (bpy.context.selected_objects)[0]
            bpy.ops.object.duplicate(linked=0,mode='TRANSLATION')
            duplicate = (bpy.context.selected_objects)[0]

            # add remesh modifier
            view_layer.objects.active = retopo_model
            bpy.ops.object.modifier_add(type='REMESH')
            bpy.context.object.modifiers["Remesh"].octree_depth = context.scene.dynaremesh_res
            bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
            bpy.context.object.modifiers["Remesh"].use_smooth_shade = True
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

            # Shrinkwrap mesh to duplicate
            bpy.ops.object.modifier_add(type='SHRINKWRAP')
            bpy.context.object.modifiers["Shrinkwrap"].target = duplicate
            bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")

            bpy.data.objects[duplicate.name].select_set(True)
            bpy.ops.object.delete()

            bpy.data.objects[retopo_model.name].select_set(True)

            if context.scene.dynaremesh_decimate == True:
                bpy.ops.object.modifier_add(type='DECIMATE')
                bpy.context.object.modifiers["Decimate"].ratio = context.scene.dynaremesh_decimate_ratio
                bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Decimate")



        return {'FINISHED'}