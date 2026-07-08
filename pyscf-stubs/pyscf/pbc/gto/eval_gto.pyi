from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import moleintor as moleintor
from pyscf.gto.eval_gto import BLKSIZE as BLKSIZE
from pyscf.gto.mole import ANG_OF as ANG_OF, extract_pgto_params as extract_pgto_params
from numpy import float64, ndarray
from pyscf.pbc.gto.cell import Cell
from typing import List, Optional, Tuple, Union

EXTRA_PREC: Incomplete
libpbc: Incomplete

def eval_gto(cell: Cell, eval_name: str, coords: ndarray, comp: Optional[int]=None, kpts: Optional[ndarray]=None, kpt: Optional[ndarray]=None, shls_slice: Optional[Tuple[int, int]]=None, non0tab: Optional[ndarray]=None, ao_loc: None=None, cutoff: Optional[float]=None, out: None=None, Ls: None=None, rcut: None=None) -> Union[ndarray, List[ndarray]]: ...
pbc_eval_gto = eval_gto

def get_lattice_Ls(cell: Cell, nimgs: None=None, rcut: Optional[float64]=None, dimension: Optional[int]=None, discard: bool = True) -> ndarray: ...
