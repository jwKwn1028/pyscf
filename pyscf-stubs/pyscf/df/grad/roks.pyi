from pyscf.df.grad import uks as uks
from pyscf.grad import rohf as rohf

class Gradients(uks.Gradients):
    make_rdm1e = rohf.make_rdm1e
Grad = Gradients
