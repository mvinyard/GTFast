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

gtf = "/path/to/ref/hg38/refdata-cellranger-arc-GRCh38-2020-A-2.0.0/genes/genes.gtf"

adata = anndata.read_h5ad("/path/to/singlecell/data/adata.h5ad")
ag.lift_genes(adata, gtf)
```
