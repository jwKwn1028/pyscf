import pyscf.lib.chkfile
from pyscf.lib.chkfile import dump as dump, dump_chkfile_key as dump_chkfile_key, load as load, load_chkfile_key as load_chkfile_key, save as save

def load_cell(chkfile): ...
dump_cell = pyscf.lib.chkfile.save_mol
save_cell = pyscf.lib.chkfile.save_mol
