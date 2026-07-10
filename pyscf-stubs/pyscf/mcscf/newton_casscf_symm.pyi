from _typeshed import Incomplete
from pyscf import fci as fci, lib as lib
from pyscf.lib import logger as logger
from pyscf.mcscf import casci_symm as casci_symm, mc1step as mc1step, newton_casscf as newton_casscf
from numpy import float64, ndarray
from pyscf.fci.direct_spin1 import FCIvector
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.scf.hf_symm import SymAdaptedRHF
from typing import Optional, Tuple

class CASSCF(newton_casscf.CASSCF):
    __doc__: Incomplete
    fcisolver: Incomplete
    def __init__(self, mf_or_mol: SymAdaptedRHF, ncas: int = 0, nelecas: Tuple[int, int] = 0, ncore: None=None, frozen: None=None) -> None: ...
    mo_coeff: Incomplete
    def kernel(self, mo_coeff: None=None, ci0: None=None, callback: None=None, _kern: None=None) -> Tuple[float64, float64, FCIvector, NPArrayWithTag, ndarray]: ...
    def uniq_var_indices(self, nmo: int, ncore: int, ncas: int, frozen: None) -> ndarray: ...
    def rotate_mo(self, mo: NPArrayWithTag, u: ndarray, log: Optional[Logger]=None) -> NPArrayWithTag: ...
