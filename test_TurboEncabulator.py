from .TurboEncabulator import TurboEncabulatorInputs, turbo_encabulator

import pytest

@pytest.mark.parametrize("test_input, expected", [((True, 1, 2), 3), ((False, 2, 3), 5), ((True, 23, 4), 27)])
def test_flux_power(test_input, expected):
    input_vars = TurboEncabulatorInputs(*test_input)
    output_vars = turbo_encabulator(input_vars)
    assert output_vars.FluxPower == expected

@pytest.mark.parametrize("test_input", [(True, 1, 2), (False, 2, 3), (True, 23, 4)])
def test_head_chopper(test_input):
    input_vars = TurboEncabulatorInputs(*test_input)
    output_vars = turbo_encabulator(input_vars)
    assert not output_vars.HeadChopper