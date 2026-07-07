from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto.moleintor import make_loc as make_loc

BLKSIZE: int
NBINS: int
CUTOFF: Incomplete
libcgto: Incomplete

def eval_gto(mol, eval_name, coords, comp=None, shls_slice=None, non0tab=None, ao_loc=None, cutoff=None, out=None): ...
def make_screen_index(mol, coords, shls_slice=None, cutoff=..., blksize=...): ...
