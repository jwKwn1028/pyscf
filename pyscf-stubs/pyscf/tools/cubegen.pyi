from _typeshed import Incomplete
from pyscf import __config__ as __config__, df as df, gto as gto, lib as lib
from pyscf.dft import numint as numint
from numpy import int64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.gto.cell import Cell
from typing import Optional, Union

RESOLUTION: Incomplete
BOX_MARGIN: Incomplete
ORIGIN: Incomplete
EXTENT: Incomplete

def density(mol: Union[Cell, Mole], outfile: str, dm: NPArrayWithTag, nx: int = 80, ny: int = 80, nz: int = 80, resolution: Optional[float]=..., margin: float=...) -> ndarray: ...
def orbital(mol: Mole, outfile: str, coeff: ndarray, nx: int = 80, ny: int = 80, nz: int = 80, resolution: Optional[float]=..., margin: float=...) -> ndarray: ...
def mep(mol: Mole, outfile: str, dm: NPArrayWithTag, nx: int = 80, ny: int = 80, nz: int = 80, resolution: Optional[float]=..., margin: float=...) -> ndarray: ...

class Cube:
    mol: Incomplete
    box: Incomplete
    boxorig: Incomplete
    nx: Incomplete
    ny: Incomplete
    nz: Incomplete
    xs: Incomplete
    ys: Incomplete
    zs: Incomplete
    def __init__(self, mol: Union[Cell, Mole], nx: int = 80, ny: int = 80, nz: int = 80, resolution: Optional[float]=..., margin: float=..., origin: None=..., extent: None=...) -> None: ...
    def get_coords(self) -> ndarray: ...
    def get_ngrids(self) -> Union[int64, int]: ...
    def get_volume_element(self): ...
    def write(self, field: ndarray, fname: str, comment: Optional[str]=None) -> None: ...
    def read(self, cube_file: str) -> ndarray: ...
