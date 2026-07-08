from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df import FFTDF as FFTDF
from pyscf.pbc.dft.gen_grid import UniformGrids as UniformGrids
from pyscf.pbc.dft.numint import NumInt as NumInt
from pyscf.pbc.grad.rks_stress import ewald as ewald, strain_tensor_dispalcement as strain_tensor_dispalcement
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.pbc.grad.uks import Gradients
from pyscf.pbc.gto.cell import Cell
from typing import Union

def get_vxc(ks_grad: Gradients, cell: Cell, dm: Union[ndarray, NPArrayWithTag], with_j: bool = False, with_nuc: bool = False) -> ndarray: ...
def kernel(mf_grad: Gradients) -> ndarray: ...
