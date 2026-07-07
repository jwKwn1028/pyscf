from pyscf.df.grad import rks as dfrks_grad
from pyscf.sgx.grad.rhf import _GradientsMixin, get_jk as get_jk

class Gradients(_GradientsMixin, dfrks_grad.Gradients):
    get_jk = get_jk
Grad = Gradients
