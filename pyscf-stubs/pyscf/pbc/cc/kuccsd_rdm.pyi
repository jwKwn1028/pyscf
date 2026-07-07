from pyscf import lib as lib

einsum = lib.einsum

def make_rdm1(mycc, t1, t2, l1=None, l2=None, ao_repr: bool = False): ...
