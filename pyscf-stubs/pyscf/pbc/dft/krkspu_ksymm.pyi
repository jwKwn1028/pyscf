from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.dft import krks_ksymm as krks_ksymm, krkspu as krkspu

def get_veff(ks, cell=None, dm=None, dm_last: int = 0, vhf_last: int = 0, hermi: int = 1, kpts=None, kpts_band=None): ...

class KsymAdaptedKRKSpU(krks_ksymm.KRKS):
    get_veff = get_veff
    energy_elec = krkspu.energy_elec
    to_hf: Incomplete
    def __init__(self, cell, kpts=..., xc: str = 'LDA,VWN', exxdiv=..., U_idx=[], U_val=[], C_ao_lo=None, minao_ref: str = 'MINAO', **kwargs) -> None: ...
KRKSpU = KsymAdaptedKRKSpU
