from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.pbc import scf as scf
from pyscf.pbc.gto.pseudo.ppnl_velgauge import get_gth_pp_nl_velgauge_commutator as get_gth_pp_nl_velgauge_commutator
from pyscf.tdscf import rhf as rhf

def get_ab(mf): ...
def transition_velocity_dipole(tdobj, xy=None): ...
def oscillator_strength(tdobj, e=None, xy=None, gauge: str = 'velocity', order: int = 0): ...

class TDBase(rhf.TDBase):
    cell: Incomplete
    def __init__(self, mf, frozen=None) -> None: ...
    def get_ab(self, mf=None): ...
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
    def gen_vind(self, mf=None): ...
CIS = TDA

class TDHF(TDBase):
    get_init_guess: Incomplete
    kernel: Incomplete
    gen_vind: Incomplete
RPA = TDHF
TDRHF = TDHF
