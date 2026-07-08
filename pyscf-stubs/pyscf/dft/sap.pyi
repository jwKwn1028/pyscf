from pyscf.dft.sap_data import sap_Zeff as sap_Zeff
from numpy import int32, ndarray

def sap_effective_charge(Z: int32, r: ndarray) -> ndarray: ...
