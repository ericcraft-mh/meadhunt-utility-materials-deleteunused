__all__ = ["StageMaterialsDeleteUnused"]
import omni.ext
import omni.ui as ui

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
            print("Delete Unused Materials")
        # Add context menu to omni.kit.widget.stage
        context_menu = omni.kit.context_menu.get_instance()
        if context_menu:
            menu = {
                "name": "Delete Unused Materials",
                "glyph": "menu_delete.svg",
                "show_fn": [context_menu.is_prim_selected],
                "onclick_fn": on_unused,
            }
            self._stage_context_menu_delete_unused = omni.kit.context_menu.add_menu(menu, "MENU", "omni.kit.widget.stage")

    def _unregister_stage_menu(self):
        """Called when "omni.kit.widget.stage" is unloaded"""
        self._stage_context_menu_delete_unused = None
