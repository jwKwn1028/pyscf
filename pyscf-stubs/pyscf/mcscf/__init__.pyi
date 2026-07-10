from pyscf.mcscf.addons import *
from pyscf.mcscf import addons as addons, casci as casci, casci_symm as casci_symm, chkfile as chkfile, df as df, mc1step as mc1step, mc1step_symm as mc1step_symm, ucasci as ucasci, umc1step as umc1step
from _typeshed import Incomplete
from pyscf.dft.rks import RKS
from pyscf.dft.roks import ROKS
from pyscf.gto.mole import Mole
from pyscf.lib.misc import StreamObject
from pyscf.mcscf.casci import CASCI
from pyscf.mcscf.casci_symm import SymAdaptedCASCI
from pyscf.mcscf.mc1step_symm import SymAdaptedCASSCF
from pyscf.mcscf.ucasci import UCASCI
from pyscf.mcscf.umc1step import UCASSCF
from pyscf.scf.hf import RHF
from pyscf.scf.hf_symm import SymAdaptedRHF
from pyscf.scf.uhf import UHF
from pyscf.scf.uhf_symm import SymAdaptedUHF
from typing import Optional, Tuple, Union

casci_uhf = ucasci
mc1step_uhf = umc1step

def CASSCF(mf_or_mol: StreamObject, ncas: int, nelecas: Union[int, Tuple[int, int]], ncore: Optional[int]=None, frozen: None=None) -> Union[Incomplete, SymAdaptedCASSCF]: ...
RCASSCF = CASSCF

def CASCI(mf_or_mol: Union[RHF, Mole, SymAdaptedRHF, RKS, UHF], ncas: int, nelecas: Union[int, Tuple[int, int]], ncore: Optional[int]=None) -> Union[SymAdaptedCASCI, CASCI]: ...
RCASCI = CASCI

def UCASCI(mf_or_mol: Union[SymAdaptedRHF, UHF, ROKS, SymAdaptedUHF], ncas: int, nelecas: Tuple[int, int], ncore: Optional[Tuple[int, int]]=None) -> UCASCI: ...
def UCASSCF(mf_or_mol: Union[UHF, SymAdaptedRHF, SymAdaptedUHF], ncas: int, nelecas: Union[int, Tuple[int, int]], ncore: None=None, frozen: None=None) -> UCASSCF: ...
def newton(mc: Union[Incomplete, SymAdaptedCASSCF]) -> Union[Incomplete, Incomplete]: ...
def DFCASSCF(mf_or_mol, ncas, nelecas, auxbasis=None, ncore=None, frozen=None): ...
def DFCASCI(mf_or_mol, ncas, nelecas, auxbasis=None, ncore=None): ...
approx_hessian = df.approx_hessian

def density_fit(mc, auxbasis=None, with_df=None): ...
