from _typeshed import Incomplete
from pyscf import gto as gto, mcdcft as mcdcft, mcscf as mcscf, prop as prop
from pyscf.lib import logger as logger
from pyscf.mcpdft.mcpdft import get_mcpdft_child_class as get_mcpdft_child_class
from pyscf.mcscf import casci as casci, mc1step as mc1step

def CASSCFPDFT(mc_or_mf_or_mol, ot, ncas, nelecas, ncore=None, frozen=None, **kwargs): ...
def CASCIPDFT(mc_or_mf_or_mol, ot, ncas, nelecas, ncore=None, **kwargs): ...
CASSCF = CASSCFPDFT
CASCI = CASCIPDFT

class MultiStateMCPDFTSolver: ...

mypath: Incomplete
myproppath: Incomplete
