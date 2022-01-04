# anngtf

[![PyPI pyversions](https://img.shields.io/pypi/pyversions/licorice.svg)](https://pypi.python.org/pypi/anngtf/)
[![PyPI version](https://badge.fury.io/py/anngtf.svg)](https://badge.fury.io/py/anngtf)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Lift annotations from a **[`gtf`](https://en.wikipedia.org/wiki/Gene_transfer_format)** to your **[`adata`](https://anndata.readthedocs.io/en/stable/)** object. 

### Installation

To install via [pip](https://pypi.org/project/anngtf):
```BASH
pip install anngtf
```

To install the development version: 
```BASH
git clone https://github.com/mvinyard/anngtf.git

cd anngtf; pip install -e .
```

## Example usage

### Parsing a `.gtf` file
```python
import anngtf

gtf_filepath = "/path/to/ref/hg38/refdata-cellranger-arc-GRCh38-2020-A-2.0.0/genes/genes.gtf"

```

If this is your first time using `anngtf`, run:
```python
gtf = anngtf.parse(path=gtf_filepath, genes=False, force=False, return_gtf=True)
```
Running this function will create two `.csv` files from the given `.gtf` files - one containing all feature types and one containing only genes. Both of these files are smaller than a `.gtf` and can be loaded into memory much faster using `pandas.read_csv()` (shortcut implemented in the next function). Additionally, this function leaves a paper trail for `anngtf` to find the newly-created `.csv` files again in the future such that one does not need to pass a path to the gtf. 

In the scenario in which you've already run the above function, run:
```python
gtf = anngtf.load() # no path necessary! 
```

### Updating the `adata.var` table. 
```python
import anndata as a
import anngtf

adata = anndata.read_h5ad("/path/to/singlecell/data/adata.h5ad")
gtf = anngtf.load(genes=True)

anngtf.add(adata, gtf)
```

Since the `anngtf` distribution already knows where the `.csv / .gtf` files are, we could directly annotate `adata` without first specifcying `gtf` as a DataFrame, saving a step but I think it's more user-friendly to see what each one looks like, first. 


### Working advantage

Let's take a look at the time difference of loading a `.gtf` into memory as a `pandas.DataFrame`: 

```python
import anngtf
import gtfparse
import time

start = time.time()
gtf = gtfparse.read_gtf("/home/mvinyard/ref/hg38/refdata-cellranger-arc-GRCh38-2020-A-2.0.0/genes/genes.gtf")
stop = time.time()

print("baseline loading time: {:.2f}s".format(stop - start), end='\n\n')

start = time.time()
gtf = anngtf.load()
stop = time.time()

print("anngtf loading time: {:.2f}s".format(stop - start))
```
```
baseline loading time: 87.54s

anngtf loading time: 12.46s
```
~ 7x speed improvement. 

* **Note**: This is not meant to criticize or comment on anything related to [`gtfparse`](https://github.com/openvax/gtfparse) - in fact, this library relies solely on `gtfparse` for the actual parsing of a `.gtf` file into memory as `pandas.DataFrame`.
