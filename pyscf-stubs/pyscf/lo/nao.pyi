from _typeshed import Incomplete
from pyscf import __config__ as __config__, lib as lib, scf as scf
from pyscf.data import elements as elements
from pyscf.gto import mole as mole
from pyscf.lib import logger as logger
from pyscf.lo import orth as orth

AOSHELL: Incomplete

def prenao(mol, dm): ...
def nao(mol, mf, s=None, restore: bool = True): ...
def set_atom_conf(element, description): ...
