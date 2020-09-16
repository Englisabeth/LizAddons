import bpy

def active_get(item=True):
    if item:
        return bpy.context.active_object
    else:
        return bpy.context.active_object.name

def s_lp_end(item=True):
    active_get