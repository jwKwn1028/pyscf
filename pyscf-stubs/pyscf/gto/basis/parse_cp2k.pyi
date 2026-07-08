from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.gto.basis import parse_nwchem as parse_nwchem
from pyscf.lib.exceptions import BasisNotFoundError as BasisNotFoundError
from typing import List, Optional, Union

DISABLE_EVAL: Incomplete
MAXL: int

def parse(string: str, symb: Optional[str]=None, optimize: bool = False) -> List[List[Union[int, List[float]]]]: ...
def load(basisfile: str, symb: str, optimize: bool = False) -> List[List[Union[int, List[float]]]]: ...

BASIS_SET_DELIMITER: Incomplete

def search_seg(basisfile: str, symb: str) -> List[str]: ...
