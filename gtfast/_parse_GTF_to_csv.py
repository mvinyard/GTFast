
__module_name__ = "_parse_GTF_to_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._create_gtf_csv_dir import _create_gtf_csv_dir
from ._gtfparse import _gtfparse
from ._filter_gtf_df import _filter_gtf_df
from ._write_GTF_to_csv import _write_GTF_to_csv
from ._cache_parsed_filepaths import _cache_parsed_filepaths
from ._read_GTF_csv import _read_GTF_csv


# import packages #
# --------------- #
import os
import warnings


warnings.filterwarnings("ignore")


class _parsed_GTF:
    
    """The main/central class of this package."""
    
    def __init__(self, path):
        
        """
        Convert a .gtf file to a .csv file for much faster subsequent parsing with pandas.

        Parameters:
        -----------
        path
            path to GTF file.

        Notes:
        ------
        (1) Developed with the 10x cellranger-arc refdata.

        """
        
        self._gtf_path = path
        self._gtf_dir, self._csv_dir = _create_gtf_csv_dir(path)
        self._gtf_csv_path = os.path.join(self._csv_dir, "gtf.csv")
        self._gene_gtf_csv_path = os.path.join(self._csv_dir, "gtf.genes.csv")
        self._GTF_filt = None
        
    def parse(self):
        
        self._GTF = _gtfparse(self._gtf_path)
        self._gene_columns_to_keep = self._gtf.columns
        
        
    def filter_GTF(self, col="feature", selection="gene", keep_columns=False):        
        
        if not keep_columns:
            keep_columns = self._gene_columns_to_keep
        
        self._GTF_filt = _filter_gtf_df(self._GTF, col=col, selection=selection, keep_columns=keep_columns)
        
    def write_csv(self):
        
        _write_GTF_to_csv(self._GTF)
        del self._GTF
        
        if self._GTF_filt != None:
            _write_GTF_to_csv(self._GTF_filt)
            del self._GTF_filt
            
    def remember(self):
        
        _cache_parsed_filepaths(self._gtf_path, self._gtf_csv_path, self._gene_gtf_csv_path)
        
    def read_GTF_csv(self, genes=False):
        
        if genes:
            self._GTF_genes = _read_GTF_csv(genes=genes, path=self._gtf_path)
        else:
            self._GTF = _read_GTF_csv(genes=genes, path=self._gtf_path)
            
            
            
def _parse_GTF_to_csv(path, genes=False, force=False, return_gtf=False):

    """
    Parameters:
    -----------
    path
        type: str
    
    genes
        Indicate if the GTF returned should be subset to genes only. 
        type: bool
        default: False
    
    force
        Force re-parsing of the GTF file.
        type: bool
        default: False
    
    return_gtf
        Indicate if the GTF should be returned.
        type: bool
        default: False
        
    Returns:
    --------
    [ optionally ] GTF
        type: pandas.DataFrame
        
    Notes:
    ------
    """
    
    _GTF = _parsed_GTF(path)
    
    if not os.path.exists(_GTF._gtf_csv_path) or not os.path.exists(_GTF._gene_gtf_csv_path) or force:
        _GTF.parse()
        _GTF.filter_GTF(col="feature", selection="gene", keep_columns=False)
        _GTF.write_csv()
        _GTF.remember()
        _GTF.read_GTF_csv(genes=genes, path=False)
    
    if return_gtf:
        return _GTF.read_GTF_csv(genes=genes, path=False)
    