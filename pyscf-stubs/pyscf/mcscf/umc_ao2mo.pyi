from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcscf.umc1step import UCASSCF
from typing import Callable, Optional, Tuple, Union

libmcscf: Incomplete

def trans_e1_incore(eri_ao: ndarray, mo: Union[ndarray, Tuple[NPArrayWithTag, NPArrayWithTag], Tuple[ndarray, ndarray]], ncore: Tuple[int, int], ncas: int) -> Tuple[ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray]: ...
def trans_e1_outcore(mol: Mole, mo: ndarray, ncore: Tuple[int, int], ncas: int, max_memory: Optional[float]=None, ioblk_size: int = 512, verbose: Logger=...) -> Tuple[ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray, ndarray]: ...

class _ERIS:
    vhf_c: Incomplete
    def __init__(self, casscf: UCASSCF, mo: Union[ndarray, Tuple[NPArrayWithTag, NPArrayWithTag], Tuple[ndarray, ndarray]], method: str = 'incore') -> None: ...
