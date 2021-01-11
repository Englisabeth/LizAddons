import bpy

def active_get(item=True):
    if item:
        return bpy.context.active_object
    else:
        return bpy.context.active_object.name
        
    def low_hp_changer(self, context):
        for item in context.selected_objects:
            if item.name.endswith("_high"):
                item.name = item.name[:-len("_high")] + "_low"
            elif item.name.endswith("_low"):
                item.name = item.name[:-len("_low")] + "_high"
            else:
                item.name += "_high"
        return {'FINISHED'}