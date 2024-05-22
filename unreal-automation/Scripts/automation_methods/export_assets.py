import unreal


def export_assets(self):

    selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()
    for selectedAsset in selected_assets:
        assetName = selectedAsset.get_name()

        exportTask = unreal.AssetExportTask()
        exportTask.automated = True
        exportTask.filename = 'D:\\' + assetName + '.fbx'
        exportTask.object = selectedAsset
        exportTask.options = unreal.FbxExportOption()
        exportTask.prompt = False

        fbxExporter = unreal.StaticMeshExporterFBX()
        exportTask.exporter = fbxExporter
        fbxExporter.run_asset_export_task(exportTask)
