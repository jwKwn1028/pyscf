from _typeshed import Incomplete
from pyscf import fci as fci, lib as lib, scf as scf, symm as symm
from pyscf.lib import logger as logger
from pyscf.mcscf import addons as addons, casci as casci
from pyscf.scf.hf_symm import SymAdaptedRHF, map_degeneracy as map_degeneracy
from numpy import float64, ndarray
from pyscf.fci.direct_spin1 import FCIvector
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcscf.mc1step_symm import SymAdaptedCASSCF
from pyscf.mcscf.newton_casscf_symm import CASSCF
from typing import Dict, Optional, Tuple, Union

class SymAdaptedCASCI(casci.CASCI):
    fcisolver: Incomplete
    def __init__(self, mf_or_mol: SymAdaptedRHF, ncas: int = 0, nelecas: Union[int, Tuple[int, int]] = 0, ncore: Optional[int]=None) -> None: ...
    @property
    def wfnsym(self): ...
    @wfnsym.setter
    def wfnsym(self, wfnsym) -> None: ...
    mo_coeff: Incomplete
    def kernel(self, mo_coeff: Optional[NPArrayWithTag]=None, ci0: None=None, verbose: None=None) -> Tuple[float64, float64, FCIvector, NPArrayWithTag, ndarray]: ...
    def sort_mo_by_irrep(self, cas_irrep_nocc: Dict[str, int], cas_irrep_ncore: None=None, mo_coeff: None=None, s: None=None) -> NPArrayWithTag: ...
    to_gpu = lib.to_gpu
CASCI = SymAdaptedCASCI

def eig(mat: Union[ndarray, NPArrayWithTag], orbsym: ndarray) -> Tuple[ndarray, ndarray]: ...
def label_symmetry_(mc: Union[CASSCF, SymAdaptedCASCI, SymAdaptedCASSCF], mo_coeff: Union[ndarray, NPArrayWithTag], ci0: Optional[FCIvector]=None) -> NPArrayWithTag: ...
