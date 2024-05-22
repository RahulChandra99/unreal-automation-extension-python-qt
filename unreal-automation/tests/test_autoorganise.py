import unittest
from unittest.mock import MagicMock, patch
import os
import Scripts.unreal
from Scripts.automation_methods.auto_organise import auto_organise

# tested in unreal engine output log

class TestAutoOrganise(unittest.TestCase):
    @patch('unreal.EditorUtilityLibrary')
    @patch('unreal.SystemLibrary')
    @patch('unreal.EditorAssetLibrary')
    def test_auto_organise(self, mock_editor_asset_lib, mock_system_lib, mock_editor_util):
        # Setup mock return values
        asset1 = MagicMock()
        asset2 = MagicMock()
        asset3 = MagicMock()

        mock_editor_util.get_selected_assets.return_value = [asset1, asset2, asset3]
        mock_editor_asset_lib.get_path_name_for_loaded_asset.return_value = "/Game/Folder/Asset1"
        mock_system_lib.get_object_name.side_effect = ["Asset1", "Asset2", "Asset3"]
        mock_system_lib.get_class_display_name.side_effect = ["Class1", "Class2", "Class3"]

        asset1.get_class.return_value = MagicMock()
        asset2.get_class.return_value = MagicMock()
        asset3.get_class.return_value = MagicMock()

        # Call the function
        auto_organise()

        # Check that get_selected_assets was called once
        mock_editor_util.get_selected_assets.assert_called_once()

        # Check that get_path_name_for_loaded_asset was called once
        mock_editor_asset_lib.get_path_name_for_loaded_asset.assert_called_once_with(asset1)

        # Check that get_object_name and get_class_display_name were called for each asset
        self.assertEqual(mock_system_lib.get_object_name.call_count, 3)
        self.assertEqual(mock_system_lib.get_class_display_name.call_count, 3)

        # Check that rename_loaded_asset was called with the correct parameters
        mock_editor_asset_lib.rename_loaded_asset.assert_any_call(asset1, "\\Game/Folder/Class1/Asset1")
        mock_editor_asset_lib.rename_loaded_asset.assert_any_call(asset2, "\\Game/Folder/Class2/Asset2")
        mock_editor_asset_lib.rename_loaded_asset.assert_any_call(asset3, "\\Game/Folder/Class3/Asset3")

