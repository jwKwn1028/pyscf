from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.gto.basis import parse_nwchem as parse_nwchem
from pyscf.lib.exceptions import BasisNotFoundError as BasisNotFoundError

DISABLE_EVAL: Incomplete
MAXL: int

def parse(string, symb=None, optimize: bool = False): ...
def load(basisfile, symb, optimize: bool = False): ...

BASIS_SET_DELIMITER: Incomplete

def search_seg(basisfile, symb): ...
