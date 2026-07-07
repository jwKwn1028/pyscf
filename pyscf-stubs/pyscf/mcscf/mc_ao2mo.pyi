from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.ao2mo import outcore as outcore
from pyscf.lib import logger as logger

libmcscf: Incomplete

def trans_e1_incore(eri_ao, mo, ncore, ncas): ...
def trans_e1_outcore(mol, mo, ncore, ncas, erifile, max_memory=None, level: int = 1, verbose=...): ...

class _ERIS:
    vhf_c: Incomplete
    feri: Incomplete
    ppaa: Incomplete
    papa: Incomplete
    def __init__(self, casscf, mo, method: str = 'incore', level: int = 1) -> None: ...

def prange(start, end, step) -> Generator[Incomplete]: ...
