import types
from _typeshed import Incomplete
from pyscf import lib as lib

libao2mo: Incomplete

class load:
    eri: Incomplete
    dataname: Incomplete
    feri: Incomplete
    def __init__(self, eri, dataname: str = 'eri_mo') -> None: ...
    def __enter__(self): ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

def restore(symmetry, eri, norb, tao=None): ...
