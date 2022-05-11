
__module_name__ = "_gtfparse.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


# import packages #
# --------------- #
import gtfparse


def _gtfparse(gtf_path, silent=False):
    
    msg = _Messages(silent)
    msg.gtfparse(gtf_path)
    return gtfparse.read_gtf(gtf_path)