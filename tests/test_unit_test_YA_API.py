import unittest
import requests
from parameterized import parameterized
from unittest.mock import patch
from main_hw_YA_API import create_folder


class TestFunctions(unittest.TestCase):

    def test_create_folder(self):

        ya_token = 'AQAAAAA1RjtIAADLW3Cq_QCE_047lq5Xt2jj9xc'
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {ya_token}'}

        create_folder('test')
        result = str(requests.get(f'{url}?path=test', headers=headers))
        expected_result = '<Response [200]>'

        self.assertEqual(result, expected_result)