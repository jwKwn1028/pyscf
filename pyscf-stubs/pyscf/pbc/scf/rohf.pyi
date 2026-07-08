from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf import hf as pbchf, uhf as pbcuhf
from pyscf.scf import rohf as mol_rohf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

get_fock = mol_rohf.get_fock
get_occ = mol_rohf.get_occ
get_grad = mol_rohf.get_grad
make_rdm1 = mol_rohf.make_rdm1
energy_elec = mol_rohf.energy_elec
dip_moment = pbcuhf.dip_moment
get_rho: Incomplete

class ROHF(pbchf.RHF):
    get_init_guess: Incomplete
    init_guess_by_chkfile: Incomplete
    init_guess_by_minao: Incomplete
    init_guess_by_atom: Incomplete
    init_guess_by_huckel: Incomplete
    init_guess_by_mod_huckel: Incomplete
    eig: Incomplete
    get_fock: Incomplete
    get_occ: Incomplete
    get_grad: Incomplete
    get_rho = get_rho
    make_rdm1: Incomplete
    energy_elec: Incomplete
    analyze: Incomplete
    canonicalize: Incomplete
    spin_square: Incomplete
    stability: Incomplete
    dip_moment: Incomplete
    gen_response = pbcuhf.gen_response
    to_gpu = lib.to_gpu
    def __init__(self, cell: Cell, kpt: Optional[ndarray]=None, exxdiv: str=...) -> None: ...
    @property
    def nelec(self): ...
    @nelec.setter
    def nelec(self, x) -> None: ...
    def dump_flags(self, verbose: None=None) -> "ROHF": ...
    def get_veff(self, cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[ndarray, int] = 0, hermi: int = 1, kpt: None=None, kpts_band: None=None) -> ndarray: ...
    def get_bands(self, kpts_band, cell=None, dm=None, kpt=None) -> None: ...
    def init_guess_by_1e(self, cell: None=None) -> NPArrayWithTag: ...
    def to_ks(self, xc: str = 'HF'): ...
