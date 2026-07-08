from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import gen_grid as gen_grid, krks as krks, multigrid as multigrid, rks as rks
from pyscf.pbc.scf import khf as khf, khf_ksymm as khf_ksymm
from numpy import float64, ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.krkspu_ksymm import KsymAdaptedKRKSpU
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from typing import Optional, Tuple, Union

def get_veff(ks: Union[KsymAdaptedKRKS, KsymAdaptedKRKSpU], cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, int, NPArrayWithTag] = 0, vhf_last: Union[int, NPArrayWithTag] = 0, hermi: int = 1, kpts: Optional[KPoints]=None, kpts_band: Optional[ndarray]=None) -> NPArrayWithTag: ...

class KsymAdaptedKRKS(krks.KRKS, khf_ksymm.KRHF):
    reset: Incomplete
    get_veff = get_veff
    kpts: Incomplete
    kmesh: Incomplete
    get_ovlp: Incomplete
    get_hcore: Incomplete
    get_jk: Incomplete
    get_occ: Incomplete
    init_guess_by_chkfile: Incomplete
    dump_chk: Incomplete
    eig: Incomplete
    get_orbsym: Incomplete
    orbsym: Incomplete
    get_init_guess: Incomplete
    def __init__(self, cell: Cell, kpts: KPoints=..., xc: str = 'LDA,VWN', exxdiv: str=..., **kwargs) -> None: ...
    def dump_flags(self, verbose: None=None) -> Union[KsymAdaptedKRKS, KsymAdaptedKRKSpU]: ...
    def energy_elec(self, dm_kpts: Optional[Union[ndarray, NPArrayWithTag]]=None, h1e_kpts: Optional[ndarray]=None, vhf: Optional[NPArrayWithTag]=None) -> Tuple[float64, float64]: ...
    def to_hf(self): ...
KRKS = KsymAdaptedKRKS
