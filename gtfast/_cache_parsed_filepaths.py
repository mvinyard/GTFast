
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


def _cache_parsed_filepaths(gtf_path, gtf_csv_path, gene_gtf_csv_path):

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


    Returns:
    --------
    None

    Notes:
    ------

    """

    msg = _Messages()
    
    GTF_path_cache = os.path.join(os.path.dirname(__file__), ".cached/GTF_paths.txt")
    pydk.mkdir_flex(".cached")
    msg.remember_paths(GTF_path_cache)
    
    with open(GTF_path_cache, "w") as f:
        f.write(gtf_path + "\n")
        f.write(gtf_csv_path + "\n")
        f.write(gene_gtf_csv_path + "\n")
        f.close()