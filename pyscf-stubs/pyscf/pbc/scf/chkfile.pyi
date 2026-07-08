from pyscf.lib.chkfile import dump as dump, dump_chkfile_key as dump_chkfile_key, load as load, load_chkfile_key as load_chkfile_key, save as save
from pyscf.pbc.lib.chkfile import load_cell as load_cell, save_cell as save_cell
from pyscf.scf.chkfile import dump_scf as dump_scf
from numpy import float64, ndarray
from pyscf.pbc.gto.cell import Cell
from typing import Dict, List, Tuple, Union

def load_scf(chkfile: str) -> Union[Tuple[Cell, Dict[str, Union[float64, ndarray, List[ndarray]]]], Tuple[Cell, Dict[str, Union[float64, ndarray]]]]: ...
