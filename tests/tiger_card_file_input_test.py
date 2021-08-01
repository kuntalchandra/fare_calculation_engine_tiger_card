from os import getcwd
from unittest import TestCase
from tiger_card.services.commute_compute import CommuteComputeService
from tiger_card.cli import process_file


class TigerCardFileInputTest(TestCase):
    def setUp(self):
        pass

    def test_calculate_fare(self):
        input_path = getcwd() + "/tests/fixtures/input_fare.txt"
        output_path = getcwd() + "/tests/fixtures/output_fare.txt"

        with open(output_path) as fp:
            expected_output = fp.readlines()  # Output fixture
        expected_output = [int(val) for val in expected_output]
        compute_commute_service = CommuteComputeService()
        self.assertListEqual(process_file(compute_commute_service, input_path), expected_output)

    def test_calculate_daily_cap(self):
        input_path = getcwd() + "/tests/fixtures/input_daily_cap.txt"
        output_path = getcwd() + "/tests/fixtures/output_daily_cap.txt"

        with open(output_path) as fp:
            expected_output = fp.readlines()
        expected_output = [int(val) for val in expected_output]
        compute_commute_service = CommuteComputeService()
        self.assertListEqual(process_file(compute_commute_service, input_path), expected_output)

    def test_calculate_weekly_cap(self):
        input_path = getcwd() + "/tests/fixtures/input_weekly_cap.txt"
        output_path = getcwd() + "/tests/fixtures/output_weekly_cap.txt"

        with open(output_path) as fp:
            expected_output = fp.readlines()
        expected_output = [int(val) for val in expected_output]
        compute_commute_service = CommuteComputeService()
        self.assertListEqual(process_file(compute_commute_service, input_path), expected_output)
