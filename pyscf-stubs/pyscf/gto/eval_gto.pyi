from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto.moleintor import make_loc as make_loc
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Tuple, Union

BLKSIZE: int
NBINS: int
CUTOFF: Incomplete
libcgto: Incomplete

def eval_gto(mol: Mole, eval_name: str, coords: ndarray, comp: Optional[int]=None, shls_slice: None=None, non0tab: Optional[ndarray]=None, ao_loc: None=None, cutoff: Optional[float]=None, out: Optional[ndarray]=None) -> ndarray: ...
def make_screen_index(mol: Mole, coords: ndarray, shls_slice: None=None, cutoff: float=..., blksize: int=...) -> ndarray: ...
