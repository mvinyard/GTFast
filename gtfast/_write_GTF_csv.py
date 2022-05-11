
__module_name__ = "_write_GTF_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages

def _write_GTF_csv(GTF_df, path, silent=False):
    
    msg = _Messages(silent)
    msg.writing(path)
    GTF_df.to_csv(path)    