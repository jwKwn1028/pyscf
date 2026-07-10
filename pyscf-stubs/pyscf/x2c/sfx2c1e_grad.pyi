from pyscf import gto as gto, lib as lib
from pyscf.x2c import x2c as x2c
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.x2c.sfx2c1e import SpinFreeX2CHelper
from typing import Callable, Tuple

def hcore_grad_generator(x2cobj: SpinFreeX2CHelper, mol: None=None) -> Callable: ...
def gen_sf_hfw(mol: Mole, approx: str = '1E') -> Callable: ...
