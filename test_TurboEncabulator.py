from .TurboEncabulator import TurboEncabulatorInputs, turbo_encabulator

import pytest

@pytest.mark.parametrize("test_input, expected", [
    ({"EncabulatorEnergized":True, "MegnetoReluctance":1, "SinusoidalRepleneration":2}, 3),
    ({"EncabulatorEnergized":False,"MegnetoReluctance":3, "SinusoidalRepleneration":8}, 11),
    ({"EncabulatorEnergized":True, "MegnetoReluctance":2, "SinusoidalRepleneration":6}, 8)
])
def test_flux_power(test_input, expected):
    input_vars = TurboEncabulatorInputs(**test_input)
    output_vars = turbo_encabulator(input_vars)
    assert output_vars.FluxPower == expected

@pytest.mark.parametrize("test_input", [
{"EncabulatorEnergized":True, "MegnetoReluctance":1, "SinusoidalRepleneration": 2},
{"EncabulatorEnergized":False,"MegnetoReluctance":3, "SinusoidalRepleneration": 8},
{"EncabulatorEnergized":True, "MegnetoReluctance":2, "SinusoidalRepleneration": 6}
])
def test_head_chopper(test_input):
    input_vars = TurboEncabulatorInputs(**test_input)
    output_vars = turbo_encabulator(input_vars)
    assert not output_vars.HeadChopper