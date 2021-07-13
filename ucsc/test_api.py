import unittest

from ucsc.api import Hub, NotFoundException


class MyTestCase(unittest.TestCase):
    def test_it_returns_a_hub_object_if_it_exists(self):
        hub = Hub.find('ALFA Hub')
        self.assertIsInstance(hub, Hub)

        with self.assertRaises(NotFoundException):
            Hub.find('Hello there')

    def test_it_returns_a_hub_object_by_attribute_if_it_exists(self):
        hub = Hub.findBy('name','ALFA Hub')
        self.assertIsInstance(hub, Hub)

        with self.assertRaises(NotFoundException):
            Hub.findBy('name','Hello there')

    def test_it_returns_all_hubs_as_lists(self):
        hubs = Hub.get()
        self.assertIsInstance(hubs, list)

    def test_it_returns_all_genomes_in_a_hub_as_lists(self):
        hub = Hub.findBy('name', 'ALFA Hub')
        genomes = hub.genomes
        self.assertIsInstance(genomes, list)





if __name__ == '__main__':
    unittest.main()
