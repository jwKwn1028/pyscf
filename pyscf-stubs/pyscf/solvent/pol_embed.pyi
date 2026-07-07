from _typeshed import Incomplete
from pyscf import df as df, gto as gto, lib as lib, scf as scf
from pyscf.data import elements as elements
from pyscf.lib import logger as logger
from pyscf.solvent import _attach_solvent

min_version: str

def pe_for_scf(mf, solvent_obj, dm=None): ...
def pe_for_casscf(mc, solvent_obj, dm=None): ...
def pe_for_casci(mc, solvent_obj, dm=None): ...
def pe_for_post_scf(method, solvent_obj, dm=None): ...
def pe_for_tdscf(method, solvent_obj=None, dm=None, equilibrium_solvation: bool = False): ...

class TDSCFWithSolvent(_attach_solvent.TDSCFWithSolvent):
    def gen_response(self, *args, **kwargs): ...
    get_ab = NotImplemented
    nuc_grad_method = NotImplemented

class PolEmbed(lib.StreamObject):
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    max_cycle: int
    conv_tol: float
    state_id: int
    frozen: bool
    equilibrium_solvation: bool
    options: Incomplete
    do_ecp: Incomplete
    eef: Incomplete
    cppe_state: Incomplete
    potentials: Incomplete
    V_es: Incomplete
    ecpmol: Incomplete
    e: Incomplete
    v: Incomplete
    def __init__(self, mol, options_or_potfile) -> None: ...
    def build(self): ...
    def dump_flags(self, verbose=None): ...
    def reset(self, mol=None): ...
    def kernel(self, dm, elec_only: bool = False): ...
    def effective_dipole_operator(self): ...
    def nuc_grad_method(self, grad_method) -> None: ...
