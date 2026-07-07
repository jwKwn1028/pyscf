from _typeshed import Incomplete
from pyscf import lib as lib
from pyscf.data.elements import ELEMENTS as ELEMENTS
from pyscf.gto import moleintor as moleintor

libecp: Incomplete

def type1_by_shell(mol, shls, cart: bool = False): ...
def type2_by_shell(mol, shls, cart: bool = False): ...

AS_ECPBAS_OFFSET: int
AS_NECPBAS: int

def so_by_shell(mol, shls): ...
def core_configuration(nelec_core, atom_symbol=None): ...
