from _typeshed import Incomplete
from pyscf import data as data, lib as lib
from pyscf.grad.rhf import GradientsBase as GradientsBase
from pyscf.lib import logger as logger
from numpy import float64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.mcscf.mc1step import CASSCF
from pyscf.scf.hf import RHF
from typing import Optional, Tuple, Union

class Frame:
    ekin: Incomplete
    epot: Incomplete
    etot: Incomplete
    coord: Incomplete
    veloc: Incomplete
    time: Incomplete
    def __init__(self, ekin: Optional[float64]=None, epot: Optional[float64]=None, coord: Optional[ndarray]=None, veloc: Optional[ndarray]=None, time: Optional[int]=None) -> None: ...

def kernel(integrator: Union[NVTBerendson, VelocityVerlet], verbose: Logger=...) -> Union[NVTBerendson, VelocityVerlet]: ...

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
    def __init__(self, method: Union[CASSCF, RHF], **kwargs) -> None: ...
    def kernel(self, veloc: None=None, steps: None=None, dump_flags: bool = True, verbose: None=None) -> Union[NVTBerendson, VelocityVerlet]: ...
    def dump_input(self, verbose=None) -> None: ...
    def check_sanity(self) -> Union[NVTBerendson, VelocityVerlet]: ...
    def compute_kinetic_energy(self) -> float64: ...
    def temperature(self) -> float64: ...
    def __iter__(self) -> Union[NVTBerendson, VelocityVerlet]: ...
    def __next__(self) -> Frame: ...

class VelocityVerlet(_Integrator):
    accel: Incomplete
    def __init__(self, method: Union[CASSCF, RHF], **kwargs) -> None: ...

class NVTBerendson(_Integrator):
    T: Incomplete
    taut: Incomplete
    accel: Incomplete
    def __init__(self, method: RHF, T: int, taut: int, **kwargs) -> None: ...
