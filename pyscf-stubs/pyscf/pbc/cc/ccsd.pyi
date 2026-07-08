from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.cc import gccsd as gccsd, rccsd as rccsd, uccsd as uccsd
from pyscf.pbc import mp as mp, scf as scf
from numpy import float64, int64, ndarray
from typing import Optional, Tuple, Union

class RCCSD(rccsd.RCCSD):
    t1: Incomplete
    def ccsd(self, t1: None=None, t2: None=None, eris: Optional[Incomplete]=None, mbpt2: bool = False) -> Tuple[float64, ndarray, ndarray]: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> Incomplete: ...

class UCCSD(uccsd.UCCSD):
    t1: Incomplete
    def ccsd(self, t1: None=None, t2: None=None, eris: None=None, mbpt2: bool = False) -> Tuple[float64, Tuple[ndarray, ndarray], Tuple[ndarray, ndarray, ndarray]]: ...
    def ao2mo(self, mo_coeff: Optional[ndarray]=None) -> Incomplete: ...

class GCCSD(gccsd.GCCSD):
    t1: Incomplete
    def ccsd(self, t1=None, t2=None, eris=None, mbpt2: bool = False): ...
    def ao2mo(self, mo_coeff=None): ...
