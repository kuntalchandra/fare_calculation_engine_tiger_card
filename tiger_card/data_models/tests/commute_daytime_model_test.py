from json import load
from unittest import TestCase
from tiger_card.data_models.commute_daytime_model import CommuteDayTimeModel


class CommuteDayTimeModelTest(TestCase):
    def setUp(self) -> None:
        self.days = CommuteDayTimeModel.instance().days_map()

    def test_days(self):
        # TODO: extend the test to validate all the objects
        self.assertListEqual(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                             list(self.days.keys()))
