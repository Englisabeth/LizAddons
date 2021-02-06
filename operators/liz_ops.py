import bpy
from ..utils import liztools

class LizOrbitSelectionToggle(bpy.types.Operator):
    bl_idname = "view3d.orbit_select"
    bl_label = "Orbit around selection toggle"
    bl_description = "Orbit around selection toggle"

    def execute(self, context):
        OrbitSelectionToggle = not context.preferences.inputs.use_rotate_around_active
        context.preferences.inputs.use_rotate_around_active = OrbitSelectionToggle
        return {'FINISHED'}

class LizNormalSmooth(bpy.types.Operator):
    bl_idname = "mesh.liznormal"
    bl_label = "Smooth & Weight Normals"
    bl_description = "Sets normal smoothing to 45 and adds a weighted normal modifier"

    def execute(self, context):
        bpy.ops.object.shade_smooth()
        bpy.context.object.data.use_auto_smooth = True
        bpy.context.object.data.auto_smooth_angle = 0.785398
        bpy.ops.object.modifier_add(type='WEIGHTED_NORMAL')
        bpy.context.object.modifiers["WeightedNormal"].keep_sharp = True
        return {'FINISHED'}

class LizExportHP(bpy.types.Operator):
    bl_idname = "export.lizhp"
    bl_label = "Move and export mesh back and forth"
    bl_description = "Snaps to 3D cursor and Exports to obj, then resets position"

    def execute(self, context):
        LocationCopy = bpy.context.active_object.location.copy()
        RotationCopy = bpy.context.active_object.location.copy()
        bpy.ops.view3d.snap_cursor_to_center()
        bpy.ops.view3d.snap_selected_to_cursor()
        bpy.ops.transform.translate(value=(print('LocationCopy[1]'), print('LocationCopy[2]'), print('LocationCopy[3]'), orient_type='GLOBAL', orient_matrix=((0, 0, 0), (0, 0, 0), (0, 0, 0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=(print('RotationCopy[1]'), print('RotationCopy[2]'), print('RotationCopy[3]'), orient_type='GLOBAL', orient_matrix=((0, 0, 0), (0, 0, 0), (0, 0, 0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', use_proportional_connected=False, use_proportional_projected=False)
        return {'FINISHED'}

class LizCenterCursor(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Center 3d cursor"
    bl_description = "Center 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()
        return {'FINISHED'}

class LizHPLPRenamer(bpy.types.Operator):
    bl_idname = "view3d.lizhplp"
    bl_label = "Toggle between high and low poly names"
    bl_description = "Toggle between high and low poly names"

    def execute(self, context):
        for item in context.selected_objects:
            if item.name.endswith("_high"):
                item.name = item.name[:-len("_high")] + "_low"
            elif item.name.endswith("_low"):
                item.name = item.name[:-len("_low")] + "_high"
            else:
                item.name += "_high"
        return {'FINISHED'}