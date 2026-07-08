from pyscf import gto as gto, lib as lib
from pyscf.gto.moleintor import libcgto as libcgto
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Tuple, Union

def ft_aopair(mol: Mole, Gv: ndarray, shls_slice: Optional[Tuple[int, int, int, int]]=None, aosym: str = 's1', b: ndarray=..., gxyz: Optional[ndarray]=None, Gvbase: Optional[Tuple[ndarray, ndarray, ndarray]]=None, out: None=None, intor: str = 'GTO_ft_ovlp', comp: int = 1, q: ndarray=..., return_complex: bool = True, ovlp_mask: None=None, verbose: None=None) -> ndarray: ...
def ft_ao(mol: Union[Mole, Cell], Gv: ndarray, shls_slice: None=None, b: Optional[ndarray]=..., gxyz: Optional[ndarray]=None, Gvbase: Optional[Tuple[ndarray, ndarray, ndarray]]=None, verbose: None=None) -> ndarray: ...
