from _typeshed import Incomplete
from itertools import product as product
from pyscf import ao2mo as ao2mo, gto as gto, lib as lib
from pyscf.df.grad.casdm2_util import grad_elec_auxresponse_dferi as grad_elec_auxresponse_dferi, grad_elec_dferi as grad_elec_dferi, solve_df_rdm2 as solve_df_rdm2
from pyscf.grad import casci as casci_grad
from pyscf.lib import logger as logger
from pyscf.mcscf.addons import StateAverageMCSCFSolver as StateAverageMCSCFSolver
from scipy import linalg as linalg

def grad_elec(mc_grad, mo_coeff=None, ci=None, atmlst=None, verbose=None): ...
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
    def get_jk(self, mol=None, dm=None, hermi: int = 0): ...
    atmlst: Incomplete
    de: Incomplete
    def kernel(self, mo_coeff=None, ci=None, atmlst=None, verbose=None): ...
    as_scanner = as_scanner
    to_gpu = lib.to_gpu
Grad = Gradients
