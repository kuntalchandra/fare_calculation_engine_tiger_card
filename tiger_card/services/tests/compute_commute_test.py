from unittest import TestCase
from tiger_card.services.commute_compute import CommuteComputeService


class ComputeCommuteServiceTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_daily_fares(self):
        commuting_times = ["10:20", "10:45", "16:15", "18:15", "19:00"]
        commuting_zones = [(2, 1), (1, 1), (1, 1), (1, 1), (1, 2)]
        expected_fares = [35, 25, 25, 30, 5]
        commute_compute_service = CommuteComputeService()
        fares = []
        total_fare = 0
        for commuting_time, zones in zip(commuting_times, commuting_zones):
            from_zone, to_zone = zones
            fare = commute_compute_service.calculate_fare(commute_day="Monday", commute_time=commuting_time,
                                                          from_zone=str(from_zone), to_zone=str(to_zone))
            fares.append(fare)
            total_fare += fare
        self.assertListEqual(expected_fares, fares)
        self.assertEqual(sum(expected_fares), total_fare)

    def test_weekly_fares(self):
        commuting_days = ["Monday", "Monday", "Monday", "Monday", "Monday", "Tuesday", "Tuesday", "Tuesday", "Tuesday",
                          "Tuesday", "Wednesday", "Wednesday", "Wednesday", "Wednesday", "Wednesday", "Thursday",
                          "Thursday", "Thursday", "Thursday", "Thursday", "Friday", "Friday", "Friday", "Saturday",
                          "Saturday", "Sunday"]
        commuting_times = ["10:20", "10:45", "16:15", "18:15", "19:00", "10:20", "10:45", "16:15", "18:15", "19:00",
                           "10:20", "10:45", "16:15", "18:15", "19:00", "10:20", "10:45", "16:15", "18:15", "19:00",
                           "10:20", "10:45", "16:00", "16:00", "16:30", "10:20"]
        commuting_zones = [(2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (2, 1),
                           (1, 1), (1, 1), (1, 1), (1, 2), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (2, 1), (1, 1),
                           (2, 2), (2, 2), (2, 2), (2, 1)]
        expected_fares = [35, 25, 25, 30, 5, 35, 25, 25, 30, 5, 35, 25, 25, 30, 5, 35, 25, 25, 30, 5, 35, 25, 20, 20,
                          20, 0]
        commute_compute_service = CommuteComputeService()
        fares = []
        total_fare = 0
        for commuting_day, commuting_time, zones in zip(commuting_days, commuting_times, commuting_zones):
            from_zone, to_zone = zones
            fare = commute_compute_service.calculate_fare(commute_day=commuting_day, commute_time=commuting_time,
                                                          from_zone=str(from_zone), to_zone=str(to_zone))
            fares.append(fare)
            total_fare += fare
        self.assertListEqual(expected_fares, fares)
        self.assertEqual(sum(expected_fares), total_fare)
