from pyscf import lib as lib, scf as scf
from pyscf.agf2 import aux_space as aux_space, dfragf2 as dfragf2, dfuagf2 as dfuagf2, ragf2 as ragf2, ragf2_slow as ragf2_slow, uagf2 as uagf2, uagf2_slow as uagf2_slow
from pyscf.agf2.aux_space import AuxiliarySpace as AuxiliarySpace, GreensFunction as GreensFunction, SelfEnergy as SelfEnergy
from _typeshed import Incomplete
from pyscf.agf2.uagf2 import UAGF2
from pyscf.scf.hf import RHF
from pyscf.scf.uhf import UHF
from typing import Tuple, Union

aux = aux_space

def AGF2(mf, nmom=(None, 0), frozen=None, mo_energy=None, mo_coeff=None, mo_occ=None): ...
def RAGF2(mf: RHF, nmom: Union[Tuple[int, int], Tuple[None, int]]=(None, 0), frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> Union[Incomplete, Incomplete]: ...
def UAGF2(mf: UHF, nmom: Tuple[None, int]=(None, 0), frozen: None=None, mo_energy: None=None, mo_coeff: None=None, mo_occ: None=None) -> UAGF2: ...
