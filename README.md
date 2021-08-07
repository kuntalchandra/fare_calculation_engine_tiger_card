# Fare Calculation Engine for the Tiger Card
## Problem Statement
*Refer to the functional spec*

## Virtual environment
`$ source venv/bin/activate`

## Install
run `$ bin/setup` *Includes tests*

## Interactive execution
run `$ bin/tiger_card` [Not implemented, future scope]

## Data model tests
run `$ nosetests tiger_card/data_models/tests/zone_model_test.py -v`

## Service tests
run `$ nosetests tiger_card/services/tests/ -v`

## E2E tests
run `$ nosetests tests/tiger_card_file_input_test.py -v`