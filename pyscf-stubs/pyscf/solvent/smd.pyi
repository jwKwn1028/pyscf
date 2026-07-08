from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib, scf as scf
from pyscf.data import radii as radii
from pyscf.dft.gen_grid import LEBEDEV_ORDER as LEBEDEV_ORDER
from pyscf.lib import load_library as load_library, logger as logger
from pyscf.solvent import pcm as pcm
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from typing import Optional, Tuple, Union

def smd_for_scf(mf, solvent_obj=None, dm=None): ...

hartree2kcal: float
solvent_db: Incomplete

def smd_radii(alpha: float) -> ndarray: ...

libsolvent: Incomplete

def get_cds_legacy(smdobj: "SMD") -> Tuple[float, ndarray]: ...

class SMD(pcm.PCM):
    mol: Incomplete
    stdout: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    vdw_scale: float
    sasa_ng: int
    method: str
    solvent: Incomplete
    solvent_descriptors: Incomplete
    radii_table: Incomplete
    eps: Incomplete
    surface_discretization_method: str
    max_cycle: int
    conv_tol: float
    state_id: int
    frozen: bool
    frozen_dm0_for_finite_difference_without_response: Incomplete
    equilibrium_solvation: bool
    surface: Incomplete
    e: Incomplete
    v: Incomplete
    v_grids_n: Incomplete
    e_cds: Incomplete
    def __init__(self, mol: Mole, solvent: str = '') -> None: ...
    def build(self, ng: None=None) -> "SMD": ...
    @property
    def sol_desc(self): ...
    @sol_desc.setter
    def sol_desc(self, values) -> None: ...
    @property
    def lebedev_order(self): ...
    @lebedev_order.setter
    def lebedev_order(self, x) -> None: ...
    def dump_flags(self, verbose: None=None) -> "SMD": ...
    def get_cds(self) -> float: ...
    def nuc_grad_method(self, grad_method) -> None: ...
    def grad(self, dm: Union[ndarray, NPArrayWithTag], verbose: None=None) -> ndarray: ...
    def Hessian(self, hess_method) -> None: ...
    def hess(self, dm: NPArrayWithTag) -> ndarray: ...
    def reset(self, mol: Optional[Mole]=None) -> "SMD": ...
