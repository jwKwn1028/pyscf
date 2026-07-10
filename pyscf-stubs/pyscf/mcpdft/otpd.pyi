from pyscf.lib import logger as logger
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcpdft.otfnal import ftransfnal, transfnal
from typing import Tuple, Union

def get_ontop_pair_density(ot: Union[ftransfnal, transfnal], rho: ndarray, ao: ndarray, cascm2: ndarray, mo_cas: Union[ndarray, NPArrayWithTag], deriv: int = 0, non0tab: None=None) -> ndarray: ...
def density_orbital_derivative(ot: transfnal, ncore: int, ncas: int, casdm1s: Tuple[ndarray, ndarray], cascm2: ndarray, rho: ndarray, mo: ndarray, deriv: int = 0, non0tab: None=None) -> Tuple[ndarray, ndarray]: ...
