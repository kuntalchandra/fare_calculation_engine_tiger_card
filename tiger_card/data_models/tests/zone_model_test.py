from json import load
from os import getcwd
from unittest import TestCase
from tiger_card.data_models.zone_model import ZoneModel


class ZoneModelTest(TestCase):
    def setUp(self) -> None:
        self.zones_map = ZoneModel.instance().zones_map()

    def test_zones_map(self):
        with open(getcwd() + "/tiger_card/data_models/tests/fixtures/zone.json", "r") as fixture_file:
            fixture = load(fixture_file)
        self.assertEqual(fixture, self.zones_map)
