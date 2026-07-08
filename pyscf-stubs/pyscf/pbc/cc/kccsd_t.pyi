from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.lib.misc import tril_product as tril_product
from pyscf.lib.numpy_helper import NPArrayWithTag, cartesian_prod as cartesian_prod
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import scf as scf
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from numpy import float64
from pyscf.cc.gccsd import _PhysicistsERIs
from pyscf.pbc.cc.kccsd import GCCSD
from typing import Optional

einsum = lib.einsum

def kernel(mycc: GCCSD, eris: _PhysicistsERIs, t1: Optional[NPArrayWithTag]=None, t2: Optional[NPArrayWithTag]=None, max_memory: int = 2000, verbose: int=...) -> float64: ...
