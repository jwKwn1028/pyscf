from pyscf.pbc import scf as scf
from pyscf.pbc.adc import kadc_rhf as kadc_rhf, kadc_rhf_ea as kadc_rhf_ea, kadc_rhf_ip as kadc_rhf_ip

def KRADC(mf, frozen=None, mo_coeff=None, mo_occ=None): ...
