import unittest

from ucsc.api import Hub, NotFoundException


class MyTestCase(unittest.TestCase):
    def test_it_returns_a_hub_object_if_it_exists(self):
        hub = Hub.find('ALFA Hub')
        self.assertIsInstance(hub, Hub)

        with self.assertRaises(NotFoundException):
            Hub.find('Hello there')



if __name__ == '__main__':
    unittest.main()
