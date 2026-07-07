from pyscf import gto as gto, lib as lib
from pyscf.lib import logger as logger

def get_jk(mols, dms, scripts=['ijkl,ji->kl'], intor: str = 'int2e_sph', aosym: str = 's1', comp=None, hermi: int = 0, shls_slice=None, verbose=..., vhfopt=None): ...
jk_build = get_jk
