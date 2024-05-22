import unreal


def create_multiple_bpclass():
    # instances of unreal classes
    assettool_lib = unreal.AssetToolsHelpers

    totalNumberOfBPs = 20
    textDisplay = "Creating Custom Assets"
    BPPath = "/Game/Test"
    BPName = "New_BP_%d"

    factory = unreal.BlueprintFactory()
    factory.set_editor_property("ParentClass", unreal.Pawn)
    assetTools = assettool_lib.get_asset_tools()

    with unreal.ScopedSlowTask(totalNumberOfBPs, textDisplay) as ST:
        ST.make_dialog(True)
        for i in range(totalNumberOfBPs):
            if ST.should_cancel():
                break;

            myNewFile = assetTools.create_asset_with_dialog(BPName % (i), BPPath, None, factory)

            unreal.EditorAssetLibrary.save_loaded_asset(myNewFile)

            ST.enter_progress_frame(1)
