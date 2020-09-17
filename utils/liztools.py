import bpy

def active_get(item=True):
    if item:
        return bpy.context.active_object
    else:
        return bpy.context.active_object.name

# Return item or index for selected mesh elements or names for objects
# Add selection order by using print([a.index for a in bm.select_history])
def get_selected(mode='', item=True, ordered=False, all=False):
    selection = []
    if not mode:
        mode = get_mode()

    if mode == 'OBJECT':
        if item:
            return [obj for obj in bpy.context.selected_objects]

        else:
            return [obj.name for obj in bpy.context.selected_objects]

    elif mode in ['VERT', 'EDGE', 'FACE']:
        bm = get_bmesh()

        if ordered:
            if mode == 'VERT':
                selection = [vert for vert in bm.select_history if isinstance(vert, bmesh.types.BMVert)]
            elif mode == 'EDGE':
                selection = [edge for edge in bm.select_history if isinstance(edge, bmesh.types.BMEdge)]
            elif mode == 'FACE':
                selection = [face for face in bm.select_history if isinstance(face, bmesh.types.BMFace)]

        if all:
            if mode == 'VERT':
                selection = [vert for vert in bm.verts]
            elif mode == 'EDGE':
                selection = [edge for edge in bm.edges]
            elif mode == 'FACE':
                selection = [face for face in bm.faces]

        else:
            if mode == 'VERT':
                selection = [vert for vert in bm.verts if vert.select]
            elif mode == 'EDGE':
                selection = [edge for edge in bm.edges if edge.select]
            elif mode == 'FACE':
                selection = [face for face in bm.faces if face.select]

        if item:
            return selection
        else:
            return [element.index for element in selection]

    elif mode == 'EDIT_CURVE':
        curves = bpy.context.active_object.data.splines
        points = []

        if all:
            for curve in curves:
                if curve.type == 'BEZIER':
                    points.append([point for point in curve.bezier_points])

                else:
                    points.append([point for point in curve.points])

        else:
            for curve in curves:
                if curve.type == 'BEZIER':
                    points.append([point for point in curve.bezier_points
                                   if point.select_control_point])

                else:
                    points.append([point for point in curve.points
                                   if point.select])

        points = [item for sublist in points for item in sublist]
        return points

    else:
        return []

def get_mode():
    mode = bpy.context.mode
    if mode == 'EDIT_MESH':
        selection_mode = (tuple(bpy.context.scene.tool_settings.mesh_select_mode))
        if selection_mode[0]:
            return 'VERT'
        elif selection_mode[1]:
            return 'EDGE'
        elif selection_mode[2]:
            return 'FACE'
    return mode

    def go_high():
    