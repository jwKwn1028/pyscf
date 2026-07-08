from numpy import int64, ndarray
from pyscf.pbc.adc.kadc_rhf import RADC
from pyscf.pbc.adc.kadc_rhf_ea import RADCEA
from pyscf.pbc.adc.kadc_rhf_ip import RADCIP
from typing import Union

def get_ovvv_df(myadc: Union[RADCEA, RADC, RADCIP], Lov: ndarray, Lvv: ndarray, p: int, chnk_size: int64) -> ndarray: ...
def get_vvvv_df(myadc: Union[RADCEA, RADC], vv1: ndarray, vv2: ndarray, p: int, chnk_size: Union[int64, int]) -> ndarray: ...
