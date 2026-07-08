from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.scf.smearing import SMEARING_METHOD as SMEARING_METHOD, smearing as smearing, smearing_ as smearing_
from pyscf.pbc.tools import k2gamma as k2gamma
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.dft.krks import KRKS
from pyscf.pbc.dft.kuks_ksymm import KsymAdaptedKUKS
from pyscf.pbc.dft.rks import RKS
from pyscf.pbc.gto.cell import Cell
from pyscf.pbc.scf.ghf import GHF
from pyscf.pbc.scf.hf import RHF, SCF
from pyscf.pbc.scf.kghf import KGHF
from pyscf.pbc.scf.khf import KRHF
from pyscf.pbc.scf.krohf import KROHF
from pyscf.pbc.scf.kuhf import KUHF
from pyscf.pbc.scf.kuhf_ksymm import KsymAdaptedKUHF
from pyscf.pbc.scf.rohf import ROHF
from pyscf.pbc.scf.uhf import UHF
from typing import Any, List, Optional, Union

def project_mo_nr2nr(cell1: Cell, mo1: ndarray, cell2: Cell, kpts: Optional[ndarray]=None) -> Union[ndarray, List[ndarray]]: ...
def project_dm_k2k(cell: Cell, dm: NPArrayWithTag, kpts1: ndarray, kpts2: ndarray) -> ndarray: ...
def canonical_occ_(mf: KUHF, nelec: None=None) -> KUHF: ...
canonical_occ = canonical_occ_

def convert_to_uhf(mf: SCF, out: Optional[Union[KUHF, KsymAdaptedKUKS, UHF, KsymAdaptedKUHF]]=None) -> SCF: ...
def convert_to_rhf(mf: SCF, out: Optional[Any]=None) -> SCF: ...
def convert_to_ghf(mf: SCF, out: Optional[Union[GHF, KGHF]]=None) -> Union[GHF, KGHF]: ...
def convert_to_kscf(mf: Union[RHF, GHF, ROHF, UHF, RKS], out: None=None) -> Union[KUHF, KROHF, KGHF, KRHF, KRKS]: ...
convert_to_khf = convert_to_kscf

def mo_energy_with_exxdiv_none(mf: SCF, mo_coeff: None=None) -> Union[ndarray, List[List[ndarray]], List[ndarray]]: ...
