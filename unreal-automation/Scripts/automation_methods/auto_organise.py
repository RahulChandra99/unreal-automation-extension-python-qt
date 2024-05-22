import unreal
import os


def auto_organise():
    # instances fo unreal classes
    editor_util = unreal.EditorUtilityLibrary()
    system_lib = unreal.SystemLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()

    # get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    organised = 0

    # to organise within the Content folder
    parent_dir = "\\Game"

    # to organise within custom sub folder
    if num_assets > 0:
        asset_path = editor_asset_lib.get_path_name_for_loaded_asset(selected_assets[0])
        parent_dir = os.path.dirname(asset_path)

    for asset in selected_assets:
        # get the class instance and text name
        asset_name = system_lib.get_object_name(asset)
        asset_class = asset.get_class()
        class_name = system_lib.get_class_display_name(asset_class)

        # assemble new path and relocate assets
        try:
            new_path = os.path.join(parent_dir, class_name, asset_name)
            editor_asset_lib.rename_loaded_asset(asset, new_path)
            organised += 1

        except Exception as err:
            pass
