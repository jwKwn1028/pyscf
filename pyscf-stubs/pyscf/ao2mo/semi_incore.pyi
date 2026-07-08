from pyscf import lib as lib
from pyscf.ao2mo.incore import iden_coeffs as iden_coeffs
from pyscf.lib import logger as logger

IOBLK_SIZE: int

def general(eri, mo_coeffs, erifile, dataname: str = 'eri_mo', ioblk_size=..., compact: bool = True, verbose=...): ...
