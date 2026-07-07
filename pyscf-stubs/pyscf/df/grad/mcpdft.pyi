from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.df.grad import sacasscf as dfsacasscf_grad
from pyscf.grad import mcpdft as mcpdft_grad

class Gradients(dfsacasscf_grad.Gradients, mcpdft_grad.Gradients):
    auxbasis_response: bool
    def __init__(self, pdft, state=None) -> None: ...
    def get_ham_response(self, **kwargs): ...
    kernel: Incomplete
    get_wfn_response: Incomplete
    get_init_guess: Incomplete
    project_Aop: Incomplete
