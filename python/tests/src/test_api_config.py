import unittest
import mock
from src.api_config import ApiConfig

class ApiConfigTest(unittest.TestCase):

    mock_os_environ_minimal = {'PINTEREST_APP_ID': 'test-app-id',
                               'PINTEREST_APP_SECRET': 'test-app-secret'
                               }

    @mock.patch.dict('os.environ', mock_os_environ_minimal, clear=True)
    def test_api_config_default(self):
        api_config = ApiConfig()
        self.assertEqual(api_config.app_id, 'test-app-id')
        self.assertEqual(api_config.app_secret, 'test-app-secret')
        self.assertEqual(api_config.port, 8085)
        self.assertEqual(api_config.redirect_uri, 'https://localhost:8085/')
        self.assertEqual(api_config.landing_uri, 'https://developers.pinterest.com/manage/test_app_id')
        self.assertEqual(api_config.https_key_file, 'localhost-key.pem')
        self.assertEqual(api_config.https_cert_file, 'localhost.pem')
        self.assertEqual(api_config.oauth_uri, 'https://www.pinterest.com')
        self.assertEqual(api_config.api_uri, 'https://api.pinterest.com')

    mock_os_environ_complete = {'PINTEREST_APP_ID': 'test-app-id',
                                'PINTEREST_APP_SECRET': 'test-app-secret',
                                'REDIRECT_LANDING_URI': 'test-landing-uri',
                                'HTTPS_KEY_FILE': 'test-https-key-file',
                                'HTTPS_CERT_FILE': 'test-https-cert-file',
                                'PINTEREST_OAUTH_URI': 'test-oauth-uri',
                                'PINTEREST_API_URI': 'test-api-uri'
                                }

    @mock.patch.dict('os.environ', mock_os_environ_complete, clear=True)
    def test_api_config_default(self):
        api_config = ApiConfig()
        self.assertEqual(api_config.app_id, 'test-app-id')
        self.assertEqual(api_config.app_secret, 'test-app-secret')
        self.assertEqual(api_config.port, 8085)
        self.assertEqual(api_config.redirect_uri, 'https://localhost:8085/')
        self.assertEqual(api_config.landing_uri, 'test-landing-uri')
        self.assertEqual(api_config.https_key_file, 'test-https-key-file')
        self.assertEqual(api_config.https_cert_file, 'test-https-cert-file')
        self.assertEqual(api_config.oauth_uri, 'test-oauth-uri')
        self.assertEqual(api_config.api_uri, 'test-api-uri')
        
        