import pyscf.adc.radc
from _typeshed import Incomplete
from itertools import product as product
from pyscf import __config__ as __config__, lib as lib
from pyscf.adc import radc_ao2mo as radc_ao2mo
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import df as df, mp as mp, scf as scf
from pyscf.pbc.adc import dfadc as dfadc, kadc_ao2mo as kadc_ao2mo, kadc_rhf_amplitudes as kadc_rhf_amplitudes
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx

def kernel(adc, nroots: int = 1, guess=None, eris=None, kptlist=None, verbose=None): ...

class RADC(pyscf.adc.radc.RADC):
    kpts: Incomplete
    exxdiv: Incomplete
    verbose: Incomplete
    max_memory: Incomplete
    method: str
    method_type: str
    max_space: Incomplete
    max_cycle: Incomplete
    conv_tol: Incomplete
    tol_residual: Incomplete
    scf_energy: Incomplete
    khelper: Incomplete
    cell: Incomplete
    mo_coeff: Incomplete
    mo_occ: Incomplete
    frozen: Incomplete
    compute_properties: bool
    approx_trans_moments: bool
    nkop_chk: bool
    kop_npick: bool
    t1: Incomplete
    t2: Incomplete
    e_corr: Incomplete
    chnk_size: Incomplete
    imds: Incomplete
    keep_exxdiv: bool
    mo_energy: Incomplete
    def __init__(self, mf, frozen=None, mo_coeff=None, mo_occ=None) -> None: ...
    transform_integrals = kadc_ao2mo.transform_integrals_incore
    compute_amplitudes = kadc_rhf_amplitudes.compute_amplitudes
    compute_energy = kadc_rhf_amplitudes.compute_energy
    compute_amplitudes_energy = kadc_rhf_amplitudes.compute_amplitudes_energy
    get_chnk_size = kadc_ao2mo.calculate_chunk_size
    @property
    def nkpts(self): ...
    @property
    def nocc(self): ...
    @property
    def nmo(self): ...
    get_nocc = get_nocc
    get_nmo = get_nmo
    with_df: Incomplete
    def kernel_gs(self): ...
    def kernel(self, nroots: int = 1, guess=None, eris=None, kptlist=None): ...
    def ip_adc(self, nroots: int = 1, guess=None, eris=None, kptlist=None): ...
    def ea_adc(self, nroots: int = 1, guess=None, eris=None, kptlist=None): ...
    def density_fit(self, auxbasis=None, with_df=None): ...
