from _typeshed import Incomplete
from pyscf import ao2mo as ao2mo, lib as lib
from pyscf.cc import ccsd_rdm as ccsd_rdm
from pyscf.grad.mp2 import has_frozen_orbitals as has_frozen_orbitals

def kernel(cc, t1, t2, l1, l2, eris=None): ...

class _ERIS:
    oooo: Incomplete
    ooov: Incomplete
    ovoo: Incomplete
    oovo: Incomplete
    oovv: Incomplete
    ovov: Incomplete
    ovvo: Incomplete
    ovvv: Incomplete
    vvvv: Incomplete
    vvvo: Incomplete
    vovv: Incomplete
    vvov: Incomplete
    vvoo: Incomplete
    voov: Incomplete
    vooo: Incomplete
    mo_coeff: Incomplete
    fock: Incomplete
    def __init__(self, cc, mo_coeff) -> None: ...

def index_frozen_active(cc): ...
