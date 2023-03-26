import bpy 
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import StringProperty,PointerProperty
from random import randint


bl_info = {
    "name": "unselect obj with same uv map name",
    "description": "unselect obj with same uv map name",
    "author": "Forcks",
    "version": (1, 0),
    "blender": (3,4,1),
    "location": "View3D > UI > set theme",
    "warning": "", 
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Select",
}

class UvProps(PropertyGroup):
    mainUvName  : StringProperty(
        name='main uv name',
        default=""
    )

class UnselectObjWithMainUv(Operator):
    bl_idname = "forks_space.unselect_obj_with_main_uv"
    bl_label = "Unselect Objects With Main Uv"
    mainUvName = None
    
    def structure(self,context):
        props = context.scene.unselect_obj_with_main_uv_sc
        self.mainUvName = props.mainUvName

    def unselectExecute(self):
        props = bpy.context.scene.unselect_obj_with_main_uv_sc
        for obj in bpy.context.selected_objects:
            uv_maps = [uv for uv in obj.data.uv_layers] 
            for map in uv_maps:
                if map.name == props.mainUvName:
                    obj.select_set(False)
            
    def execute(self, context):
        self.structure(context)
        self.unselectExecute()
        return {"FINISHED"}
    
class OBJECT_PT_UnselectObj(Panel):
    bl_label = "unselect obj with same uv map name"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "unselect obj with same uv map name"

    def draw(self, context):
        layout = self.layout
        props = context.scene.unselect_obj_with_main_uv_sc
        col = layout.column()
        col.prop(props, "mainUvName")
        col.operator("forks_space.unselect_obj_with_main_uv")

classes = [
    UvProps,
    UnselectObjWithMainUv,
    OBJECT_PT_UnselectObj
]

def register():
    for cl in classes:
        register_class(cl)
    bpy.types.Scene.unselect_obj_with_main_uv_sc = PointerProperty(type=UvProps)

def unregister():
    for cl in reversed(classes):
        unregister_class(cl)
    del bpy.types.Scene.unselect_obj_with_main_uv_sc

if __name__ == '__main__':
    register()

    
    