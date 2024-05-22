import unittest
from unittest.mock import MagicMock, patch
import os
import Scripts.unreal
from Scripts.automation_methods.create_project_folders import create_project_folders



class TestCreateFolder(unittest.TestCase):
    @patch('unreal.EditorAssetLibrary')
    @patch('unreal.log')
    def test_create_folder_success(self, mock_log, mock_editor_asset_library):
        # Setup mock return value for successful folder creation
        mock_editor_asset_library.make_directory.return_value = True

        # Call the function
        create_project_folders()

        # Check that make_directory was called with the correct path
        mock_editor_asset_library.make_directory.assert_called_once_with("/Game/NewFolder")

        # Check that the success log message was generated
        mock_log.assert_called_with("Folder created successfully at /Game/")

    @patch('unreal.EditorAssetLibrary')
    @patch('unreal.log')
    def test_create_folder_failure(self, mock_log, mock_editor_asset_library):
        # Setup mock to raise an OSError
        mock_editor_asset_library.make_directory.side_effect = OSError("Permission denied")

        # Call the function
        create_project_folders()

        # Check that make_directory was called with the correct path
        mock_editor_asset_library.make_directory.assert_called_once_with("/Game/NewFolder")

        # Check that the error log message was generated
        mock_log.assert_called_with("Error creating folder at /Game/ : Permission denied")


if __name__ == '__main__':
    unittest.main()
