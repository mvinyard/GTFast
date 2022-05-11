
__module_name__ = "_filter_gtf_df.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import local modules #
# -------------------- #
from ._Messages import _Messages


def _filter_gtf_df(GTF_df, col, selection, keep_columns, silent=False):

    """
    Filter a GTF on a specific feature type (e.g., genes)

    Parameters:
    -----------
    GTF_df
        pandas DataFrame of a GTF
        type: pd.DataFrame

    col
        colname on which df.loc will be performed
        type: str

    selection
        value in df[col]
        type: str, int, float, etc. (most likely str)

    keep_columns
        A list of strings of colnames to keep. If False (default behavior), all cols are kept.
        type: bool
        default: False

    silent
        default: False
        type: bool
    
    Returns:
    --------
    GTF_filtered
        type: pandas.DataFrame
    """
    
    msg = _Messages(silent)
    msg.filtering(col, selection)

    return GTF_df.loc[GTF_df[col] == selection][keep_columns]