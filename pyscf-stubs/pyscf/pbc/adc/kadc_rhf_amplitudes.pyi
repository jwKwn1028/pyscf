from itertools import product as product
from pyscf import __config__ as __config__, lib as lib
from pyscf.adc import radc_ao2mo as radc_ao2mo
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import df as df, mp as mp, scf as scf, tools as tools
from pyscf.pbc.adc import dfadc as dfadc, kadc_ao2mo as kadc_ao2mo
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx

def compute_amplitudes_energy(myadc, eris, verbose=None): ...
def compute_amplitudes(myadc, eris): ...
def compute_energy(myadc, t2, eris): ...
def contract_ladder(myadc, t_amp, vvvv, ka, kb, kc): ...
