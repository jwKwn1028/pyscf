from _typeshed import Incomplete
from pyscf import __config__ as __config__
from pyscf.md import distributions as distributions, integrators as integrators

SEED: Incomplete
rng: Incomplete

def set_seed(seed: int) -> None: ...
NVE = integrators.VelocityVerlet
