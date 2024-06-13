import ctypes

class TurboEncabulatorInputs(ctypes.Structure):
    _fields_ = [
        ("EncabulatorEnergized", ctypes.c_bool),
        ("MegnetoReluctance", ctypes.c_int),
        ("SinusoidalRepleneration", ctypes.c_int)
    ]

class TurboEncabulatorOutputs(ctypes.Structure):
    _fields_ = [
        ("FluxPower", ctypes.c_int),
        ("HeadChopper", ctypes.c_bool),
    ]

_dll_handle = ctypes.WinDLL ("./build/TurboEncabulator.dll")

def turbo_encabulator(input_vars: TurboEncabulatorInputs) -> TurboEncabulatorOutputs:
    output_vars = TurboEncabulatorOutputs()
    _dll_handle.TurboEncabulatorWrapper(ctypes.byref(input_vars), ctypes.byref(output_vars))
    return output_vars
