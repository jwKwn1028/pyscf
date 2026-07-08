from _typeshed import Incomplete
from itertools import product as product
from pyscf import ao2mo as ao2mo, gto as gto, lib as lib
from pyscf.df.grad.casdm2_util import grad_elec_auxresponse_dferi as grad_elec_auxresponse_dferi, grad_elec_dferi as grad_elec_dferi, solve_df_rdm2 as solve_df_rdm2
from pyscf.grad import casci as casci_grad
from pyscf.lib import logger as logger
from pyscf.mcscf.addons import StateAverageMCSCFSolver as StateAverageMCSCFSolver
from scipy import linalg as linalg
from numpy import ndarray
from pyscf.fci.direct_spin1 import FCIvector
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Tuple

def grad_elec(mc_grad: "Gradients", mo_coeff: Optional[ndarray]=None, ci: Optional[FCIvector]=None, atmlst: None=None, verbose: Optional[Logger]=None) -> ndarray: ...
def as_scanner(mcscf_grad): ...

class CASSCF_GradScanner(lib.GradScanner):
    def __init__(self, g) -> None: ...
    mol: Incomplete
    def __call__(self, mol_or_geom, **kwargs): ...

class Gradients(casci_grad.Gradients):
    with_df: Incomplete
    auxbasis_response: bool
    def __init__(self, mc) -> None: ...
    grad_elec = grad_elec
    def get_jk(self, mol: Optional[Mole]=None, dm: Optional[Tuple[ndarray, ndarray]]=None, hermi: int = 0) -> Tuple[NPArrayWithTag, NPArrayWithTag]: ...
    atmlst: Incomplete
    de: Incomplete
    def kernel(self, mo_coeff: Optional[ndarray]=None, ci: Optional[FCIvector]=None, atmlst: None=None, verbose: Optional[int]=None) -> ndarray: ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients
