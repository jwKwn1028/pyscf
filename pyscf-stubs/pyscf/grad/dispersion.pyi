from pyscf import grad as grad
from pyscf.lib import logger as logger
from pyscf.scf.dispersion import check_disp as check_disp, parse_disp as parse_disp

def get_dispersion(mf_grad, disp=None, with_3body=None, verbose=None): ...
