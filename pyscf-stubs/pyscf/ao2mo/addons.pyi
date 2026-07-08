import types
from _typeshed import Incomplete
from pyscf import lib as lib
from h5py._hl.dataset import Dataset
from numpy import ndarray
from pyscf.lib.misc import H5TmpFile
from tempfile import _TemporaryFileWrapper
from typing import Union

libao2mo: Incomplete

class load:
    eri: Incomplete
    dataname: Incomplete
    feri: Incomplete
    def __init__(self, eri: Union[ndarray, _TemporaryFileWrapper, str, H5TmpFile], dataname: str = 'eri_mo') -> None: ...
    def __enter__(self) -> Union[ndarray, Dataset]: ...
    def __exit__(self, type: None, value: None, traceback: None) -> None: ...

def restore(symmetry: Union[int, str], eri: ndarray, norb: int, tao: None=None) -> ndarray: ...
