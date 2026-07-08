from pyscf.pbc.scf.hf import SCF
from typing import Optional, Tuple

def density_fit(mf: SCF, auxbasis: Optional[str]=None, mesh: Optional[Tuple[int, int, int]]=None, with_df: None=None) -> SCF: ...
