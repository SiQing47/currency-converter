import unittest
from app import app

class TestCurrencyConverter(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_conversion_pass(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=$1,525')
        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['msg'], 'success')
        self.assertEqual(data['amount'], '$170,496.53')
    
    def test_conversion_miss_source(self):
        response = self.app.get('/convert?target=JPY&amount=$1,525')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'fail')
        self.assertEqual(data['error'], 'Missing source or target currency')
    
    def test_conversion_miss_target(self):
        response = self.app.get('/convert?source=JPY&amount=$1,525')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'fail')
        self.assertEqual(data['error'], 'Missing source or target currency')
    
    def test_conversion_miss_amount(self):
        response = self.app.get('/convert?source=USD&target=JPY')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'fail')
        self.assertEqual(data['error'], "Missing 'amount' parameter")
    
    def test_conversion_invalid_currency(self):
        response = self.app.get('/convert?source=OOO&target=JPY&amount=$1,525')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'fail')
        self.assertEqual(data['error'], 'Invalid currency')
    
    def test_conversion_invalid_amount(self):
        response = self.app.get('/convert?source=USD&target=JPY&amount=-456')
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['msg'], 'fail')
        self.assertEqual(data['error'], 'Invalid amount')

if __name__ == '__main__':
    unittest.main()