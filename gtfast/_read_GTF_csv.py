
__module_name__ = "_read_GTF_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


# import packages #
# --------------- #
import os
import pandas as pd


def _read_cached_GTF_filepaths(GTF_csv_path):

    """
    Read the locally-saved .txt file to find the .csv paths.

    Parameters:
    -----------
    GTF_csv_path

    Returns:
    --------
    GTFPathDict
        type: dict
    """

    GTFPathDict = {}
    paths = ["gtf_path", "gtf_csv_path", "gene_gtf_csv_path"]

    with open(GTF_csv_path, "r") as f:
        for n, line in enumerate(f.readlines()):
            GTFPathDict[paths[n]] = line.strip("\n")

    return GTFPathDict


def _read_gtf_from_csv(path):
    return pd.read_csv(path, index_col=0)


def _read_GTF_csv(genes=False, gtf_path=False, silent=False):
    
    """
    Load GTF (.csv) as a pandas DataFrame from cached path.
    
    Parameters:
    -----------
    genes
        default: False
        type: str or bool
        
    gtf_path
        default: False
        type: str or bool
        
    silent
        default: False
        type: bool
    
    Returns:
    --------
    GTF
        type: pandas.DataFrame
    
    Notes:
    ------
    (1) This is the key function that is run once the user has done the initial GTF parsing.
    
    """

    msg = _Messages(silent)

    GTF_csv_path = os.path.join(os.path.dirname(__file__), ".cached/GTF_paths.txt")

    if os.path.exists(GTF_csv_path):
        msg.cache_found(GTF_csv_path)
        GTFPathDict = _read_cached_GTF_filepaths(GTF_csv_path)
        if genes:
            msg.read_gene_csv()
            return _read_gtf_from_csv(GTFPathDict["gene_gtf_csv_path"])
        else:
            msg.read_csv()
            return _read_gtf_from_csv(GTFPathDict["gtf_csv_path"])

    else:
        assert gtf_path, msg.assert_GTF_path()
#         return _parse_GTF_to_csv(gtf_path, genes=genes, force=False, return_gtf=True)