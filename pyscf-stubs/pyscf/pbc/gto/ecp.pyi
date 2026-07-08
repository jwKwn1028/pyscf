from functools import reduce as reduce
from pyscf import gto as gto, lib as lib
from pyscf.pbc.df import incore as incore
from numpy import ndarray
from pyscf.pbc.gto.cell import Cell
from typing import List, Optional, Union

def ecp_int(cell: Cell, kpts: Optional[Union[List[ndarray], ndarray]]=None, intor: str = 'ECPscalar') -> Union[ndarray, List[ndarray]]: ...
