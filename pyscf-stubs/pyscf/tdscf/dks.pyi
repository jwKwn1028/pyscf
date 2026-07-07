from pyscf import dft as dft, lib as lib
from pyscf.tdscf import dhf as dhf

class TDA(dhf.TDA): ...
class TDDFT(dhf.TDHF): ...
RPA = TDDFT
TDDKS = TDDFT
