from pyscf.fci import addons as addons, cistring as cistring, direct_nosym as direct_nosym, direct_spin0 as direct_spin0, direct_spin0_symm as direct_spin0_symm, direct_spin1 as direct_spin1, direct_spin1_symm as direct_spin1_symm, direct_uhf as direct_uhf, fci_dhf_slow as fci_dhf_slow, rdm as rdm, selected_ci as selected_ci, selected_ci_spin0 as selected_ci_spin0, selected_ci_spin0_symm as selected_ci_spin0_symm, selected_ci_symm as selected_ci_symm, spin_op as spin_op
from pyscf.fci.cistring import num_strings as num_strings
from pyscf.fci.direct_spin1 import FCIvector as FCIvector, make_diag_precond as make_diag_precond, make_pspace_precond as make_pspace_precond
from pyscf.fci.rdm import reorder_rdm as reorder_rdm
from pyscf.fci.selected_ci import SCI as SCI, SCIvector as SCIvector, SelectedCI as SelectedCI
from pyscf.fci.spin_op import spin_square as spin_square

select_ci = selected_ci

def solver(mol=None, singlet: bool = False, symm=None): ...
def FCI(mol_or_mf, mo=None, singlet: bool = False): ...
