import unreal
import os


def duplicate_assets():
    # instances of unreal classes
    editor_util = unreal.EditorUtilityLibrary()
    editor_asset_lib = unreal.EditorAssetLibrary()

    # get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)

    # hard coded value
    num_copies = 5

    total_num_copies = num_copies * num_copies
    progress_text_label = "Duplicating Assets..."
    running = True

    with unreal.ScopedSlowTask(total_num_copies, progress_text_label) as slow_tasks:

        # display dialog
        slow_tasks.make_dialog(True)

        for asset in selected_assets:
            # get the asset name and the path to be duplicated
            asset_name = asset.get_fname()
            asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)
            source_path = os.path.dirname(asset_path)

            for i in range(num_copies):

                # if cancel btn is pressed
                if slow_tasks.should_cancel():
                    running = False
                    break

                new_name = "{}_{}".format(asset_name, i)
                dest_path = os.path.join(source_path, new_name)
                duplicate = editor_asset_lib.duplicate_asset(asset_path, dest_path)
                slow_tasks.enter_progress_frame(1)

                if duplicate is None:
                    unreal.log_warning("Duplicate from {} at {} already exists".format(source_path, dest_path))

            if not running:
                break

        unreal.log("{} assets duplicated".format(num_assets))



