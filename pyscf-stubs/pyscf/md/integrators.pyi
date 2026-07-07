from _typeshed import Incomplete
from pyscf import data as data, lib as lib
from pyscf.grad.rhf import GradientsBase as GradientsBase
from pyscf.lib import logger as logger

class Frame:
    ekin: Incomplete
    epot: Incomplete
    etot: Incomplete
    coord: Incomplete
    veloc: Incomplete
    time: Incomplete
    def __init__(self, ekin=None, epot=None, coord=None, veloc=None, time=None) -> None: ...

def kernel(integrator, verbose=...): ...

class _Integrator(lib.StreamObject):
    scanner: Incomplete
    mol: Incomplete
    stdout: Incomplete
    incore_anyway: Incomplete
    veloc: Incomplete
    verbose: Incomplete
    steps: int
    dt: int
    frames: Incomplete
    epot: Incomplete
    ekin: Incomplete
    time: int
    data_output: Incomplete
    trajectory_output: Incomplete
    callback: Incomplete
    def __init__(self, method, **kwargs) -> None: ...
    def kernel(self, veloc=None, steps=None, dump_flags: bool = True, verbose=None): ...
    def dump_input(self, verbose=None) -> None: ...
    def check_sanity(self): ...
    def compute_kinetic_energy(self): ...
    def temperature(self): ...
    def __iter__(self): ...
    def __next__(self): ...

class VelocityVerlet(_Integrator):
    accel: Incomplete
    def __init__(self, method, **kwargs) -> None: ...

class NVTBerendson(_Integrator):
    T: Incomplete
    taut: Incomplete
    accel: Incomplete
    def __init__(self, method, T, taut, **kwargs) -> None: ...
