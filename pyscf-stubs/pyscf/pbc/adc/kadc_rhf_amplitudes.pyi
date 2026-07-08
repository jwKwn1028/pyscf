from itertools import product as product
from pyscf import __config__ as __config__, lib as lib
from pyscf.adc import radc_ao2mo as radc_ao2mo
from pyscf.lib import logger as logger
from pyscf.lib.parameters import LARGE_DENOM as LARGE_DENOM, LOOSE_ZERO_TOL as LOOSE_ZERO_TOL
from pyscf.pbc import df as df, mp as mp, scf as scf, tools as tools
from pyscf.pbc.adc import dfadc as dfadc, kadc_ao2mo as kadc_ao2mo
from pyscf.pbc.lib import kpts_helper as kpts_helper
from pyscf.pbc.mp.kmp2 import get_frozen_mask as get_frozen_mask, get_nmo as get_nmo, get_nocc as get_nocc, padded_mo_coeff as padded_mo_coeff, padding_k_idx as padding_k_idx
from h5py._hl.dataset import Dataset
from numpy import float64, ndarray
from pyscf.pbc.adc.kadc_rhf import RADC
from typing import Callable, Optional, Tuple, Union

def compute_amplitudes_energy(myadc: RADC, eris: Callable, verbose: Optional[int]=None) -> Union[Tuple[float64, Tuple[None, None], Tuple[Dataset, None]], Tuple[float64, Tuple[ndarray, None], Tuple[Dataset, ndarray]]]: ...
def compute_amplitudes(myadc: RADC, eris: Callable) -> Union[Tuple[Tuple[None, None], Tuple[Dataset, None], None], Tuple[Tuple[ndarray, None], Tuple[Dataset, ndarray], Dataset]]: ...
def compute_energy(myadc: RADC, t2: Union[Tuple[Dataset, None], Tuple[Dataset, ndarray]], eris: Callable) -> float64: ...
def contract_ladder(myadc: RADC, t_amp: ndarray, vvvv: ndarray, ka: int, kb: int, kc: int) -> ndarray: ...
