from pyscf.df.grad import uhf as uhf
from pyscf.grad import rohf as rohf

class Gradients(uhf.Gradients):
    make_rdm1e = rohf.make_rdm1e
Grad = Gradients
