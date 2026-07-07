from pyscf import lib as lib
from pyscf.pbc import df as df, dft as dft
from pyscf.pbc.tdscf import krhf as krhf

class TDA(krhf.TDA):
    def kernel(self, x0=None): ...
KTDA = TDA

class TDDFT(krhf.TDHF):
    def kernel(self, x0=None): ...
RPA = TDDFT
KTDDFT = TDDFT
