from pyscf import lib as lib
from pyscf.ao2mo.incore import iden_coeffs as iden_coeffs
from pyscf.lib import logger as logger
from numpy import ndarray
from typing import List

IOBLK_SIZE: int

def general(eri: ndarray, mo_coeffs: List[ndarray], erifile: str, dataname: str = 'eri_mo', ioblk_size: float=..., compact: bool = True, verbose: int=...) -> str: ...
