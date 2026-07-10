from _typeshed import Incomplete
from pyscf import df as df, lib as lib, scf as scf
from pyscf.mp.dfmp2_native import DFRMP2 as DFRMP2, ints3c_cholesky as ints3c_cholesky, orbgrad_from_Gamma as orbgrad_from_Gamma
from pyscf.scf import ucphf as ucphf

class DFUMP2(DFRMP2):
    mo_coeff: Incomplete
    mo_energy: Incomplete
    nocc: Incomplete
    nmo: Incomplete
    e_scf: Incomplete
    frozen_mask: Incomplete
    occ_mask: Incomplete
    mol: Incomplete
    auxmol: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    max_memory: Incomplete
    e_corr: Incomplete
    ps: float
    pt: float
    cphf_max_cycle: int
    cphf_tol: Incomplete
    def __init__(self, mf, frozen=None, auxbasis=None) -> None: ...
    def dump_flags(self, logger=None) -> None: ...
    def calculate_energy(self): ...
    def make_rdm1(self, relaxed: bool = False, ao_repr: bool = False): ...
    def make_natorbs(self, rdm1_mo=None, relaxed: bool = False): ...
    def calculate_integrals_(self) -> None: ...
    def delete(self) -> None: ...
    def nuc_grad_method(self) -> None: ...
    to_gpu = lib.to_gpu
MP2 = DFUMP2
UMP2 = DFUMP2
DFMP2 = DFUMP2

class SCSDFUMP2(DFUMP2):
    ps: Incomplete
    pt: Incomplete
    def __init__(self, mf, ps=..., pt=..., *args, **kwargs) -> None: ...
    def dump_flags(self, logger=None) -> None: ...
SCSMP2 = SCSDFUMP2
SCSUMP2 = SCSDFUMP2
SCSDFMP2 = SCSDFUMP2

def emp2_uhf(intsfiles, mo_energy, frozen_mask, logger, ps: float = 1.0, pt: float = 1.0): ...
def make_rdm1(mp2, relaxed, logger=None): ...
def ump2_densities_contribs(intsfiles, mo_energy, frozen_mask, max_memory, logger, calcGamma: bool = False, auxmol=None, ps: float = 1.0, pt: float = 1.0): ...
def fock_response_uhf(mf, dm, full: bool = True): ...
def solve_cphf_uhf(mf, Lvo, max_cycle, tol, logger): ...
