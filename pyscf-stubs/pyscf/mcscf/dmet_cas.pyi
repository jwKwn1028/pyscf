from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, scf as scf
from pyscf.lib import logger as logger
from pyscf.tools import dump_mat as dump_mat

THRESHOLD: Incomplete
OCC_CUTOFF: Incomplete
BASE: Incomplete
ORTH_METHOD: Incomplete
CANONICALIZE: Incomplete
FREEZE_IMP: Incomplete

def kernel(mf, dm, aolabels_or_baslst, threshold=..., occ_cutoff=..., base=..., orth_method=..., s=None, canonicalize=..., freeze_imp=..., verbose=None): ...
dmet_cas = kernel
guess_cas = kernel

def search_for_degeneracy(e): ...
def symmetrize(mol, e, c, s, log): ...
