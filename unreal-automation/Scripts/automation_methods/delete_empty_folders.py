import unreal


def delete_empty_folders():
    # instances of unreal classes
    editor_asset_lib = unreal.EditorAssetLibrary()

    # set source dir and options
    source_dir = "/Game"
    include_subfolders = True
    deleted = 0

    # get all assets in source dir
    assets = editor_asset_lib.list_assets(source_dir, recursive=include_subfolders, include_folder=True)

    for asset in assets:
        if editor_asset_lib.does_directory_exist(asset):
            # check if folder has assets
            has_assets = editor_asset_lib.does_directory_have_assets(asset)

            if not has_assets:
                # delete folder
                editor_asset_lib.delete_directory(asset)
                deleted += 1
                unreal.log("Folder {} without assets was deleted".format(asset))

    unreal.log("Deleted {} folders without assets".format(deleted))



