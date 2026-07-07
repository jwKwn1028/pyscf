from pyscf import hessian as hessian
from pyscf.lib import logger as logger
from pyscf.scf.dispersion import check_disp as check_disp, parse_disp as parse_disp

def get_dispersion(hessobj, disp=None, with_3body=None): ...
