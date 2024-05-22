import unreal


def import_assets(self):
    """
    Import assets into project.
    """
    # list of files to import
    fileNames = [
        'D:\\abc.fbx',

    ]
    # create asset tools object
    assetTools = unreal.AssetToolsHelpers.get_asset_tools()
    # create asset import data object
    assetImportData = unreal.AutomatedAssetImportData()
    # set assetImportData attributes
    assetImportData.destination_path = '/Game/'
    assetImportData.filenames = fileNames
    assetImportData.replace_existing = True
    assetTools.import_assets_automated(assetImportData)