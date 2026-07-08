from pyscf import __config__ as __config__, lib as lib
from pyscf.lib import logger as logger
from numpy import float64, int64, ndarray
from pyscf.agf2.aux_space import SelfEnergy
from scipy.optimize._optimize import OptimizeResult
from typing import Optional, Tuple, Union

def binsearch_chempot(fock: Union[ndarray, Tuple[ndarray, ndarray]], nphys: int, nelec: int64, occupancy: int = 2) -> Tuple[float64, float64]: ...
def minimize_chempot(se: SelfEnergy, fock: ndarray, nelec: int64, occupancy: int = 2, x0: float64 = 0.0, tol: float = 1e-06, maxiter: int = 200, jac: bool = True) -> Tuple[SelfEnergy, OptimizeResult]: ...
