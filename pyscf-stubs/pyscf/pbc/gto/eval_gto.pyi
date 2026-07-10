from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib
from pyscf.gto import moleintor as moleintor
from pyscf.gto.eval_gto import BLKSIZE as BLKSIZE
from pyscf.gto.mole import ANG_OF as ANG_OF, extract_pgto_params as extract_pgto_params

EXTRA_PREC: Incomplete
libpbc: Incomplete

def eval_gto(cell, eval_name, coords, comp=None, kpts=None, kpt=None, shls_slice=None, non0tab=None, ao_loc=None, cutoff=None, out=None, Ls=None, rcut=None): ...
pbc_eval_gto = eval_gto

def get_lattice_Ls(cell, nimgs=None, rcut=None, dimension=None, discard: bool = True): ...
