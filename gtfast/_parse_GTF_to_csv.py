
__module_name__ = "_parse_GTF_to_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._cache_parsed_filepaths import _cache_parsed_filepaths
from ._create_gtf_csv_dir import _create_gtf_csv_dir
from ._filter_gtf_df import _filter_gtf_df
from ._gtfparse import _gtfparse
from ._read_GTF_csv import _read_GTF_csv
from ._write_GTF_csv import _write_GTF_csv


# import packages #
# --------------- #
import os
import warnings


warnings.filterwarnings("ignore")


class _parsed_GTF:
    
    """The main/central class of this package."""
    
    def __init__(self, path, silent=False):
        
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
        self._silent = silent
        self._gtf_dir, self._csv_dir = _create_gtf_csv_dir(self._gtf_path)
        self._gtf_csv_path = os.path.join(self._csv_dir, "gtf.csv")
        self._gene_gtf_csv_path = os.path.join(self._csv_dir, "gtf.genes.csv")
        self._GTF_filt = None
        
    def parse(self):
        
        self._GTF = _gtfparse(self._gtf_path, silent=self._silent)
        self._keep_columns = self._GTF.columns
        
        
    def filter_GTF(self, col="feature", selection="gene", keep_columns=False):        
        
        if not keep_columns:
            keep_columns = self._keep_columns
        
        self._GTF_filt = _filter_gtf_df(self._GTF, col=col,
                                        selection=selection,
                                        keep_columns=keep_columns,
                                        silent=self._silent,
                                       )
        
    def write_csv(self):
        
        _write_GTF_csv(self._GTF,
                       self._gtf_csv_path,
                       self._silent,
                      )
        del self._GTF
        _write_GTF_csv(self._GTF_filt,
                       self._gene_gtf_csv_path,
                       self._silent,
                      )
        del self._GTF_filt
            
    def remember(self):
        
        _cache_parsed_filepaths(self._gtf_path,
                                self._gtf_csv_path,
                                self._gene_gtf_csv_path,
                                self._silent)
                  
            
def _parse_GTF_to_csv(path, genes=False, force=False, silent=False):

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
        
    silent
        default: False
        type: bool
        
    Returns:
    --------
    [ optionally ] GTF
        type: pandas.DataFrame
        
    Notes:
    ------
    """
    
    _GTF = _parsed_GTF(path, silent)
    
    if not os.path.exists(_GTF._gtf_csv_path) or not os.path.exists(_GTF._gene_gtf_csv_path) or force:
        _GTF.parse()
        _GTF.filter_GTF(col="feature", selection="gene", keep_columns=False)
        _GTF.write_csv()
        _GTF.remember()
    