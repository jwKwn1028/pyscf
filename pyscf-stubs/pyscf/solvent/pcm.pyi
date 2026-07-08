from _typeshed import Incomplete
from pyscf import cc as cc, ci as ci, df as df, gto as gto, lib as lib, mcscf as mcscf, mp as mp, scf as scf, tdscf as tdscf
from pyscf.data import radii as radii
from pyscf.dft import gen_grid as gen_grid
from pyscf.lib import logger as logger
from pyscf.solvent import ddcosmo as ddcosmo
from numpy import float64, int64, ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.logger import Logger
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.solvent.smd import SMD
from typing import Dict, List, Optional, Tuple, Union

def pcm_for_scf(mf, solvent_obj=None, dm=None): ...
def pcm_for_casscf(mc, solvent_obj=None, dm=None): ...
def pcm_for_casci(mc, solvent_obj=None, dm=None): ...
def pcm_for_post_scf(method, solvent_obj=None, dm=None): ...

pcm_for_tdscf: Incomplete
XI: Incomplete
modified_Bondi: Incomplete
PI: Incomplete

def switch_h(x: ndarray) -> ndarray: ...
def gen_surface(mol: Mole, ng: int = 302, rad: ndarray=..., surface_discretization_method: str = 'SWIG') -> Dict[str, Union[int, List[List[Union[int, int64]]], ndarray]]: ...
def get_F_A(surface: Dict[str, Union[int, List[List[Union[int, int64]]], ndarray]]) -> Tuple[ndarray, ndarray]: ...
def get_D_S(surface: Dict[str, Union[int, List[List[Union[int, int64]]], ndarray]], with_S: bool = True, with_D: bool = False) -> Tuple[ndarray, ndarray]: ...

class PCM(lib.StreamObject):
    kernel: Incomplete
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    method: str
    vdw_scale: float
    r_probe: float
    radii_table: Incomplete
    lebedev_order: int
    eps: float
    surface_discretization_method: str
    max_cycle: int
    conv_tol: float
    state_id: int
    frozen: bool
    equilibrium_solvation: bool
    surface: Incomplete
    v_grids_n: Incomplete
    e: Incomplete
    v: Incomplete
    def __init__(self, mol: Mole) -> None: ...
    def dump_flags(self, verbose: Optional[Logger]=None) -> "PCM": ...
    def to_gpu(self): ...
    def reset(self, mol: Optional[Mole]=None) -> Union[SMD, PCM]: ...
    def build(self, ng: None=None) -> None: ...
    def nuc_grad_method(self, grad_method) -> None: ...
    def grad(self, dm: Union[ndarray, NPArrayWithTag]) -> ndarray: ...
    def Hessian(self, hess_method) -> None: ...
    def hess(self, dm: Union[ndarray, NPArrayWithTag]) -> ndarray: ...
