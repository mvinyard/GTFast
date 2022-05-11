
__module_name__ = "_create_gtf_csv_dir.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


# import packages #
# --------------- #
import os
import pydk


def _create_gtf_csv_dir(path, silent=False):

    """
    Make a directory for the .csv files, adjacent to the original .gtf file.
    
    Parameters:
    -----------
    path
        type: str
        
    silent
        default: False
        type: bool
    """
    
    msg = _Messages()

    gtf_dir = os.path.dirname(path)
    csv_dir = os.path.join(gtf_dir, "csv")
    
    if not os.path.exists(csv_dir):
        msg.mk_csv_dir(csv_dir)
        pydk.mkdir_flex(csv_dir)

    return gtf_dir, csv_dir