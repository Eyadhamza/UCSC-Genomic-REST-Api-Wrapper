import unittest

from ucsc.api import Hub, NotFoundException, Genome, Track, TrackSchema, Chromosome


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

    def test_it_can_find_a_genome_by_name_if_it_exists(self):

        self.assertTrue(Genome.exists('hg38','https://ftp.ncbi.nlm.nih.gov/snp/population_frequency/TrackHub/20200227123210/hub.txt'))
        genome = Genome.find('hg38')
        self.assertIsInstance(genome, Genome)

        with self.assertRaises(NotFoundException):
            Genome.find('hsssg38')

    def test_it_can_find_a_genome_by_attribute_if_it_exists(self):
        genome = Genome.findBy('name','hg38')
        self.assertIsInstance(genome, Genome)

        with self.assertRaises(NotFoundException):
            Genome.findBy('name','hsssg38')

    def test_it_can_get_tracks_of_genome(self):
        genome = Genome.findBy('name', 'hg38')
        tracks = genome.tracks
        self.assertIsInstance(tracks, list)

    def test_it_can_get_a_track_of_genome(self):
        genome = Genome.findBy('name', 'hg38')
        self.assertTrue(genome.isTrackExists('gold'))
        track = genome.findTrack('gold')
        self.assertIsInstance(track, Track)
        track2 = genome.findTrackBy('name','gold')
        self.assertIsInstance(track2, Track)

    def test_it_can_get_track_data_of_a_chromosome(self):
        chromosome = Chromosome.find('chr1', genome='hg38', track='gold')


    def test_it_can_get_schema_of_track(self):
        track = Track.find('gold','hg38')
        self.assertIsInstance(track.schema,list)

    def test_it_returns_a_list_of_all_chromosomes(self):
        chromosomes = Chromosome.get(genome='hg38',track='gold')
        self.assertIsInstance(chromosomes,list)

    def test_it_checks_if_chromosome_exists(self):
        self.assertTrue(Chromosome.exists('chr1',genome='hg38',track='gold'))
        self.assertFalse(Chromosome.exists('cr1',genome='hg38',track='gold'))

    def test_it_returns_a_chromosome_by_name(self):
        chromosomes = Chromosome.find('chr1',genome='hg38',track='gold')
        self.assertIsInstance(chromosomes,Chromosome)



if __name__ == '__main__':
    unittest.main()
