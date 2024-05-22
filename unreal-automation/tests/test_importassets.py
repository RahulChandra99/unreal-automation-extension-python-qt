import unittest
from unittest.mock import MagicMock, patch
import os
import Scripts.unreal
from Scripts.automation_methods.import_assets import import_assets


class TestAssetImporter(unittest.TestCase):
    @patch('unreal.AssetToolsHelpers.get_asset_tools')
    @patch('unreal.AutomatedAssetImportData')
    def test_import_assets(self, mock_AutomatedAssetImportData, mock_get_asset_tools):
        # Create an instance of the AssetImporter
        importer = import_assets()

        # Mocking the AssetTools object
        mock_asset_tools = MagicMock()
        mock_get_asset_tools.return_value = mock_asset_tools

        # Mocking the AutomatedAssetImportData object
        mock_import_data = MagicMock()
        mock_AutomatedAssetImportData.return_value = mock_import_data

        # Call the import_assets method
        importer.import_assets()

        # Check that get_asset_tools was called
        mock_get_asset_tools.assert_called_once()

        # Check that AutomatedAssetImportData was instantiated
        mock_AutomatedAssetImportData.assert_called_once()

        # Check the attributes of assetImportData
        self.assertEqual(mock_import_data.destination_path, '/Game/')
        self.assertEqual(mock_import_data.filenames, ['D:\\abc.fbx'])
        self.assertTrue(mock_import_data.replace_existing)

        # Check that import_assets_automated was called with the correct arguments
        mock_asset_tools.import_assets_automated.assert_called_once_with(mock_import_data)

if __name__ == '__main__':
    unittest.main()
