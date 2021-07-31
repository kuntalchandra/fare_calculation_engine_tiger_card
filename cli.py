import click
from os import path
from typing import List
from tiger_card.services.commute_compute import CommuteComputeService
from tiger_card.exceptions import InvalidCommandException

commands = (
    "calculate_fare"
)


@click.command()
@click.argument("input_file", type=str, required=False)
def tiger_card(input_file: str) -> None:
    commute_compute_service = CommuteComputeService()
    if input_file:
        process_file(commute_compute_service, input_file)
    else:
        process_input(commute_compute_service)
    process_file(commute_compute_service, input_file)


def process_file(compute_commute_service: CommuteComputeService, input_file: str) -> List[int]:
    if not path.exists(input_file):
        raise FileNotFoundError(input_file)
    output = []
    with open(input_file) as fp:
        lines = fp.readlines()
        for line in lines:
            output.append(decide_action(compute_commute_service, line))
    return output


def process_input(commute_compute_service: CommuteComputeService) -> None:
    raise NotImplementedError("Manual input/output is not needed atm")


def decide_action(compute_commute_service: CommuteComputeService, line: str) -> int:
    line = line.strip().split()
    # decide action
    command = line[0]
    if command not in commands:
        raise InvalidCommandException(command)
    # get action input
    params = line[1:]
    command_function = getattr(compute_commute_service, command)
    return command_function(*params)


if __name__ == "__main__":
    tiger_card()
