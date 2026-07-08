from pyscf import lib as lib
from pyscf.pbc import dft as dft
from pyscf.pbc.tdscf import kuhf as kuhf

class TDA(kuhf.TDA):
    def kernel(self, x0: None=None) -> None: ...
KTDA = TDA

class TDDFT(kuhf.TDHF):
    def kernel(self, x0: None=None) -> None: ...
RPA = TDDFT
KTDDFT = TDDFT
