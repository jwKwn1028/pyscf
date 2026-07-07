import geometric
from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.geomopt.addons import dump_mol_geometry as dump_mol_geometry
from pyscf.pbc.grad.krhf import GradientsBase as GradientsBase

msg: str
INCLUDE_GHOST: Incomplete
ASSERT_CONV: Incomplete

class PySCFEngine(geometric.engine.Engine):
    cell: Incomplete
    scanner: Incomplete
    cycle: int
    e_last: int
    callback: Incomplete
    maxsteps: int
    assert_convergence: bool
    def __init__(self, scanner) -> None: ...
    def calc_new(self, coords, dirname): ...

def kernel(method, assert_convergence=..., include_ghost=..., constraints=None, callback=None, maxsteps: int = 100, **kwargs): ...

class GeometryOptimizer(lib.StreamObject):
    method: Incomplete
    callback: Incomplete
    params: Incomplete
    converged: bool
    max_cycle: int
    def __init__(self, method) -> None: ...
    @property
    def cell(self): ...
    @cell.setter
    def cell(self, x) -> None: ...
    def kernel(self, params=None): ...
    optimize = kernel

class NotConvergedError(RuntimeError): ...
