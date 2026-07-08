from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.cc import ccsd as ccsd
from pyscf.lib import logger as logger
from h5py._hl.dataset import Dataset
from numpy import ndarray
from pyscf.cc.ccd import CCD
from pyscf.cc.ccsd import CCSD
from pyscf.cc.rccsd import RCCSD
from pyscf.lib.misc import H5TmpFile
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mp.dfmp2 import DFRMP2
from pyscf.mp.mp2 import RMP2
from typing import Tuple, Union

def make_rdm1(mycc: Union[RCCSD, CCD, CCSD], t1: ndarray, t2: ndarray, l1: ndarray, l2: ndarray, ao_repr: bool = False, with_frozen: bool = True, with_mf: bool = True) -> ndarray: ...
def make_rdm2(mycc: Union[RCCSD, CCD, CCSD], t1: ndarray, t2: ndarray, l1: ndarray, l2: ndarray, ao_repr: bool = False, with_frozen: bool = True, with_dm1: bool = True) -> ndarray: ...
