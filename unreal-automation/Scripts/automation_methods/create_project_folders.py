import unreal
import os


def create_project_folders():
    # instances of unreal classes
    editor_util = unreal.EditorAssetLibrary()
    system_lib = unreal.SystemLibrary()

    folder_path = "/Game/"
    folder_name = "NewFolder"
    full_folder_path = folder_path + folder_name

    try:
        editor_util.make_directory(full_folder_path)
        unreal.log("Folder created successfully at {}".format(folder_path))
    except OSError as e:
        unreal.log("Error creating folder at {} : {}".format(folder_path, e))


create_project_folders()