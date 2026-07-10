from pyscf import scf as scf
from pyscf.dft import KohnShamDFT as KohnShamDFT
from pyscf.tdscf import dhf as dhf, dks as dks, ghf as ghf, gks as gks, rhf as rhf, rks as rks, uhf as uhf, uks as uks
from pyscf.tdscf.ghf import TDGHF as TDGHF
from pyscf.tdscf.gks import TDGKS as TDGKS
from pyscf.tdscf.rhf import TDBase, TDRHF as TDRHF
from pyscf.tdscf.rks import TDRKS as TDRKS
from pyscf.tdscf.uhf import TDUHF as TDUHF
from pyscf.tdscf.uks import TDUKS as TDUKS
from _typeshed import Incomplete
from pyscf.dft.rks import RKS
from pyscf.dft.uks import UKS
from pyscf.scf.hf import RHF
from pyscf.scf.uhf import UHF
from pyscf.scf.uhf_symm import SymAdaptedUHF
from typing import Union

def TDHF(mf: Union[RHF, UHF], frozen: None=None) -> Union[Incomplete, Incomplete]: ...
def TDA(mf: Union[UKS, SymAdaptedUHF, RKS, UHF, RHF], frozen: None=None) -> Union[Incomplete, Incomplete, Incomplete, Incomplete]: ...
def TDDFT(mf: Union[RHF, UHF, UKS, RKS], frozen: None=None) -> TDBase: ...
TD = TDDFT

def RPA(mf: Union[RHF, UHF, UKS, RKS], frozen: None=None) -> TDBase: ...
def dRPA(mf: Union[UKS, RKS], frozen: None=None) -> Union[Incomplete, Incomplete]: ...
def dTDA(mf: Union[UKS, RKS], frozen: None=None) -> Union[Incomplete, Incomplete]: ...
