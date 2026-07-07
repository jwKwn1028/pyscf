from pyscf import scf as scf
from pyscf.gw import gw_ac as gw_ac, gw_cd as gw_cd, gw_exact as gw_exact, ugw_ac as ugw_ac

def GW(mf, freq_int: str = 'ac', frozen=None, tdmf=None): ...
