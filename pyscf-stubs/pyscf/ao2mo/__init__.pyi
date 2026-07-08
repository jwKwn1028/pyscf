from pyscf import gto as gto
from pyscf.ao2mo import incore as incore, outcore as outcore, r_outcore as r_outcore
from pyscf.ao2mo.addons import load as load, restore as restore
from numpy import ndarray
from pyscf.gto.mole import Mole
from pyscf.lib.misc import H5TmpFile
from pyscf.lib.numpy_helper import NPArrayWithTag
from tempfile import _TemporaryFileWrapper
from typing import List, Optional, Tuple, Union

def full(eri_or_mol: Union[ndarray, Mole], mo_coeff: ndarray, erifile: Optional[Union[str, H5TmpFile, _TemporaryFileWrapper]]=None, dataname: str = 'eri_mo', intor: str = 'int2e', *args, **kwargs) -> Union[ndarray, H5TmpFile, str]: ...
def general(eri_or_mol: Union[Mole, ndarray], mo_coeffs: Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray], List[ndarray], Tuple[NPArrayWithTag, NPArrayWithTag, NPArrayWithTag, NPArrayWithTag]], erifile: Optional[Union[H5TmpFile, str, _TemporaryFileWrapper]]=None, dataname: str = 'eri_mo', intor: str = 'int2e', *args, **kwargs) -> Union[ndarray, H5TmpFile, str]: ...
def kernel(eri_or_mol: Union[Mole, ndarray], mo_coeffs: Union[ndarray, Tuple[ndarray, ndarray, ndarray, ndarray], List[ndarray]], erifile: Optional[Union[H5TmpFile, _TemporaryFileWrapper, str]]=None, dataname: str = 'eri_mo', intor: str = 'int2e', *args, **kwargs) -> Union[ndarray, H5TmpFile, str]: ...
def get_ao_eri(mol: Mole) -> ndarray: ...
get_mo_eri = kernel
