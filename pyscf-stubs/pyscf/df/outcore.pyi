from _typeshed import Incomplete
from pyscf import __config__ as __config__, ao2mo as ao2mo, gto as gto, lib as lib
from pyscf.df.addons import make_auxmol as make_auxmol
from pyscf.df.incore import LINEAR_DEP_THR as LINEAR_DEP_THR
from pyscf.lib import logger as logger

MAX_MEMORY: Incomplete

def cholesky_eri(mol, erifile, auxbasis: str = 'weigend+etb', dataname: str = 'j3c', tmpdir=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory=..., auxmol=None, verbose=...): ...
def cholesky_eri_b(mol, erifile, auxbasis: str = 'weigend+etb', dataname: str = 'j3c', int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory=..., auxmol=None, decompose_j2c: str = 'CD', lindep=..., verbose=...): ...
def general(mol, mo_coeffs, erifile, auxbasis: str = 'weigend+etb', dataname: str = 'eri_mo', tmpdir=None, int3c: str = 'int3c2e', aosym: str = 's2ij', int2c: str = 'int2c2e', comp: int = 1, max_memory=..., verbose: int = 0, compact: bool = True): ...
