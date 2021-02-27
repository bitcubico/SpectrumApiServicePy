import unittest

from spectrum_api_service import SpectrumApiService


class MyTestCase(unittest.TestCase):
    def test_validate_existence_of_host(self):
        exception = False
        try:
            api_service = SpectrumApiService()
        except:
            exception = True

        self.assertEqual(exception, True)


if __name__ == '__main__':
    unittest.main()
