from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.lib.parameters import OUTPUT_COLS as OUTPUT_COLS, OUTPUT_DIGITS as OUTPUT_DIGITS
from io import TextIOWrapper
from numpy import ndarray
from typing import List, Optional

BASE: Incomplete

def dump_tri(stdout, c, label=None, ncol=..., digits=..., start=...) -> None: ...
def dump_rec(stdout: TextIOWrapper, c: ndarray, label: Optional[List[str]]=None, label2: None=None, ncol: int=..., digits: int=..., start: int=...) -> None: ...
def dump_mo(mol, c, label=None, ncol=..., digits=..., start=...) -> None: ...
