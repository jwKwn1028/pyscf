import pyscf.scf.ghf as mol_ghf
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf import addons as addons, hf as pbchf
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.gks import GKS
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.hf import SCF
from pyscf.pbc.scf.kghf import KGHF
from typing import Optional, Tuple, Union

def get_jk(mf: Union[GHF, GKS], cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, hermi: int = 0, kpt: Optional[ndarray]=None, kpts_band: None=None, with_j: bool = True, with_k: bool = True, **kwargs) -> Union[Tuple[ndarray, None], Tuple[ndarray, ndarray]]: ...

class GHF(pbchf.SCF):
    with_soc: Incomplete
    def __init__(self, cell: Cell, kpt: Optional[ndarray]=None, exxdiv: str=...) -> None: ...
    init_guess_by_chkfile: Incomplete
    init_guess_by_minao: Incomplete
    init_guess_by_atom: Incomplete
    init_guess_by_huckel: Incomplete
    get_jk = get_jk
    get_occ = mol_ghf.get_occ
    get_grad: Incomplete
    analyze: Incomplete
    mulliken_pop: Incomplete
    mulliken_meta: Incomplete
    spin_square: Incomplete
    stability: Incomplete
    gen_response = NotImplemented
    def get_hcore(self, cell: Optional[Cell]=None, kpt: None=None) -> ndarray: ...
    def get_ovlp(self, cell: Optional[Cell]=None, kpt: None=None) -> ndarray: ...
    def get_veff(self, cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[NPArrayWithTag, int, ndarray] = 0, vhf_last: Union[ndarray, int] = 0, hermi: int = 1, kpt: None=None, kpts_band: None=None) -> ndarray: ...
    def get_bands(self, kpts_band, cell=None, dm=None, kpt=None) -> None: ...
    def x2c1e(self): ...
    x2c = x2c1e
    sfx2c1e = x2c1e
    def to_ks(self, xc: str = 'HF'): ...
    def convert_from_(self, mf: SCF) -> Union[KGHF, GHF]: ...
    to_gpu = lib.to_gpu
