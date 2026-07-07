from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df import FFTDF as FFTDF
from pyscf.pbc.dft.gen_grid import UniformGrids as UniformGrids
from pyscf.pbc.dft.numint import NumInt as NumInt
from pyscf.pbc.grad.rks_stress import ewald as ewald, strain_tensor_dispalcement as strain_tensor_dispalcement

def get_vxc(ks_grad, cell, dm, with_j: bool = False, with_nuc: bool = False): ...
def kernel(mf_grad): ...
