from pyscf.pbc import scf as scf
from pyscf.pbc.adc import kadc_rhf as kadc_rhf, kadc_rhf_ea as kadc_rhf_ea, kadc_rhf_ip as kadc_rhf_ip
from pyscf.pbc.adc.kadc_rhf import RADC
from pyscf.pbc.scf.khf import KRHF

def KRADC(mf: KRHF, frozen: None=None, mo_coeff: None=None, mo_occ: None=None) -> RADC: ...
