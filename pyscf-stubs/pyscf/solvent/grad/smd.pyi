from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.solvent import smd as smd
from pyscf.solvent.grad import pcm as pcm_grad
from numpy import ndarray
from pyscf.lib.numpy_helper import NPArrayWithTag
from pyscf.solvent.smd import SMD
from typing import Union

def grad_solver(pcmobj: SMD, dm: Union[ndarray, NPArrayWithTag]) -> ndarray: ...
def get_cds(smdobj: SMD) -> ndarray: ...
make_grad_object = pcm_grad.make_grad_object
