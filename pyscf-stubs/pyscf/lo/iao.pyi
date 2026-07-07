from _typeshed import Incomplete
from pyscf import __config__ as __config__, gto as gto, scf as scf
from pyscf.data.elements import is_ghost_atom as is_ghost_atom
from pyscf.lib import logger as logger
from pyscf.lo.orth import vec_lowdin as vec_lowdin

MINAO: Incomplete

def iao(mol, orbocc, minao=..., kpts=None, lindep_threshold: float = 1e-08): ...
def reference_mol(mol, minao=...): ...
def fast_iao_mullikan_pop(mol, dm, iaos, verbose=...): ...
