from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import mole as mole
from numpy import ndarray
from pyscf.pbc.df.ft_ao import _RangeSeparatedCell
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.symm.space_group import SPGElement
from typing import List, Tuple, Union

SYMPREC: Incomplete

def search_point_group_ops(cell: Union[Cell, _RangeSeparatedCell], tol: float=...) -> ndarray: ...
def search_space_group_ops(cell: Union[Cell, _RangeSeparatedCell], rotations: None=None, tol: float=...) -> List[SPGElement]: ...
def get_crystal_class(cell: Union[Cell, _RangeSeparatedCell], ops: None=None, tol: float=...) -> Tuple[str, str]: ...
