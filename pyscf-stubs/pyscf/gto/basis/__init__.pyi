from _typeshed import Incomplete
from pyscf.gto.basis import parse_nwchem
from numpy import float64
from typing import Any, Callable, List, Optional, Tuple, Union

__all__ = ['ALIAS', 'GTH_ALIAS', 'PP_ALIAS', 'parse', 'parse_ecp', 'load', 'load_ecp', 'load_pseudo', 'optimize_contraction', 'to_general_contraction']

ALIAS: Incomplete
GTH_ALIAS: Incomplete
PP_ALIAS: Incomplete

def parse(string: str, symb: Optional[str]=None, optimize: bool=...) -> List[List[Union[int, List[float]]]]: ...
def parse_ecp(string: str, symb: None=None) -> List[Union[int, List[List[Union[int, List[List[Any]], List[List[Union[Any, List[float]]]]]]], List[List[Union[int, List[List[Union[Any, List[float]]]]]]]]]: ...
optimize_contraction = parse_nwchem.optimize_contraction
to_general_contraction = parse_nwchem.to_general_contraction

def load(filename_or_basisname: str, symb: str, optimize: bool=...) -> List[List[Union[int, List[Union[float, int]], List[float]]]]: ...
def load_ecp(filename_or_basisname: str, symb: str) -> List[Union[int, List[List[Union[int, List[List[Union[Any, List[float]]]], List[List[Union[List[Union[float, float64]], Any]]]]]], Any, List[List[Union[int, List[List[Union[Any, List[float]]]]]]]]]: ...
def load_pseudo(filename_or_basisname: str, symb: str) -> List[Any]: ...
