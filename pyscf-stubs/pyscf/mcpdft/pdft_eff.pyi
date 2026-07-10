from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.dft import numint as numint
from pyscf.lib import logger as logger
from io import TextIOWrapper
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcpdft.otfnal import ftransfnal, transfnal
from typing import List, Optional, Tuple, Union

SWITCH_SIZE: Incomplete
libpdft: Incomplete

class _ERIS:
    mol: Incomplete
    mo_coeff: Incomplete
    ncore: Incomplete
    ncas: Incomplete
    vhf_c: Incomplete
    method: Incomplete
    paaa_only: Incomplete
    aaaa_only: Incomplete
    jk_pc: Incomplete
    verbose: Incomplete
    stdout: Incomplete
    papa: Incomplete
    j_pc: Incomplete
    def __init__(self, mol: Mole, mo_coeff: Union[NPArrayWithTag, ndarray], ncore: int, ncas: int, method: str = 'incore', paaa_only: bool = False, aaaa_only: bool = False, jk_pc: bool = False, verbose: int = 0, stdout: Optional[TextIOWrapper]=None) -> None: ...

def get_eff_1body(otfnal: Union[transfnal, ftransfnal], ao: Union[ndarray, List[ndarray]], weight: ndarray, kern: ndarray, non0tab: None=None, shls_slice: Optional[Tuple[int, int]]=None, ao_loc: Optional[ndarray]=None, hermi: int = 0) -> ndarray: ...
def get_eff_2body(otfnal: Union[transfnal, ftransfnal], ao: Union[ndarray, List[ndarray]], weight: ndarray, kern: ndarray, aosym: Union[int, str] = 's4', eff_ao: None=None) -> ndarray: ...
def get_eff_2body_kl(ot: Union[transfnal, ftransfnal], ao_k: ndarray, ao_l: ndarray, weight: ndarray, kern: ndarray, symm: bool = False) -> ndarray: ...
