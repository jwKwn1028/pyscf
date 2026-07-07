from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib
from pyscf.tools import cubegen as cubegen

RESOLUTION: Incomplete
BOX_MARGIN: Incomplete

def density(cell, outfile, dm, nx: int = 60, ny: int = 60, nz: int = 60, resolution=...) -> None: ...
def orbital(cell, outfile, coeff, nx: int = 60, ny: int = 60, nz: int = 60, resolution=...) -> None: ...

class CHGCAR(cubegen.Cube):
    box: Incomplete
    mol: Incomplete
    nx: Incomplete
    ny: Incomplete
    nz: Incomplete
    cell: Incomplete
    boxorig: Incomplete
    vol: Incomplete
    def __init__(self, cell, nx: int = 60, ny: int = 60, nz: int = 60, resolution=..., margin=...) -> None: ...
    def get_coords(self): ...
    def write(self, field, fname, comment=None): ...
    def read(self, chgcar_file) -> None: ...
