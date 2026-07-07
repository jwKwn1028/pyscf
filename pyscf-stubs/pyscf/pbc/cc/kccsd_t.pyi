from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.lib.misc import tril_product as tril_product
from pyscf.lib.numpy_helper import cartesian_prod as cartesian_prod
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import scf as scf
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx

einsum = lib.einsum

def kernel(mycc, eris, t1=None, t2=None, max_memory: int = 2000, verbose=...): ...
