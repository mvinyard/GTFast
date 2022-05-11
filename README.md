# GTFast

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/gtfast.svg)](https://pypi.python.org/pypi/gtfast/)
[![PyPI version](https://badge.fury.io/py/gtfast.svg)](https://badge.fury.io/py/gtfast)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Installation

To install via [pip](https://pypi.org/project/gtfast):
```BASH
pip install gtfast
```

To install the development version: 
```BASH
git clone https://github.com/mvinyard/gtfast.git

cd gtfast; pip install -e .
```

## Example usage

### Parsing a `.gtf` file
```python
import gtfast

gtf_filepath = "/path/to/ref/hg38/refdata-cellranger-arc-GRCh38-2020-A-2.0.0/genes/genes.gtf"

```

If this is your first time using `gtfast`, run:
```python
gtf = gtfast.parse(path=gtf_filepath, genes=False, force=False, return_gtf=True)
```
Running this function will create two `.csv` files from the given `.gtf` files - one containing all feature types and one containing only genes. Both of these files are smaller than a `.gtf` and can be loaded into memory much faster using `pandas.read_csv()` (shortcut implemented in the next function). Additionally, this function leaves a paper trail for `gtfast` to find the newly-created `.csv` files again in the future such that one does not need to pass a path to the gtf. 

In the scenario in which you've already run the above function, run:
```python
gtf = gtfast.load() # no path necessary! 
```

### Interfacing with [AnnData](https://anndata.readthedocs.io/en/stable/) and updating an `adata.var` table. 

If you're workign with single-cell data, you can easily lift annotations from a **[`gtf`](https://en.wikipedia.org/wiki/Gene_transfer_format)** to your **[`adata`](https://anndata.readthedocs.io/en/stable/)** object. 

```python
from anndata import read_h5ad
import gtfast

adata = read_h5ad("/path/to/singlecell/data/adata.h5ad")
gtf = gtfast.load(genes=True)

gtfast.add(adata, gtf)
```

Since the `gtfast` distribution already knows where the `.csv / .gtf` files are, we could directly annotate `adata` without first specifcying `gtf` as a DataFrame, saving a step but I think it's more user-friendly to see what each one looks like, first. 


### Working advantage

Let's take a look at the time difference of loading a `.gtf` into memory as a `pandas.DataFrame`: 

```python
import gtfast
import gtfparse
import time

start = time.time()
gtf = gtfparse.read_gtf("/home/mvinyard/ref/hg38/refdata-cellranger-arc-GRCh38-2020-A-2.0.0/genes/genes.gtf")
stop = time.time()

print("baseline loading time: {:.2f}s".format(stop - start), end='\n\n')

start = time.time()
gtf = gtfast.load()
stop = time.time()

print("GTFast loading time: {:.2f}s".format(stop - start))
```
```
baseline loading time: 87.54s

GTFast loading time: 12.46s
```
~ 7x speed improvement. 

* **Note**: This is not meant to criticize or comment on anything related to [`gtfparse`](https://github.com/openvax/gtfparse) - in fact, this library relies solely on `gtfparse` for the actual parsing of a `.gtf` file into memory as `pandas.DataFrame` and it's an amazing tool for python developers!

### Contact

If you have suggestions, questions, or comments, please reach out to Michael Vinyard via [email](mailto:mvinyard@broadinstitute.org)