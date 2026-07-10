from pyscf.mcscf import mc1step as mc1step
from numpy import float64, ndarray
from pyscf.fci.direct_spin1 import FCIvector
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.mcscf.mc1step import CASSCF
from pyscf.mcscf.mc1step_symm import SymAdaptedCASSCF
from typing import Optional, Tuple, Union

def kernel(casscf: Union[SymAdaptedCASSCF, CASSCF], mo_coeff: Union[ndarray, NPArrayWithTag], tol: float = 1e-07, conv_tol_grad: None=None, ci0: Optional[FCIvector]=None, callback: None=None, verbose: Optional[int]=None, dump_chk: bool = True) -> Union[Tuple[bool, float64, float64, FCIvector, ndarray, ndarray], Tuple[bool, float64, float64, ndarray, NPArrayWithTag, ndarray], Tuple[bool, float64, float64, FCIvector, NPArrayWithTag, ndarray]]: ...
