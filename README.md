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

### Example usage

```python
import anndata
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

To be implemented...
```
adata = anndata.read_h5ad("/path/to/singlecell/data/adata.h5ad")
ag.lift_genes(adata, gtf) 
```
