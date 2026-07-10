from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.cc import addons as addons, ccsd as ccsd, eom_rccsd as eom_rccsd, uccsd as uccsd, uintermediates as uintermediates
from pyscf.lib import logger as logger, module_method as module_method

def vector_to_amplitudes_ip(vector, nmo, nocc): ...
def amplitudes_to_vector_ip(r1, r2): ...
def spatial2spin_ip(rx, orbspin=None): ...
def spin2spatial_ip(rx, orbspin): ...
def ipccsd_matvec(eom, vector, imds=None, diag=None): ...
def ipccsd_diag(eom, imds=None): ...

class EOMIP(eom_rccsd.EOMIP):
    matvec = ipccsd_matvec
    l_matvec: Incomplete
    get_diag = ipccsd_diag
    ipccsd_star: Incomplete
    ccsd_star_contract: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc) -> None: ...
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag=None): ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self): ...
    def make_imds(self, eris=None): ...

def vector_to_amplitudes_ea(vector, nmo, nocc): ...
def amplitudes_to_vector_ea(r1, r2): ...
def spatial2spin_ea(rx, orbspin=None): ...
def spin2spatial_ea(rx, orbspin): ...
def eaccsd_matvec(eom, vector, imds=None, diag=None): ...
def eaccsd_diag(eom, imds=None): ...

class EOMEA(eom_rccsd.EOMEA):
    matvec = eaccsd_matvec
    l_matvec: Incomplete
    get_diag = eaccsd_diag
    eaccsd_star: Incomplete
    ccsd_star_contract: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc) -> None: ...
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag=None): ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self): ...
    def make_imds(self, eris=None): ...

def eeccsd(eom, nroots: int = 1, koopmans: bool = False, guess=None, eris=None, imds=None): ...
def eomee_ccsd(eom, nroots: int = 1, koopmans: bool = False, guess=None, eris=None, imds=None, diag=None): ...
def eomsf_ccsd(eom, nroots: int = 1, koopmans: bool = False, guess=None, eris=None, imds=None, diag=None): ...
amplitudes_to_vector_ee = uccsd.amplitudes_to_vector
amplitudes_to_vector_eomee = uccsd.amplitudes_to_vector
vector_to_amplitudes_ee = uccsd.vector_to_amplitudes
vector_to_amplitudes_eomee = uccsd.vector_to_amplitudes

def amplitudes_to_vector_eomsf(t1, t2, out=None): ...
def vector_to_amplitudes_eomsf(vector, nmo, nocc): ...
spatial2spin_eomee = addons.spatial2spin
spin2spatial_eomee = addons.spin2spatial

def spatial2spin_eomsf(rx, orbspin=None): ...
def spin2spatial_eomsf(rx, orbspin): ...
def eomee_ccsd_matvec(eom, vector, imds=None): ...
def eomsf_ccsd_matvec(eom, vector, imds=None): ...
def eeccsd_diag(eom, imds=None): ...

class EOMEE(eom_rccsd.EOMEE):
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc) -> None: ...
    kernel = eeccsd
    eeccsd = eeccsd
    get_diag = eeccsd_diag
    def vector_size(self): ...
    def make_imds(self, eris=None): ...

class EOMEESpinKeep(EOMEE):
    kernel = eomee_ccsd
    eomee_ccsd = eomee_ccsd
    matvec = eomee_ccsd_matvec
    get_diag = eeccsd_diag
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag=None): ...
    def gen_matvec(self, imds=None, diag=None, **kwargs): ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self): ...

class EOMEESpinFlip(EOMEE):
    kernel = eomsf_ccsd
    eomsf_ccsd = eomsf_ccsd
    matvec = eomsf_ccsd_matvec
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag=None): ...
    def gen_matvec(self, imds=None, diag=None, **kwargs): ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self): ...

class _IMDS:
    verbose: Incomplete
    stdout: Incomplete
    t1: Incomplete
    t2: Incomplete
    eris: Incomplete
    made_ip_imds: bool
    made_ea_imds: bool
    made_ee_imds: bool
    def __init__(self, cc, eris=None) -> None: ...
    def make_ip(self): ...
    Wvvvv: Incomplete
    def make_ea(self): ...
    Fooa: Incomplete
    Foob: Incomplete
    Fvva: Incomplete
    Fvvb: Incomplete
    Fova: Incomplete
    Fovb: Incomplete
    wooov: Incomplete
    wOOOV: Incomplete
    wooOV: Incomplete
    wOOov: Incomplete
    woooo: Incomplete
    wOOOO: Incomplete
    wooOO: Incomplete
    saved: Incomplete
    wovvo: Incomplete
    wOVVO: Incomplete
    woVvO: Incomplete
    wOvVo: Incomplete
    woVVo: Incomplete
    wOvvO: Incomplete
    wovoo: Incomplete
    wOVOO: Incomplete
    woVoO: Incomplete
    wOvOo: Incomplete
    wvovv: Incomplete
    wVOVV: Incomplete
    wvOvV: Incomplete
    wVoVv: Incomplete
    def make_ee(self) -> None: ...
