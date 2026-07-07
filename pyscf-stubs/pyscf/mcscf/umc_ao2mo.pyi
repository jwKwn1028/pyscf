from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.lib import logger as logger

libmcscf: Incomplete

def trans_e1_incore(eri_ao, mo, ncore, ncas): ...
def trans_e1_outcore(mol, mo, ncore, ncas, max_memory=None, ioblk_size: int = 512, verbose=...): ...

class _ERIS:
    vhf_c: Incomplete
    def __init__(self, casscf, mo, method: str = 'incore') -> None: ...
