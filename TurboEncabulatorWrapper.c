#include <stdbool.h>

struct TurboEncabulatorInstance {
    // inputs
    bool EncabulatorEnergized;
    int MegnetoReluctance;
    int SinusoidalRepleneration;
    // locals
    bool _;
    bool __;
    
    // constants
    int ______;
    int _______;
    int ________;
    int _________;
    // outputs
    int FluxPower;
    bool HeadChopper;
};

struct TurboEncabulatorInputs {
    bool EncabulatorEnergized;
    int MegnetoReluctance;
    int SinusoidalRepleneration;
};

struct TurboEncabulatorOutputs {
    int FluxPower;
    bool HeadChopper;
};

extern void TurboEncabulator(struct TurboEncabulatorInstance* encabulator);

__declspec(dllexport)
void TurboEncabulatorWrapper(struct TurboEncabulatorInputs* encabulator, struct TurboEncabulatorOutputs* outputs) {
    struct TurboEncabulatorInstance instance;
    instance.EncabulatorEnergized = encabulator->EncabulatorEnergized;
    instance.MegnetoReluctance = encabulator->MegnetoReluctance;
    instance.SinusoidalRepleneration = encabulator->SinusoidalRepleneration;
    TurboEncabulator(&instance);
    outputs->FluxPower = instance.FluxPower;
    outputs->HeadChopper = instance.HeadChopper;
}

