from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import krks_ksymm as krks_ksymm, krkspu as krkspu
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.lib.kpts import KPoints
from typing import List, Optional, Union

def get_veff(ks: "KsymAdaptedKRKSpU", cell: Optional[Cell]=None, dm: Optional[Union[ndarray, NPArrayWithTag]]=None, dm_last: Union[ndarray, NPArrayWithTag, int] = 0, vhf_last: Union[NPArrayWithTag, int] = 0, hermi: int = 1, kpts: None=None, kpts_band: None=None) -> NPArrayWithTag: ...

class KsymAdaptedKRKSpU(krks_ksymm.KRKS):
    get_veff = get_veff
    energy_elec = krkspu.energy_elec
    to_hf: Incomplete
    def __init__(self, cell: Cell, kpts: KPoints=..., xc: str = 'LDA,VWN', exxdiv: str=..., U_idx: List[str]=[], U_val: List[float]=[], C_ao_lo: Optional[str]=None, minao_ref: str = 'MINAO', **kwargs) -> None: ...
KRKSpU = KsymAdaptedKRKSpU
