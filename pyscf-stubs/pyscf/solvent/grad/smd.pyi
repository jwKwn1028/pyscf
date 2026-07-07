from pyscf import lib as lib
from pyscf.lib import logger as logger
from pyscf.solvent import smd as smd
from pyscf.solvent.grad import pcm as pcm_grad

def grad_solver(pcmobj, dm): ...
def get_cds(smdobj): ...
make_grad_object = pcm_grad.make_grad_object
