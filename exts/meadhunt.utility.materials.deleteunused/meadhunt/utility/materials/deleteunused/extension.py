__all__ = ["StageMaterialsDeleteUnused"]

import omni.ext
import omni.kit.context_menu
import omni.usd
from pxr import UsdShade, Sdf

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.

class StageMaterialsDeleteUnused(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        app = omni.kit.app.get_app_interface()
        ext_manager = app.get_extension_manager()

        self._stage_menu = ext_manager.subscribe_to_extension_enable(
            on_enable_fn=lambda _: self._register_stage_menu(),
            on_disable_fn=lambda _: self._unregister_stage_menu(),
            ext_name="omni.kit.widget.stage",
            hook_name="meadhunt.utility.materials.deleteunused",
        )   

    def on_shutdown(self):
        self._stage_menu = None

    def _register_stage_menu(self):
        """Called when "omni.kit.widget.stage" is loaded"""
        def on_unused(self):
            """Called from the context menu"""
            usedMats = []
            allMats = []
            stage = omni.usd.get_context().get_stage()
            printZero = "Deleted Unused Materials (0): No Unused Materials Found!"
            for prim in stage.Traverse():
                # ignore references and payloads
                if not omni.usd.check_ancestral(prim):
                    matList = UsdShade.MaterialBindingAPI(prim).GetDirectBindingRel().GetTargets()
                    # join usedMats and matList
                    if len(matList):
                        usedMats = list(set(usedMats + matList))
                    # if it is a Material add to allMats
                    if prim.IsA(UsdShade.Material):
                        allMats.append(prim.GetPath())
            # if there are materials
            if len(allMats):
                # use Python List Comprehension to quickly check for unused mats
                unusedMats = [mat for mat in allMats if mat not in usedMats]
                # if unusedMats is not 0 delete the materials and print what is deleted
                if len(unusedMats):
                    # collect names of materials using List Comprehension
                    unusedNames = [Sdf.Path(x).name for x in unusedMats]
                    # delete unused mats
                    omni.kit.commands.execute('DeletePrims',paths=unusedMats)
                    # print results
                    print(f"Deleted Unused Materials ({len(unusedNames)}): {unusedNames}")
                # else printZero statement
                else:
                    print(printZero)
            # else printZero statement
            else:
                print(printZero)
        # Add context menu to omni.kit.widget.stage
        context_menu = omni.kit.context_menu.get_instance()
        if context_menu:
            appear_after = "Open in MDL Material Graph"
            menu = {
                "name": "Delete Unused Materials",
                "glyph": "menu_delete.svg",
                "onclick_fn": on_unused,
                "appear_after": appear_after,
            }
            self._stage_context_menu_delete_unused = omni.kit.context_menu.add_menu(menu, "MENU", "omni.kit.widget.stage")
    def _unregister_stage_menu(self):
        """Called when "omni.kit.widget.stage" is unloaded"""
        self._stage_context_menu_delete_unused = None
