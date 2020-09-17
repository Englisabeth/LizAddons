import bpy
from ..utils import liztools

class LizCenterCursor(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_description = "Center 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}

class LizHPLPRenamer(bpy.types.Operator):
    bl_idname = "mesh.hplprenamer_liz"
    bl_label = "Simple operator"
    bl_description = "HP LP renamer"

    def execute(self, context):
        selection = []
        selection = liztools.get_selected()
        lp_suffix = '_low'
        hp_suffix = '_high'

        lp = [obj for obj in selection if obj.name.endswith(lp_suffix)]
        if lp = go_high()
    
    

            polycount_list = [len(obj.data.polygons) for obj in selection]
            lowest_index = polycount_list.index(min(polycount_list))
            lp = selection[lowest_index]
            lp.name = lp.name + lp_suffix

        elif lp[0].name.endswith(lp_suffix):
            lp = lp[0]

        for obj in selection:
            if obj is not lp:
                obj.name = lp.name[:-len(lp_suffix)] + hp_suffix

        return{'FINISHED'}

        # selection = []
        # selection = liztools.active_get
        # lp_s = '_LowPoly'
        # hp_s = '_high'


        # for obj in selection:
        #     if obj is lp:
        #         bpy.context.object.name = hp_rename
    
        # for obj in selection:
        #     if obj is hp:
        #         bpy.context.object.name = lp_rename

        return {'FINISHED'}

# Sets active object based on name
def active_set(obj, item=True):
    if item:
        print(obj)
        bpy.context.view_layer.objects.active = obj
    else:
        bpy.context.view_layer.objects.active = bpy.data.objects[obj]