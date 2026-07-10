from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.pbc.df import FFTDF as FFTDF
from pyscf.pbc.dft.gen_grid import UniformGrids as UniformGrids
from pyscf.pbc.dft.krkspu import reference_mol as reference_mol
from pyscf.pbc.dft.numint import KNumInt as KNumInt
from pyscf.pbc.grad.krks_stress import get_ovlp as get_ovlp
from pyscf.pbc.grad.rks_stress import ewald as ewald, strain_tensor_dispalcement as strain_tensor_dispalcement

def get_vxc(ks_grad, cell, dm_kpts, kpts, with_j: bool = False, with_nuc: bool = False): ...
def kernel(mf_grad): ...
