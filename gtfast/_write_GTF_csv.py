__module_name__ = "_write_GTF_csv.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


msg = _Messages()

def _write_GTF_csv(GTF_df, path):
    
    msg.writing()
    GTF_df.to_csv(path)    