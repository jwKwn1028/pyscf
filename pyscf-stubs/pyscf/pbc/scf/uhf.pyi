from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf import addons as addons, chkfile as chkfile, hf as pbchf
from numpy import ndarray
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.uks import UKS
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.hf import RHF
from pyscf.pbc.scf.kuhf import KUHF
from typing import Callable, List, Optional, Tuple, Union

def init_guess_by_chkfile(cell: Cell, chkfile_name: str, project: Optional[bool]=None, kpt: Optional[ndarray]=None) -> NPArrayWithTag: ...
def dip_moment(cell: Cell, dm: NPArrayWithTag, unit: str = 'Debye', verbose: Logger=..., grids: None=None, rho: Optional[ndarray]=None, kpt: ndarray=...) -> ndarray: ...
get_rho = pbchf.get_rho

def gen_response(mf: "UHF", mo_coeff: Optional[ndarray]=None, mo_occ: Optional[ndarray]=None, with_j: bool = True, hermi: int = 0, max_memory: Optional[float]=None, with_nlc: bool = True) -> Callable: ...

class UHF(pbchf.SCF):
    init_guess_breaksym: Incomplete
    init_guess_by_minao: Incomplete
    init_guess_by_atom: Incomplete
    init_guess_by_huckel: Incomplete
    init_guess_by_mod_huckel: Incomplete
    eig: Incomplete
    get_fock: Incomplete
    get_grad: Incomplete
    get_occ: Incomplete
    make_rdm1: Incomplete
    make_rdm2: Incomplete
    energy_elec: Incomplete
    get_rho = get_rho
    analyze: Incomplete
    mulliken_pop: Incomplete
    mulliken_meta: Incomplete
    mulliken_meta_spin: Incomplete
    canonicalize: Incomplete
    spin_square: Incomplete
    stability: Incomplete
    gen_response = gen_response
    to_gpu = lib.to_gpu
    def __init__(self, cell: Cell, kpt: Optional[ndarray]=None, exxdiv: Optional[str]=...) -> None: ...
    @property
    def nelec(self): ...
    @nelec.setter
    def nelec(self, x) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[UHF, UKS]: ...
    def get_veff(self, cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag, List[ndarray]]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[ndarray, int] = 0, hermi: int = 1, kpt: Optional[ndarray]=None, kpts_band: Optional[ndarray]=None) -> ndarray: ...
    def get_bands(self, kpts_band: ndarray, cell: None=None, dm: None=None, kpt: None=None) -> Tuple[Tuple[List[ndarray], List[ndarray]], Tuple[List[ndarray], List[ndarray]]]: ...
    def dip_moment(self, cell: Optional[Cell]=None, dm: Optional[NPArrayWithTag]=None, unit: str = 'Debye', verbose: Logger=..., **kwargs) -> ndarray: ...
    def get_init_guess(self, cell: Optional[Cell]=None, key: str = 'minao', s1e: Optional[ndarray]=None) -> Union[ndarray, NPArrayWithTag]: ...
    def init_guess_by_1e(self, cell: Optional[Cell]=None) -> ndarray: ...
    def init_guess_by_chkfile(self, chk: None=None, project: bool = True, kpt: None=None) -> NPArrayWithTag: ...
    def get_fermi(self): ...
    def to_ks(self, xc: str = 'HF'): ...
    def convert_from_(self, mf: Union[RHF, KUHF]) -> "UHF": ...
    def Gradients(self): ...
