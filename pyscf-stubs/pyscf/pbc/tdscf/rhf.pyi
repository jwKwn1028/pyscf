from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc import scf as scf
from pyscf.pbc.gto.pseudo.ppnl_velgauge import get_gth_pp_nl_velgauge_commutator as get_gth_pp_nl_velgauge_commutator
from pyscf.tdscf import rhf as rhf
from numpy import ndarray
from pyscf.pbc.dft.rks import RKS
from pyscf.pbc.dft.uks import UKS
from pyscf.pbc.scf.hf import RHF, SCF
from pyscf.pbc.scf.uhf import UHF
from typing import Callable, Optional, Tuple, Union

def get_ab(mf: Union[RHF, RKS]) -> Tuple[ndarray, ndarray]: ...
def transition_velocity_dipole(tdobj: Union[TDHF, TDA], xy: None=None) -> ndarray: ...
def oscillator_strength(tdobj: Union[TDHF, TDA], e: None=None, xy: None=None, gauge: str = 'velocity', order: int = 0) -> ndarray: ...

class TDBase(rhf.TDBase):
    cell: Incomplete
    def __init__(self, mf: SCF, frozen: None=None) -> None: ...
    def get_ab(self, mf: None=None) -> Tuple[ndarray, ndarray]: ...
    def nuc_grad_method(self) -> None: ...
    get_nto: Incomplete
    transition_velocity_dipole = transition_velocity_dipole
    oscillator_strength = oscillator_strength
    analyze: Incomplete
    transition_dipole: Incomplete
    transition_quadrupole: Incomplete
    transition_octupole: Incomplete
    transition_velocity_quadrupole: Incomplete
    transition_velocity_octupole: Incomplete
    transition_magnetic_dipole: Incomplete
    transition_magnetic_quadrupole: Incomplete
    photoabsorption_cross_section: Incomplete

class TDA(TDBase):
    get_init_guess: Incomplete
    kernel: Incomplete
    def gen_vind(self, mf: Optional[Union[RHF, UKS, RKS, UHF]]=None) -> Tuple[Callable, ndarray]: ...
CIS = TDA

class TDHF(TDBase):
    get_init_guess: Incomplete
    kernel: Incomplete
    gen_vind: Incomplete
RPA = TDHF
TDRHF = TDHF
