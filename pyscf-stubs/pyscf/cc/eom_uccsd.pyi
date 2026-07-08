from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.cc import addons as addons, ccsd as ccsd, eom_rccsd as eom_rccsd, uccsd as uccsd, uintermediates as uintermediates
from pyscf.lib import logger as logger, module_method as module_method
from numpy import float64, int64, ndarray
from typing import Callable, List, Optional, Tuple, Union

def vector_to_amplitudes_ip(vector: ndarray, nmo: Tuple[int, int], nocc: Tuple[int, int]) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
def amplitudes_to_vector_ip(r1: List[ndarray], r2: List[ndarray]) -> ndarray: ...
def spatial2spin_ip(rx: Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]], orbspin: Optional[ndarray]=None) -> ndarray: ...
def spin2spatial_ip(rx: ndarray, orbspin: ndarray) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
def ipccsd_matvec(eom: "EOMIP", vector: ndarray, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None) -> ndarray: ...
def ipccsd_diag(eom: "EOMIP", imds: Optional[_IMDS]=None) -> ndarray: ...

class EOMIP(eom_rccsd.EOMIP):
    matvec = ipccsd_matvec
    l_matvec: Incomplete
    get_diag = ipccsd_diag
    ipccsd_star: Incomplete
    ccsd_star_contract: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc: Union[Incomplete, Incomplete]) -> None: ...
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag: Optional[ndarray]=None) -> List[ndarray]: ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self) -> int: ...
    def make_imds(self, eris: None=None) -> "_IMDS": ...

def vector_to_amplitudes_ea(vector: ndarray, nmo: Tuple[int, int], nocc: Tuple[int, int]) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
def amplitudes_to_vector_ea(r1: Union[Tuple[ndarray, ndarray], List[ndarray]], r2: Union[List[ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]) -> ndarray: ...
def spatial2spin_ea(rx: Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]], orbspin: Optional[ndarray]=None) -> ndarray: ...
def spin2spatial_ea(rx: ndarray, orbspin: ndarray) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
def eaccsd_matvec(eom: "EOMEA", vector: ndarray, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None) -> ndarray: ...
def eaccsd_diag(eom: "EOMEA", imds: Optional[_IMDS]=None) -> ndarray: ...

class EOMEA(eom_rccsd.EOMEA):
    matvec = eaccsd_matvec
    l_matvec: Incomplete
    get_diag = eaccsd_diag
    eaccsd_star: Incomplete
    ccsd_star_contract: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc: Union[Incomplete, Incomplete]) -> None: ...
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag: Optional[ndarray]=None) -> List[ndarray]: ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self) -> int: ...
    def make_imds(self, eris: None=None) -> "_IMDS": ...

def eeccsd(eom: "EOMEE", nroots: int = 1, koopmans: bool = False, guess: Optional[List[ndarray]]=None, eris: None=None, imds: None=None) -> Union[Tuple[ndarray, List[ndarray]], Tuple[float64, ndarray]]: ...
def eomee_ccsd(eom: Union[EOMEESpinFlip, EOMEESpinKeep], nroots: int = 1, koopmans: bool = False, guess: Optional[List[ndarray]]=None, eris: Optional[Union[Incomplete, Incomplete]]=None, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None) -> Union[Tuple[ndarray, List[ndarray]], Tuple[float64, ndarray]]: ...
def eomsf_ccsd(eom: "EOMEESpinFlip", nroots: int = 1, koopmans: bool = False, guess: Optional[List[ndarray]]=None, eris: Optional[Union[Incomplete, Incomplete]]=None, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None) -> Union[Tuple[ndarray, List[ndarray]], Tuple[float64, ndarray]]: ...
amplitudes_to_vector_ee = uccsd.amplitudes_to_vector
amplitudes_to_vector_eomee = uccsd.amplitudes_to_vector
vector_to_amplitudes_ee = uccsd.vector_to_amplitudes
vector_to_amplitudes_eomee = uccsd.vector_to_amplitudes

def amplitudes_to_vector_eomsf(t1: Tuple[ndarray, ndarray], t2: Tuple[ndarray, ndarray, ndarray, ndarray], out: None=None) -> ndarray: ...
def vector_to_amplitudes_eomsf(vector: ndarray, nmo: Tuple[int, int], nocc: Tuple[int, int]) -> Tuple[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
spatial2spin_eomee = addons.spatial2spin
spin2spatial_eomee = addons.spin2spatial

def spatial2spin_eomsf(rx: Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]], orbspin: Optional[ndarray]=None) -> ndarray: ...
def spin2spatial_eomsf(rx: ndarray, orbspin: ndarray) -> Union[Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray, ndarray]]: ...
def eomee_ccsd_matvec(eom: "EOMEESpinKeep", vector: ndarray, imds: Optional[_IMDS]=None) -> ndarray: ...
def eomsf_ccsd_matvec(eom: "EOMEESpinFlip", vector: ndarray, imds: Optional[_IMDS]=None) -> ndarray: ...
def eeccsd_diag(eom: Union[EOMEE, EOMEESpinFlip, EOMEESpinKeep], imds: Optional[_IMDS]=None) -> Tuple[ndarray, ndarray]: ...

class EOMEE(eom_rccsd.EOMEE):
    nocc: Incomplete
    nmo: Incomplete
    def __init__(self, cc: Union[Incomplete, Incomplete]) -> None: ...
    kernel = eeccsd
    eeccsd = eeccsd
    get_diag = eeccsd_diag
    def vector_size(self) -> int64: ...
    def make_imds(self, eris: Optional[Union[Incomplete, Incomplete]]=None) -> "_IMDS": ...

class EOMEESpinKeep(EOMEE):
    kernel = eomee_ccsd
    eomee_ccsd = eomee_ccsd
    matvec = eomee_ccsd_matvec
    get_diag = eeccsd_diag
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag: Optional[ndarray]=None) -> List[ndarray]: ...
    def gen_matvec(self, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None, **kwargs) -> Tuple[Callable, ndarray]: ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self) -> int: ...

class EOMEESpinFlip(EOMEE):
    kernel = eomsf_ccsd
    eomsf_ccsd = eomsf_ccsd
    matvec = eomsf_ccsd_matvec
    def get_init_guess(self, nroots: int = 1, koopmans: bool = True, diag: Optional[ndarray]=None) -> List[ndarray]: ...
    def gen_matvec(self, imds: Optional[_IMDS]=None, diag: Optional[ndarray]=None, **kwargs) -> Tuple[Callable, ndarray]: ...
    amplitudes_to_vector: Incomplete
    vector_to_amplitudes: Incomplete
    spatial2spin: Incomplete
    spin2spatial: Incomplete
    def vector_size(self) -> int: ...

class _IMDS:
    verbose: Incomplete
    stdout: Incomplete
    t1: Incomplete
    t2: Incomplete
    eris: Incomplete
    made_ip_imds: bool
    made_ea_imds: bool
    made_ee_imds: bool
    def __init__(self, cc: Union[Incomplete, Incomplete], eris: Optional[Union[Incomplete, Incomplete]]=None) -> None: ...
    def make_ip(self) -> "_IMDS": ...
    Wvvvv: Incomplete
    def make_ea(self) -> "_IMDS": ...
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
