from functools import reduce as reduce
from pyscf import gto as gto, lib as lib
from pyscf.pbc.df import incore as incore

def ecp_int(cell, kpts=None, intor: str = 'ECPscalar'): ...
