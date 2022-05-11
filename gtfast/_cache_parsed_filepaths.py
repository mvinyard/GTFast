
__module_name__ = "_cache_parsed_filepaths.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


# import packages #
# --------------- #
import os
import pydk


def _cache_parsed_filepaths(gtf_path, gtf_csv_path, gene_gtf_csv_path, silent=False):

    """
    Write a file, recording the .csv and .gtf files for later reading.

    Parameters:
    -----------
    gtf_path
        type: str

    gtf_csv_path
        type: str

    gene_gtf_csv_path
        type: str
    
    silent
        default: False
        type: bool

    Returns:
    --------
    None

    Notes:
    ------

    """

    msg = _Messages(silent)
    
    to_write = [gtf_path, gtf_csv_path, gene_gtf_csv_path]
    
    cache_dir = os.path.join(os.path.dirname(__file__), ".cached")
    cached_GTF_path= os.path.join(cache_dir, "GTF_paths.txt")
    
    pydk.mkdir_flex(cache_dir)
    msg.remember_paths(cached_GTF_path)
    
    with open(cached_GTF_path, "w") as f:
        for path in to_write:
            f.write(path + "\n")
        f.close()