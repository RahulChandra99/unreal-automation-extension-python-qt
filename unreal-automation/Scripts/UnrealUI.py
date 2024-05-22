import unreal
import sys
import os
import json

from PySide2 import QtUiTools, QtWidgets, QtGui, QtCore

class UnrealWidget(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    # store ref to window to prevent garbage collection
    window = None

    def __init__(self, parent=None):
        """
        Import UI and connect components
        """
        super(UnrealWidget, self).__init__(parent)

        # load the created UI widget
        self.widgetPath = 'D:\\GameDevelopment\\Pipeline-Project\\msccavepipelineandtdproject24-RahulChandra99\\unreal-automation\\GUI\\'
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath + 'unrealWidget.ui')  # path to PyQt .ui file

        # attach the widget to the instance of this class (aka self)
        self.widget.setParent(self)

        # find interactive elements of UI
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')

        # assign clicked handler to buttons
        # self.btn_close.clicked.connect(self.closewindow)

        # find interactive elements of UI

        # project setup tools UI
        self.line_parentfolder = self.widget.findChild(QtWidgets.QLineEdit, 'line_parentfolder')
        self.btn_createfolderstruc = self.widget.findChild(QtWidgets.QPushButton, 'btn_createfolderstruc')
        self.sp_genericassets = self.widget.findChild(QtWidgets.QSpinBox, 'sp_genericassets')
        self.btn_creategenericassets = self.widget.findChild(QtWidgets.QPushButton, 'btn_creategenericassets')
        self.cb_assettype = self.widget.findChild(QtWidgets.QComboBox, 'cb_assettype')
        self.sp_bpclasses = self.widget.findChild(QtWidgets.QSpinBox, 'sp_bpclasses')
        self.btn_createbpclasses = self.widget.findChild(QtWidgets.QPushButton, 'btn_createbpclasses')
        self.btn_duplicate = self.widget.findChild(QtWidgets.QPushButton, 'btn_duplicate')
        self.sp_duplicate = self.widget.findChild(QtWidgets.QSpinBox, 'sp_duplicate')

        # renamer tool UI
        self.btn_rename = self.widget.findChild(QtWidgets.QPushButton, 'btn_rename')
        self.line_search = self.widget.findChild(QtWidgets.QLineEdit, 'line_search')
        self.line_replace = self.widget.findChild(QtWidgets.QLineEdit, 'line_replace')
        self.cb_usecase = self.widget.findChild(QtWidgets.QCheckBox, 'cb_usecase')
        self.btn_autoprefix = self.widget.findChild(QtWidgets.QPushButton, 'btn_autoprefix')
        self.btn_autosuffix = self.widget.findChild(QtWidgets.QPushButton, 'btn_autosuffix')
        self.cb_conventional = self.widget.findChild(QtWidgets.QCheckBox, 'cb_conventional')
        self.line_customvalue = self.widget.findChild(QtWidgets.QLineEdit, 'line_customvalue')

        # cleanup tools UI
        self.btn_autoorganise = self.widget.findChild(QtWidgets.QPushButton, 'btn_autoorganise')
        self.btn_outlinersort = self.widget.findChild(QtWidgets.QPushButton, 'btn_outlinersort')
        self.btn_removeunused = self.widget.findChild(QtWidgets.QPushButton, 'btn_removeunused')
        self.btn_deleteempfolders = self.widget.findChild(QtWidgets.QPushButton, 'btn_deleteempfolders')
        self.rb_trash = self.widget.findChild(QtWidgets.QRadioButton, 'rb_trash')
        self.rb_delete = self.widget.findChild(QtWidgets.QRadioButton, 'rb_delete')


        # create actors UI
        self.btn_createactor = self.widget.findChild(QtWidgets.QPushButton, 'btn_createactor')
        self.sp_noactors = self.widget.findChild(QtWidgets.QSpinBox, 'sp_noactors')
        self.dsb_locX = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_locX')
        self.dsb_locY = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_locY')
        self.dsb_locZ = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_locZ')
        self.dsb_rotX = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_rotX')
        self.dsb_rotY = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_rotY')
        self.dsb_rotZ = self.widget.findChild(QtWidgets.QDoubleSpinBox, 'dsb_rotZ')
        self.sp_rotationvalue = self.widget.findChild(QtWidgets.QSpinBox, 'sp_rotationvalue')
        self.sp_offsetpos = self.widget.findChild(QtWidgets.QSpinBox, 'sp_offsetpos')
        self.btn_automatassign = self.widget.findChild(QtWidgets.QPushButton, 'btn_automatassign')
        self.btn_copytrans = self.widget.findChild(QtWidgets.QPushButton, 'btn_copytrans')
        self.cb_transform = self.widget.findChild(QtWidgets.QCheckBox, 'cb_transform')
        self.cb_location = self.widget.findChild(QtWidgets.QCheckBox, 'cb_location')
        self.cb_rotation = self.widget.findChild(QtWidgets.QCheckBox, 'cb_rotation')
        self.cb_scale = self.widget.findChild(QtWidgets.QCheckBox, 'cb_scale')

        # import export UI

        self.btn_import = self.widget.findChild(QtWidgets.QPushButton, 'btn_import')
        self.rb_autoimport = self.widget.findChild(QtWidgets.QRadioButton, 'rb_autoimport')
        self.rb_manualimport = self.widget.findChild(QtWidgets.QRadioButton, 'rb_manualimport')
        self.btn_export = self.widget.findChild(QtWidgets.QPushButton, 'btn_export')
        self.rb_autoexport = self.widget.findChild(QtWidgets.QRadioButton, 'rb_autoexport')
        self.rb_manualexport = self.widget.findChild(QtWidgets.QRadioButton, 'rb_manualexport')

        # misc tools
        self.sp_materialinstance = self.widget.findChild(QtWidgets.QSpinBox, 'sp_materialinstance')
        self.btn_multimatinstances = self.widget.findChild(QtWidgets.QPushButton, 'btn_multimatinstances')

        # console text UI
        self.warning_console = self.widget.findChild(QtWidgets.QLabel, 'warning_console')
        self.btn_dark = self.widget.findChild(QtWidgets.QPushButton, 'btn_dark')
        self.btn_light = self.widget.findChild(QtWidgets.QPushButton, 'btn_light')
        # self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')


        # assign clicked handler to buttons
        self.btn_rename.clicked.connect(self.renameassets)
        self.btn_autoprefix.clicked.connect(self.autoprefix)
        self.btn_autosuffix.clicked.connect(self.autosuffix)
        self.btn_createfolderstruc.clicked.connect(self.createprojectfolder)
        self.btn_createbpclasses.clicked.connect(self.createbpclasses)
        self.btn_duplicate.clicked.connect(self.duplicate)
        self.btn_autoorganise.clicked.connect(self.autoorganise)
        self.btn_outlinersort.clicked.connect(self.sortoutliner)
        self.btn_removeunused.clicked.connect(self.removeunused)
        self.btn_deleteempfolders.clicked.connect(self.deleteemptyfolder)
        self.btn_import.clicked.connect(self.importassets)
        self.btn_creategenericassets.clicked.connect(self.creategenericassets)
        self.btn_automatassign.clicked.connect(self.assignmatauto)
        self.btn_copytrans.clicked.connect(self.copytransform)
        self.btn_createactor.clicked.connect(self.createactor)
        self.btn_export.clicked.connect(self.exportselectedassets)
        self.btn_multimatinstances.clicked.connect(self.multimaterialinstacer)
        self.btn_dark.clicked.connect(self.darkmode)
        self.btn_light.clicked.connect(self.lightmode)
        # self.btn_close.clicked.connect(self.closewindow)

        for button in self.widget.findChildren(QtWidgets.QPushButton):
            self.setbtnappearance(button)

    """
    Custom Methods
    """

    @staticmethod
    def setbtnappearance(button):
        button.setStyleSheet('background-color: rgb(56, 56, 56);color: rgb(255, 255, 255);border-radius : 10;border-style:inset')



    def darkmode(self):
        self.widget.setStyleSheet(
            'background-color: rgb(21, 21, 21);color: rgb(255, 255, 255);QToolBox{color:rgb(0,0,0);};QPushButton{border-radius : 25px;}')
        self.warning_console.setStyleSheet(
        'color: rgb(255, 255, 0)')

    def lightmode(self):
        self.widget.setStyleSheet(
            'background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);QToolBox{color:rgb(0,0,0);QLabel{color:rgb(0,0,0)}')
        self.warning_console.setStyleSheet(
            'color: rgb(0, 0, 0)')

    # project setup tools

    def createprojectfolder(self):
        """
            setup most commonly used folders in UE
        """


        # instances of unreal classes
        editor_util = unreal.EditorAssetLibrary()

        folder_path = "/Game/"
        folder_name = self.line_parentfolder.text()

        if folder_name == "":
            folder_name = "MyProject"

        full_folder_path = folder_path + "_" + folder_name

        # make parent folder
        try:
            editor_util.make_directory(full_folder_path)
            self.warning_console.setText("Folder {} created successfully at {}".format(folder_name,folder_path))
        except OSError as e:
            self.warning_console.setText("Error creating folder at {} : {}".format(folder_path, e))

        # make subfolders
        editor_util.make_directory(full_folder_path + "/Art")
        editor_util.make_directory(full_folder_path + "/Art/Characters")
        editor_util.make_directory(full_folder_path + "/Art/Animation")
        editor_util.make_directory(full_folder_path + "/Art/Texture")
        editor_util.make_directory(full_folder_path + "/Art/Material")
        editor_util.make_directory(full_folder_path + "/Art/SkeletalMesh")
        editor_util.make_directory(full_folder_path + "/Art/StaticMesh")
        editor_util.make_directory(full_folder_path + "/Art/FX")

        editor_util.make_directory(full_folder_path + "/Blueprints")

        editor_util.make_directory(full_folder_path + "/UI")
        editor_util.make_directory(full_folder_path + "/UI/Materials")
        editor_util.make_directory(full_folder_path + "/UI/Fonts")

        editor_util.make_directory(full_folder_path + "/Cinematics")

        editor_util.make_directory(full_folder_path + "/Audio")

        editor_util.make_directory(full_folder_path + "/Maps")

    def creategenericassets(self):
        """
        Create commonly used assets instantly
        """
        editorasset_lib = unreal.EditorAssetLibrary()
        asset_tools =  unreal.AssetToolsHelpers.get_asset_tools()

        no_assets = self.sp_genericassets.value()

        if self.cb_assettype.currentIndex() == 0:
            factory = unreal.LevelSequenceFactoryNew()
            asset_class = unreal.LevelSequence
            new_asset_name = "LS_CustomLS_%d"
            destination_path = '/Game/LevelSequences'
            progress_text = "Creating new Level Sequence..."

        elif self.cb_assettype.currentIndex() == 1:
            factory = unreal.MaterialFactoryNew()
            asset_class = unreal.Material
            new_asset_name = "M_CustomM_%d"
            destination_path = '/Game/Materials'
            progress_text = "Creating new Material..."

        elif self.cb_assettype.currentIndex() == 2:
            factory = unreal.WorldFactory()
            asset_class = unreal.World
            new_asset_name = "W_CustomLS_%d"
            destination_path = '/Game/Worlds'
            progress_text = "Creating new Maps..."

        elif self.cb_assettype.currentIndex() == 3:
            factory = unreal.NiagaraScriptFactoryNew()
            asset_class = unreal.NiagaraSystem
            new_asset_name = "PS_CustomPS_%d"
            destination_path = '/Game/NiagaraSystems'
            progress_text = "Creating new Niagara Systems..."

        else:
            pass

        with unreal.ScopedSlowTask(no_assets, progress_text) as ST:
            ST.make_dialog(True)
            for x in range(no_assets):
                if ST.should_cancel():
                    break

                new_asset = asset_tools.create_asset(new_asset_name%(x), destination_path, asset_class, factory)
                editorasset_lib.save_loaded_asset(new_asset)
                self.warning_console.setText("Created new assets in {}".format(destination_path))

                ST.enter_progress_frame(1)

    def createbpclasses(self):
        """
            Create multiple bp classes with dialog
        """
        # instances of unreal classes
        assettool_lib = unreal.AssetToolsHelpers

        totalNumberOfBPs = self.sp_bpclasses.value()
        textDisplay = "Creating Blueprint Classes..."
        BPPath = "/Game"
        BPName = "New_BP_%d"

        factory = unreal.BlueprintFactory()
        assetTools = assettool_lib.get_asset_tools()

        with unreal.ScopedSlowTask(totalNumberOfBPs, textDisplay) as ST:
            ST.make_dialog(True)
            for i in range(totalNumberOfBPs):
                if ST.should_cancel():
                    break;

                myNewFile = assetTools.create_asset_with_dialog(BPName % (i), BPPath, None, factory)

                unreal.EditorAssetLibrary.save_loaded_asset(myNewFile)
                self.warning_console.setText("Blueprint classes created")
                ST.enter_progress_frame(1)

    def duplicate(self):
        """
        Make multiple copes
        """
        editor_util = unreal.EditorUtilityLibrary()
        editor_asset_lib = unreal.EditorAssetLibrary()

        # get the selected assets
        selected_assets = editor_util.get_selected_assets()
        num_assets = len(selected_assets)

        # hard coded value
        num_copies = self.sp_duplicate.value()

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
                        self.warning_console.setText("Duplicate from {} at {} already exists".format(source_path, dest_path))

                if not running:
                    break

            self.warning_console.setText("{} assets duplicated".format(num_assets))

    # renamer tools

    def renameassets(self):
        """
        rename Selected Assets
        """
        # instances of unreal classes
        system_lib = unreal.SystemLibrary()
        editor_util = unreal.EditorUtilityLibrary()
        string_lib = unreal.StringLibrary()

        search_pattern = self.line_search.text()
        replace_pattern = self.line_replace.text()
        use_case = self.cb_usecase.isChecked()

        # get the selected assets
        selected_assets = editor_util.get_selected_assets()
        num_assets = len(selected_assets)
        replaced = 0

        # unreal.log("Selected {} assets".format(num_assets))

        # loop over each asset and then rename
        for asset in selected_assets:
            asset_name = system_lib.get_object_name(asset)

            # check if asset name contains the string to be replaced
            if string_lib.contains(asset_name, search_pattern, use_case=use_case):
                search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
                replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case)
                editor_util.rename_asset(asset, replaced_name)

                replaced += 1
                self.warning_console.setText("Replaced {} with {}".format(asset_name, replaced_name))

            else:
                self.warning_console.setText("{} did not match the search pattern, was skipped.".format(asset_name))

        self.warning_console.setText("Replaced {} of {} assets".format(replaced, num_assets))

    def autoprefix(self):
        """
        Auto prefix assets based on standard/custom naming conventions or based on user inputs
        """
        # instances of unreal classes
        editor_util = unreal.EditorUtilityLibrary()
        system_lib = unreal.SystemLibrary()

        custom_prefix = self.line_customvalue.text()
        conventional = self.cb_conventional.isChecked()

        # prefix mapping
        prefix_mapping = {}
        with open(
                "D:\\GameDevelopment\\Pipeline-Project\\msccavepipelineandtdproject24-RahulChandra99\\unreal-automation\\prefix_mapping.json",
                "r") as json_file:
            prefix_mapping = json.loads(json_file.read())

        # get the selected assets
        selected_assets = editor_util.get_selected_assets()
        num_assets = len(selected_assets)
        prefixed = 0

        for asset in selected_assets:
            # get the class instance and text name
            asset_name = system_lib.get_object_name(asset)
            asset_class = asset.get_class()
            class_name = system_lib.get_class_display_name(asset_class)

            # get the prefix for the given class
            class_prefix = prefix_mapping.get(class_name, None) if conventional else custom_prefix

            if class_prefix is None:
                self.warning_console.setText("No mapping for asset {} of type {}".format(asset_name, class_name))
                continue

            if not asset_name.startswith(class_prefix):
                # rename the asset and add prefix
                new_name = class_prefix + asset_name
                editor_util.rename_asset(asset, new_name)
                prefixed += 1

            else:
                self.warning_console.setText(
                    "Asset {} of type {} is already prefixed with {}".format(asset_name, class_name, class_prefix))

            self.warning_console.setText("Prefixed {} of {} assets".format(prefixed, num_assets))

    def autosuffix(self):
        """
        Auto suffix assets based on standard/custom naming conventions or based on user inputs
        """
        # instances of unreal classes
        editor_util = unreal.EditorUtilityLibrary()
        system_lib = unreal.SystemLibrary()

        custom_suffix = self.line_customvalue.text()
        conventional = self.cb_conventional.isChecked()

        # suffix mapping
        suffix_mapping = {}
        with open(
                "D:\\GameDevelopment\\Pipeline-Project\\msccavepipelineandtdproject24-RahulChandra99\\unreal-automation\\suffix_mapping.json",
                "r") as json_file:
            suffix_mapping = json.loads(json_file.read())

        # get the selected assets
        selected_assets = editor_util.get_selected_assets()
        num_assets = len(selected_assets)
        suffixed = 0

        for asset in selected_assets:
            # get the class instance and text name
            asset_name = system_lib.get_object_name(asset)
            asset_class = asset.get_class()
            class_name = system_lib.get_class_display_name(asset_class)

            # get the prefix for the given class
            class_suffix = suffix_mapping.get(class_name, None) if conventional else custom_suffix

            if class_suffix is None:
                self.warning_console.setText("No mapping for asset {} of type {}".format(asset_name, class_name))
                continue

            if not asset_name.endswith(class_suffix):
                # rename the asset and add prefix
                new_name = asset_name + class_suffix
                editor_util.rename_asset(asset, new_name)
                suffixed += 1

            else:
                self.warning_console.setText(
                    "Asset {} of type {} is already suffixed with {}".format(asset_name, class_name, class_suffix))

            self.warning_console.setText("Suffixed {} of {} assets".format(suffixed, num_assets))

    # cleanup tools

    def autoorganise(self):
        """
        Organise objects into folders automatically
        """
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
                self.warning_console.setText("Cleaned up {} to {}".format(asset_name, new_path))

            except Exception as err:
                self.warning_console.setText("Could not move {} to new location{}".format(asset_name,new_path))

        self.warning_console.setText("Cleaned up {} of {} assets".format(organised, num_assets))

    def sortoutliner(self):
        """
            Organise the world outliner into folders
        """
        # instances of unreal classes
        editor_level_lib = unreal.EditorLevelLibrary()
        editor_filter_lib = unreal.EditorFilterLibrary()

        # get all actors and filter down to specific elements
        actors = editor_level_lib.get_all_level_actors()

        static_meshes = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)
        reflection_cap = editor_filter_lib.by_class(actors, unreal.ReflectionCapture)
        sound = editor_filter_lib.by_class(actors, unreal.AmbientSound)
        blueprints = editor_filter_lib.by_id_name(actors, "BP_")

        moved = 0

        # create a mapping between folder names and arrays
        mapping = {
            "StaticMeshActors": static_meshes,
            "ReflectionCaptures": reflection_cap,
            "Blueprints": blueprints,
            "Audio": sound
        }

        for folder_name in mapping:
            # for every list of actors, set new folder path
            for actor in mapping[folder_name]:
                actor_name = actor.get_fname()
                actor.set_folder_path(folder_name)

                self.warning_console.setText("Moved {} into {}".format(actor_name, folder_name))

                moved += 1

        self.warning_console.setText("Moved {} actors into folders".format(moved))

    def deleteemptyfolder(self):
        """
            Delete folders that don't have any assets
        """
        # instances of unreal classes
        editor_asset_lib = unreal.EditorAssetLibrary()

        # set source dir and options
        source_dir = "/Game"
        include_subfolders = True
        deleted = 0

        folder_exception = "Hello"

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
                    self.warning_console.setText("Folder {} without assets was deleted".format(asset))

        self.warning_console.setText("Deleted {} empty folders without assets".format(deleted))

    def removeunused(self):
        """
        Delete or move unused objects to Trash folder
        """
        # instances of unreal classes
        editor_util = unreal.EditorUtilityLibrary()
        editor_asset_lib = unreal.EditorAssetLibrary()

        # get the selected assets
        selected_assets = editor_util.get_selected_assets()
        num_assets = len(selected_assets)
        removed = 0

        # instantly delete assets or move to Trash folder
        if self.rb_delete.isChecked():
            instant_delete = True
        else:
            instant_delete = False

        trash_folder = os.path.join(os.sep, "Game", "Trash")
        to_be_deleted = []

        for asset in selected_assets:
            asset_name = asset.get_fname()
            asset_path = editor_asset_lib.get_path_name_for_loaded_asset(asset)

            # get a list of reference for this asset
            asset_references = editor_asset_lib.find_package_referencers_for_asset(asset_path)

            if len(asset_references) == 0:
                to_be_deleted.append(asset)

        for asset in to_be_deleted:
            asset_name = asset.get_fname()

            # instant delete
            if instant_delete:
                deleted = editor_asset_lib.delete_loaded_asset(asset)

                if not deleted:
                    self.warning_console.setText("Asset {} could not be deleted".format(asset_name))
                    continue

                removed += 1

            # move the assets to the trash folder
            else:
                new_path = os.path.join(trash_folder, str(asset_name))
                moved = editor_asset_lib.rename_loaded_asset(asset, new_path)

                if not moved:
                    self.warning_console.setText("Asset {} could not be moved to Trash".format(asset_name))
                    continue

                    removed += 1

        output_test = "removed" if instant_delete else "moved to Trash folder"

        self.warning_console.setText(
            "{} out of {} assets deleted, of {} selected, {}".format(removed, len(to_be_deleted), num_assets, output_test))

    # actors tool

    def createactor(self):
        """
            Create Actors
        """

        # instances of unreal classes
        editorutil_lib = unreal.EditorUtilityLibrary()


        num_actors = self.sp_noactors.value()
        actor_location = unreal.Vector(self.dsb_locX.value(), self.dsb_locY.value(), self.dsb_locZ.value())
        actor_rotation = unreal.Rotator(self.dsb_rotX.value(), self.dsb_rotY.value(), self.dsb_rotZ.value())

        progress_text_label = "Creating actors in the level..."

        # get the selected assets
        selected_assets = editorutil_lib.get_selected_assets()
        num_assets = len(selected_assets)
        created = 0

        with unreal.ScopedSlowTask(num_actors, progress_text_label) as ST:
            ST.make_dialog(True)
            for x in range(num_actors):
                if ST.should_cancel():
                    break;

                if selected_assets is None:
                    self.warning_console.setText("Nothing is selected")
                else:
                    for y in range(len(selected_assets)):
                        actor = unreal.EditorLevelLibrary.spawn_actor_from_object(selected_assets[y],
                                                                          actor_location,
                                                                          actor_rotation)
                        # Edit Tags
                        actor_tags = actor.get_editor_property('tags')
                        actor_tags.append('My Python Tag')
                        actor.set_editor_property('tags', actor_tags)
                        created += 1

                    ST.enter_progress_frame(1)
                    self.warning_console.setText("{} new actor(s) are spawned".format(created))

    def assignmatauto(self):
        """
            Assign material to selectors actors in the scene
        """
        # inst of unreal classes
        editor_util = unreal.EditorUtilityLibrary()
        layer_sys = unreal.LayersSubsystem()
        editor_filter_lib = unreal.EditorFilterLibrary()

        # get selected material and selected static mesh actors
        selected_assets = editor_util.get_selected_assets()
        materials = editor_filter_lib.by_class(selected_assets, unreal.Material)

        if len(materials) < 1:
            self.warning_console.setText("Select atleast one material from the content browser")
        else:
            material = materials[0]
            material_name = material.get_fname()

            actors = layer_sys.get_selected_actors()
            static_mesh_actors = editor_filter_lib.by_class(actors, unreal.StaticMeshActor)

            for actor in static_mesh_actors:
                actor_name = actor.get_fname()

                # get the static mesh component and assign the material
                actor_mesh_component = actor.static_mesh_component
                actor_mesh_component.set_material(0,material)

                self.warning_console.setText("Assigning material {} to actor {}".format(material_name, actor_name))

    def copytransform(self):
        """
            Copy transform of one actor to another
        """
        # instances of unreal classes
        editorlevel_lib = unreal.EditorLevelLibrary()

        # get world outliner reference
        world = editorlevel_lib.get_world()

        if len(editorlevel_lib.get_selected_level_actors()) < 2:
            self.warning_console.setText("Select atleast 2 actors to perform this function")
        else:
            # reference of actor's transform you want to copy and get the transform
            actor_to_copy = editorlevel_lib.get_selected_level_actors()[0]
            actor1_transform = actor_to_copy.get_actor_transform()
            actor1_scale = actor_to_copy.get_actor_scale3d()
            actor1_rotation = actor_to_copy.get_actor_rotation()
            actor1_location = actor_to_copy.get_actor_location()

            selected_actors = editorlevel_lib.get_selected_level_actors()

            # reference of actor's transform you want to copy to and assign the transforms
            for x in range(len(selected_actors)):
                actor_to_paste_to = selected_actors[x]
                if self.cb_transform.isChecked():
                    actor_to_paste_to.set_actor_transform(actor1_transform, sweep=False, teleport=True)
                if self.cb_scale.isChecked():
                    actor_to_paste_to.set_actor_scale3d(actor1_scale)
                if self.cb_rotation.isChecked():
                    actor_to_paste_to.set_actor_rotation(actor1_rotation, teleport_physics=True)
                if self.cb_location.isChecked():
                    actor_to_paste_to.set_actor_location(actor1_location, sweep=False, teleport=True)

                self.warning_console.setText(
                    "Copying transform values from {} to {}".format(actor_to_copy.get_name(), actor_to_paste_to.get_name()))
                unreal.log(
                    "Copying transform values from {} to {}".format(actor_to_copy.get_name(), actor_to_paste_to.get_name()))

    # import and export

    def importassets(self):
        """
        Import assets into project.
        """
        # create asset tools object
        assettools = unreal.AssetToolsHelpers.get_asset_tools()
        # create asset import data object
        assetimportdata = unreal.AutomatedAssetImportData()


        # list of files to import
        fileNames = [
            "D:\\"
        ]

        # set assetImportData attributes
        assetimportdata.destination_path = '/Game/Textures'
        assetimportdata.filenames = fileNames
        assetimportdata.replace_existing = True

        if self.rb_manualimport.isChecked():
            self.warning_console.setText("Importing Assets using Dialog into Content Folder")
            imported_assets = assettools.import_assets_with_dialog(assetimportdata.destination_path)
        else:
            self.warning_console.setText("Importing Assets automatically into Content Folder")
            imported_assets = assettools.import_assets_automated(assetimportdata)

        self.warning_console.setText("{} are imported".format(imported_assets))

    def exportselectedassets(self):
        """
        Export Selected Assets
        """
        # instances of unreal classes
        editorutility_lib = unreal.EditorUtilityLibrary()
        # create asset tools object
        assettools = unreal.AssetToolsHelpers.get_asset_tools()
        # get selected assets
        selected_assets = editorutility_lib.get_selected_assets()

        export_path = 'C://'

        if self.rb_manualexport.isChecked():
            self.warning_console.setText("Exporting Assets using Dialog ")
            assettools.export_assets_with_dialog(selected_assets, prompt_for_individual_filenames=True)
        else:
            self.warning_console.setText("Exporting Assets automatically into Destination Folder")
            assettools.export_assets(selected_assets, export_path)

    # misc tools

    def materialinstancecreate(self):
        """

        """
        editorasset_lib = unreal.EditorAssetLibrary()
        material_parent = editorasset_lib.load_asset('')

    def multimaterialinstacer(self):
        """
            Create multiple material instances for one or more materials
        """
        # instances of unreal classes
        globaleditor = unreal.GlobalEditorUtilityBase
        matediting_lib = unreal.MaterialEditingLibrary
        editorutil_lib = unreal.EditorUtilityLibrary()

        new_asset_name = ''
        source_asset_path = ''
        created_asset_path = ''
        number_of_instances = self.sp_materialinstance.value()
        factory = unreal.MaterialInstanceConstantFactoryNew()
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

        # get selected assets
        selected_assets = editorutil_lib.get_selected_assets()

        if not selected_assets:
            self.warning_console.setText("Select atleast one material")

        for selected_asset in selected_assets:
            if isinstance(selected_asset, unreal.Material):
                new_asset_name = selected_asset.get_name() + "_%s_%d"
                source_asset_path = selected_asset.get_path_name()

                created_asset_path = source_asset_path.replace(selected_asset.get_name(), "-")
                created_asset_path = created_asset_path.replace("-.-", "")

                for x in range (number_of_instances):
                    new_asset = asset_tools.create_asset(new_asset_name %("inst", x+1), created_asset_path, None, factory)
                    matediting_lib.set_material_instance_parent(new_asset, selected_asset)
            else:
                self.warning_console.setText("Select a material")



    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())

    def closewindow(self):
        """
        Close the window.
        """
        self.destroy()


def openwindow():
    """
    Create tool window.
    """

    if QtWidgets.QApplication.instance():
        # id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'toolWindow' in win.objectName():  # update this name to match name below
                win.destroy()
    else:
        QtWidgets.QApplication(sys.argv)

    # load UI into QApp instance
    UnrealWidget.window = UnrealWidget()
    UnrealWidget.window.show()
    UnrealWidget.window.setObjectName('toolWindow')  # update this with something unique to your tool
    UnrealWidget.window.setWindowTitle('Quick Assistant : The Editor Toolkit')

    unreal.parent_external_window_to_slate(UnrealWidget.window.winId())



openwindow()
