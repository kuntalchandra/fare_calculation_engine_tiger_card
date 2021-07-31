from os import getcwd
from unittest import TestCase
from tiger_card.services.commute_compute import CommuteComputeService
from tiger_card.cli import process_file


class TigerCardFileInputTest(TestCase):
    def setUp(self):
        self.input_file = "/tests/fixtures/file_input_daily_cap.txt"
        self.output_file = "/tests/fixtures/file_output_daily_cap.txt"
        # TODO: Test for the weekly cap

    def test_calculate_fare(self):
        input_path = getcwd() + self.input_file
        output_path = getcwd() + self.output_file

        with open(output_path) as fp:
            expected_output = fp.readlines()  # Output fixture
        expected_output = [int(val) for val in expected_output]
        compute_commute_service = CommuteComputeService()
        self.assertListEqual(process_file(compute_commute_service, input_path), expected_output)
