# PySCF Local Smoke Testing

Local PySCF testing should be treated as correctness and smoke testing, not
production benchmarking. The goal is to catch syntax, workflow, convergence,
and I/O bugs while hard-capping CPU and memory usage.

## 1. Limit PySCF and BLAS threads

Put thread limits at the very top of the test script, before importing NumPy or
PySCF:

```python
import os

os.environ["OMP_NUM_THREADS"] = "2"
os.environ["MKL_NUM_THREADS"] = "2"
os.environ["OPENBLAS_NUM_THREADS"] = "2"
os.environ["NUMEXPR_NUM_THREADS"] = "2"

from pyscf import lib
lib.num_threads(2)
```

Alternatively, set the limits from the shell:

```bash
OMP_NUM_THREADS=2 \
MKL_NUM_THREADS=2 \
OPENBLAS_NUM_THREADS=2 \
NUMEXPR_NUM_THREADS=2 \
python test_job.py
```

This is the most important local safety step. BLAS and OpenMP libraries may
otherwise use every CPU core.

## 2. Set PySCF memory limits

For molecular jobs, set memory on both the molecule and the method object:

```python
from pyscf import gto, scf

mol = gto.M(
    atom="H 0 0 0; F 0 0 0.9",
    basis="sto-3g",
    max_memory=1000,  # MB
)

mf = scf.RHF(mol)
mf.max_memory = 1000  # MB
mf.kernel()
```

This does not guarantee that the operating system will never see higher memory
usage, but PySCF will try to keep major intermediates within the limit.

## 3. Use tiny local test systems

For local testing, use a tiny molecule that exercises the same code path:

```python
atom = """
O  0.000000  0.000000  0.000000
H  0.000000 -0.757000  0.587000
H  0.000000  0.757000  0.587000
"""
basis = "sto-3g"
```

Another useful option:

```python
atom = "He 0 0 0"
basis = "cc-pVDZ"
```

Recommended local testing ladder:

```text
He/STO-3G
H2O/STO-3G
H2O/cc-pVDZ
small fragment of the real molecule/STO-3G
```

Use the same workflow, not the same production chemistry.

## 4. Add a test mode to scripts

A good pattern is to support a small local mode:

```python
import argparse
from pyscf import gto, scf

parser = argparse.ArgumentParser()
parser.add_argument("--test", action="store_true")
args = parser.parse_args()

if args.test:
    atom = "O 0 0 0; H 0 -0.757 0.587; H 0 0.757 0.587"
    basis = "sto-3g"
    max_memory = 1000
else:
    atom = open("geom.xyz").read()
    basis = "cc-pVTZ"
    max_memory = 64000

mol = gto.M(
    atom=atom,
    basis=basis,
    max_memory=max_memory,
    verbose=4,
)

mf = scf.RHF(mol)
mf.max_memory = max_memory
mf.kernel()
```

Run locally:

```bash
OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 python run.py --test
```

Run the full production job on the cluster:

```bash
python run.py
```

## 5. Hard-cap the process from the shell

On Linux or macOS, use `ulimit` before running:

```bash
ulimit -v $((6 * 1024 * 1024))   # 6 GB virtual memory limit, in KB
ulimit -t 1800                   # 30 minutes CPU time
python test_job.py
```

A reusable wrapper:

```bash
#!/usr/bin/env bash
set -euo pipefail

export OMP_NUM_THREADS=2
export MKL_NUM_THREADS=2
export OPENBLAS_NUM_THREADS=2
export NUMEXPR_NUM_THREADS=2

ulimit -v $((6 * 1024 * 1024))   # 6 GB
ulimit -t 1800                   # 30 minutes CPU time

python "$@"
```

Save it as something like `~/bin/safe-python` and run:

```bash
safe-python run.py --test
```

## 6. Use nice for responsiveness

Run local jobs with lower scheduling priority:

```bash
nice -n 10 python run.py --test
```

For disk-heavy jobs on Linux:

```bash
ionice -c 2 -n 7 nice -n 10 python run.py --test
```

This does not reduce the total computation, but it helps keep the laptop
responsive.

## 7. Prefer checkpoints for expensive steps

For SCF workflows:

```python
mf = scf.RHF(mol)
mf.chkfile = "test_scf.chk"
mf.kernel()
```

Then reuse the checkpoint:

```python
mf.init_guess = "chkfile"
mf.chkfile = "test_scf.chk"
```

This helps when testing post-HF or DFT workflows without repeating every
expensive setup step.

## 8. Keep post-HF tests deliberately small

For CASSCF or CASCI, test with a tiny active space:

```python
from pyscf import mcscf

mc = mcscf.CASSCF(mf, 2, 2)
mc.kernel()
```

For MP2 and CCSD, use tiny molecules only. CCSD and especially CCSD(T) can
become unreasonable very quickly.

## Recommended local wrapper

```bash
#!/usr/bin/env bash
set -euo pipefail

export OMP_NUM_THREADS="${OMP_NUM_THREADS:-2}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-2}"
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-2}"
export NUMEXPR_NUM_THREADS="${NUMEXPR_NUM_THREADS:-2}"

# Optional hard limits
ulimit -v $((8 * 1024 * 1024)) || true   # 8 GB virtual memory
ulimit -t 3600 || true                   # 1 hour CPU time

exec nice -n 10 python "$@"
```

Use it as:

```bash
safe-pyscf run.py --test
```

## Practical recommendation

Every serious PySCF script should have a `--test` or `--small` mode. Always run
that mode locally with explicit thread limits before sending the real job to a
cluster.
