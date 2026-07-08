from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, gto as gto, lib as lib, mcscf as mcscf
from pyscf.df.grad.casdm2_util import grad_elec_auxresponse_dferi as grad_elec_auxresponse_dferi, grad_elec_dferi as grad_elec_dferi, solve_df_rdm2 as solve_df_rdm2
from pyscf.fci import cistring as cistring
from pyscf.fci.spin_op import spin_square0 as spin_square0
from pyscf.grad import lagrange as lagrange, sacasscf as sacasscf_grad
from pyscf.mcscf import mc1step as mc1step, mc1step_symm as mc1step_symm, newton_casscf as newton_casscf
from pyscf.mcscf.addons import StateAverageMCSCFSolver as StateAverageMCSCFSolver
from scipy import linalg as linalg
from numpy import ndarray

def Lorb_dot_dgorb_dx(Lorb, mc, mo_coeff=None, ci=None, atmlst=None, mf_grad=None, eris=None, verbose=None, auxbasis_response: bool = True): ...
def Lci_dot_dgci_dx(Lci, weights, mc, mo_coeff=None, ci=None, atmlst=None, mf_grad=None, eris=None, verbose=None, auxbasis_response: bool = True): ...
def as_scanner(mcscf_grad, state=None): ...

class CASSCF_GradScanner(lib.GradScanner):
    state: Incomplete
    def __init__(self, g, state) -> None: ...
    e_mcscf: Incomplete
    mol: Incomplete
    def __call__(self, mol_or_geom, **kwargs): ...

class Gradients(sacasscf_grad.Gradients):
    auxbasis_response: bool
    def __init__(self, mc, state=None) -> None: ...
    def kernel(self, **kwargs) -> ndarray: ...
    def get_LdotJnuc(self, Lvec: ndarray, **kwargs) -> ndarray: ...
    to_gpu = lib.to_gpu
