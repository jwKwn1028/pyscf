from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.data.elements import ELEMENTS as ELEMENTS
from pyscf.gto import moleintor as moleintor
from numpy import ndarray
from pyscf.gto.mole import Mole
from typing import List, Optional, Tuple

libecp: Incomplete

def type1_by_shell(mol: Mole, shls: Tuple[int, int], cart: bool = False) -> ndarray: ...
def type2_by_shell(mol: Mole, shls: Tuple[int, int], cart: bool = False) -> ndarray: ...

AS_ECPBAS_OFFSET: int
AS_NECPBAS: int

def so_by_shell(mol, shls): ...
def core_configuration(nelec_core: int, atom_symbol: Optional[str]=None) -> List[int]: ...
