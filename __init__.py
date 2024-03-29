# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "LizAddons",
    "author" : "Englisabeth on GitHub",
    "description" : "Shortcuts I use in my workflow alot",
    "blender" : (2, 91, 0),
    "version" : (0, 5, 0),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
from . utils.liztools import *
from . operators.liz_ops import LizNormalSmooth
from . operators.liz_ops import LizCenterCursor
from . operators.liz_ops import LizHPLPRenamer
from . operators.liz_ops import LizOriginTo3DCursor
from . operators.liz_ops import LizOrbitSelectionToggle
from . operators.liz_ops import LizNumpadEmuSelectionToggle
from . panels.liz_panel import VIEW3D_PT_LizAddon

classes = (LizNormalSmooth, LizCenterCursor, VIEW3D_PT_LizAddon, LizHPLPRenamer, LizOrbitSelectionToggle, LizNumpadEmuSelectionToggle, LizOriginTo3DCursor)

register, unregister =bpy.utils.register_classes_factory(classes)