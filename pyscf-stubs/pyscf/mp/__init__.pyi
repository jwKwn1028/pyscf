from pyscf import scf as scf
from pyscf.mp import dfgmp2 as dfgmp2, dfmp2 as dfmp2, dfump2 as dfump2, gmp2 as gmp2, mp2 as mp2, ump2 as ump2
from _typeshed import Incomplete
from numpy import ndarray
from pyscf.mp.mp2 import RMP2
from pyscf.mp.ump2 import UMP2
from pyscf.scf.ghf import GHF
from pyscf.scf.hf import RHF
from pyscf.scf.rohf import HF1e
from pyscf.scf.uhf import UHF
from typing import List, Optional, Union

def MP2(mf: Union[RHF, GHF, UHF, HF1e], frozen: Optional[Union[ndarray, List[ndarray], int]]=None, mo_coeff: Optional[Union[ndarray, List[ndarray]]]=None, mo_occ: None=None) -> Union[RMP2, UMP2, Incomplete]: ...
def RMP2(mf: Union[RHF, HF1e], frozen: Optional[Union[int, ndarray]]=None, mo_coeff: Optional[ndarray]=None, mo_occ: None=None) -> Union[RMP2, UMP2]: ...
def UMP2(mf: Union[UHF, HF1e], frozen: Optional[Union[int, List[ndarray]]]=None, mo_coeff: Optional[List[ndarray]]=None, mo_occ: None=None) -> UMP2: ...
def GMP2(mf: Union[GHF, UHF], frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> Incomplete: ...
