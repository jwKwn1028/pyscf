from _typeshed import Incomplete
from collections.abc import Generator
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.ao2mo import outcore as outcore
from pyscf.lib import logger as logger
from numpy import float64, int64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.misc import H5TmpFile
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcscf.mc1step import CASSCF_Scanner
from pyscf.mcscf.mc1step_symm import SymAdaptedCASSCF
from typing import Iterator, Optional, Tuple, Union

libmcscf: Incomplete

def trans_e1_incore(eri_ao: ndarray, mo: Union[ndarray, NPArrayWithTag], ncore: Union[int64, int], ncas: Union[int64, int]) -> Tuple[ndarray, ndarray, ndarray, ndarray]: ...
def trans_e1_outcore(mol: Mole, mo: Union[ndarray, NPArrayWithTag], ncore: int, ncas: int, erifile: H5TmpFile, max_memory: Optional[Union[float, int]]=None, level: int = 1, verbose: Logger=...) -> Tuple[ndarray, ndarray]: ...

class _ERIS:
    vhf_c: Incomplete
    feri: Incomplete
    ppaa: Incomplete
    papa: Incomplete
    def __init__(self, casscf: Union[CASSCF_Scanner, Incomplete, Incomplete, SymAdaptedCASSCF, Incomplete], mo: Union[ndarray, NPArrayWithTag], method: str = 'incore', level: int = 1) -> None: ...

def prange(start: int, end: int, step: int) -> Iterator[Tuple[int, int]]: ...
