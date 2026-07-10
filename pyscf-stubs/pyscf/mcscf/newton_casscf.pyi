from _typeshed import Incomplete
from itertools import product as product
from pyscf import lib as lib, scf as scf
from pyscf.lib import logger as logger
from pyscf.mcscf import addons as addons, casci as casci, mc1step as mc1step
from pyscf.mcscf.casci import canonicalize as canonicalize, cas_natorb as cas_natorb, get_fock as get_fock
from pyscf.soscf import ciah as ciah
from numpy import float64, ndarray
from pyscf.fci.direct_spin1 import FCIvector
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.hf import RHF
from pyscf.scf.hf_symm import SymAdaptedRHF
from typing import Callable, Dict, List, Optional, Tuple, Union

def gen_g_hop(casscf: Union[Incomplete, Incomplete, Incomplete], mo: Union[ndarray, NPArrayWithTag], ci0: Union[ndarray, FCIvector], eris: Union[Incomplete, Incomplete], verbose: None=None) -> Tuple[ndarray, Callable, Callable, ndarray]: ...
def extract_rotation(casscf: Union[Incomplete, Incomplete, Incomplete], dr: ndarray, u: Union[ndarray, int], ci0: Union[ndarray, FCIvector]) -> Tuple[ndarray, ndarray]: ...
def update_orb_ci(casscf, mo, ci0, eris, x0_guess=None, conv_tol_grad: float = 0.0001, max_stepsize=None, verbose=None): ...
def kernel(casscf: Union[Incomplete, Incomplete], mo_coeff: Union[ndarray, NPArrayWithTag], tol: float = 1e-07, conv_tol_grad: None=None, ci0: None=None, callback: None=None, verbose: int=..., dump_chk: bool = True) -> Union[Tuple[bool, float64, float64, FCIvector, NPArrayWithTag, ndarray], Tuple[bool, float64, float64, FCIvector, ndarray, ndarray]]: ...

class CASSCF(mc1step.CASSCF):
    __doc__: Incomplete
    frozen: Incomplete
    max_stepsize: float
    max_cycle_macro: int
    max_cycle_micro: int
    conv_tol: float
    conv_tol_grad: Incomplete
    ah_level_shift: float
    ah_conv_tol: float
    ah_max_cycle: int
    ah_lindep: float
    ah_start_tol: float
    ah_start_cycle: int
    ah_grad_trust_region: float
    kf_trust_region: float
    kf_interval: int
    internal_rotation: bool
    chkfile: Incomplete
    chk_ci: bool
    e_tot: Incomplete
    e_cas: Incomplete
    ci: Incomplete
    mo_coeff: Incomplete
    mo_energy: Incomplete
    converged: bool
    def __init__(self, mf_or_mol: Union[SymAdaptedRHF, RHF], ncas: int, nelecas: Union[int, Tuple[int, int]], ncore: None=None, frozen: None=None) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[Incomplete, Incomplete]: ...
    def kernel(self, mo_coeff: None=None, ci0: None=None, callback: None=None) -> Tuple[float64, float64, FCIvector, ndarray, ndarray]: ...
    def casci(self, mo_coeff: Union[ndarray, NPArrayWithTag], ci0: Optional[FCIvector]=None, eris: Optional[Incomplete]=None, verbose: Optional[Logger]=None, envs: Optional[Union[Dict[str, Optional[Union[Incomplete, NPArrayWithTag, float, int, bool, Logger, Tuple[float, float], Incomplete]]], Dict[str, Optional[Union[Incomplete, ndarray, float, int, bool, Logger, Tuple[float, float], Incomplete]]]]]=None) -> Tuple[float64, float64, FCIvector]: ...
    def update_ao2mo(self, mo) -> None: ...
