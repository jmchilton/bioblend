"""
Use ``nose`` to run these unit tests.
"""
import GalaxyTestBase
import test_util


@test_util.skip_unless_galaxy()
class TestGalaxyDatasets(GalaxyTestBase.GalaxyTestBase):

    def setUp(self):
        super(TestGalaxyDatasets, self).setUp()
        self.history_id = self.gi.histories.create_history(name='TestShowDataset')['id']
        self.dataset_id = self._test_dataset(self.history_id)

    def test_show_dataset(self):
        with self.assertRaises(Exception):
            self.gi.datasets.show_dataset(None)
        self.gi.datasets.show_dataset(self.dataset_id)

    def test_download_dataset(self):
        with self.assertRaises(Exception):
            self.gi.datasets.download_dataset(None)
        self._wait_for_history(self.history_id)
        self.gi.datasets.download_dataset(self.dataset_id)

    def test_show_stderr(self):
        stderr = self.gi.datasets.show_stderr(self.dataset_id)
        self.assertIsNotNone(stderr)

    def test_show_stdout(self):
        stdout = self.gi.datasets.show_stdout(self.dataset_id)
        self.assertIsNotNone(stdout)
