from _typeshed import Incomplete
from pyscf import gto as gto, lib as lib
from pyscf.ao2mo.outcore import balance_segs as balance_segs
from pyscf.pbc.df.incore import make_auxcell as make_auxcell, wrap_int3c as wrap_int3c
from pyscf.pbc.lib.kpts_helper import KPT_DIFF_TOL as KPT_DIFF_TOL, gamma_point as gamma_point, unique as unique
from numpy import ndarray
from pyscf.pbc.gto.cell import Cell
from typing import Optional

libpbc: Incomplete

def aux_e1(cell: Cell, auxcell_or_auxbasis: Cell, erifile: str, intor: str = 'int3c2e', aosym: str = 's2ij', comp: Optional[int]=None, kptij_lst: Optional[ndarray]=None, dataname: str = 'eri_mo', shls_slice: None=None, max_memory: int = 2000, verbose: int = 0) -> str: ...
