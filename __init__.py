# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "LizAddons",
    "author" : "Englisabeth",
    "description" : "Shortcuts I use in my workflow alot",
    "blender" : (2, 91, 0),
    "version" : (0, 0, 5),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . utils.liztools import *
from . operators.liz_ops import LizNormalSmooth
from . operators.liz_ops import LizCenterCursor
from . operators.liz_ops import LizHPLPRenamer
from . operators.liz_ops import LizOrbitSelectionToggle
from . panels.liz_panel import VIEW3D_PT_LizAddon

classes = (LizNormalSmooth, LizCenterCursor, VIEW3D_PT_LizAddon, LizHPLPRenamer, LizOrbitSelectionToggle)

register, unregister =bpy.utils.register_classes_factory(classes)