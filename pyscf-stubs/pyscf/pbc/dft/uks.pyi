import pyscf.dft
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, multigrid as multigrid, rks as rks
from pyscf.pbc.scf import uhf as pbcuhf

get_rho = rks.get_rho

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpt=None, kpts_band=None): ...
def gen_response(mf, mo_coeff=None, mo_occ=None, with_j: bool = True, hermi: int = 0, max_memory=None, with_nlc: bool = True): ...

class UKS(rks.KohnShamDFT, pbcuhf.UHF):
    get_rho = get_rho
    get_vsap: Incomplete
    init_guess_by_vsap: Incomplete
    get_veff = get_veff
    energy_elec = pyscf.dft.uks.energy_elec
    gen_response = gen_response
    def __init__(self, cell, kpt=None, xc: str = 'LDA,VWN', exxdiv=...) -> None: ...
    def dump_flags(self, verbose=None): ...
    def initialize_grids(self, cell, dm, kpts, ground_state: bool = True): ...
    def to_hf(self): ...
    def Gradients(self): ...
    multigrid_numint: Incomplete
    to_gpu = lib.to_gpu
