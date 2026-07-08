from pyscf import lib as lib
from pyscf.pbc import df as df, dft as dft
from pyscf.pbc.tdscf import krhf as krhf
from numpy import ndarray
from pyscf.pbc.tdscf.kuks import TDA, TDDFT
from typing import List, Tuple, Union

class TDA(krhf.TDA):
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[List[ndarray], int]]]]: ...
KTDA = TDA

class TDDFT(krhf.TDHF):
    def kernel(self, x0: None=None) -> Tuple[List[ndarray], List[List[Tuple[List[ndarray], List[ndarray]]]]]: ...
RPA = TDDFT
KTDDFT = TDDFT
