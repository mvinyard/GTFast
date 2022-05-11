
__module_name__ = "_Messages.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import packages #
# --------------- #
import licorice_font


def _print_message(msg, silent):
    
    if not silent:
        print(msg)

class _Messages:
    def __init__(self, silent=False):
        
        self._silent = silent
        self._info_prefix = licorice_font.font_format(" - INFO - ", ["BOLD"])
        
    def gtfparse(self, path):
        
        self._gtfparse = "{}| Reading GTF: {} to pd.DataFrame using `gtfparse.read_gtf()`".format(
            self._info_prefix, path
        )
        _print_message(self._gtfparse, self._silent)
        
    def filtering(self, col, selection):
        
        self._filtering = "{}| Filtering GTF on GTF['{}']=='{}'".format(
            self._info_prefix, col, selection
        )
        _print_message(self._filtering, self._silent)
        
    def writing(self, path):
        
        self._writing = "{}| Writing GTF DataFrame to: {}".format(self._info_prefix, path)
        _print_message(self._writing, self._silent)

    def read_csv(self):
        
        self._read_gtf_csv = "{}| Reading GTF .csv file to pd.DataFrame".format(
            self._info_prefix
        )
        _print_message(self._read_gtf_csv, self._silent)

    def read_gene_csv(self):
        
        self._read_gene_csv = (
            "{}| Reading GTF (gene only) .csv file to pd.DataFrame".format(
                self._info_prefix
            )
        )
        _print_message(self._read_gene_csv, self._silent)

    def cache_found(self, path):
        
        self._cache_found = "{}| Cached paths to GTF .csv files found: {}".format(
            self._info_prefix, path
        )
        _print_message(self._cache_found, self._silent)

    def assert_GTF_path(self):

        self._assert_GTF_path = (
            "{}| No .csv found. Path (path to GTF) must be provided".format(
                self._info_prefix
            )
        )
        _print_message(self._assert_GTF_path, self._silent)

    def remember_paths(self, path):
        
        self._read_cache = "{}| Caching paths to {} for later reading".format(
            self._info_prefix, path
        )
        _print_message(self._read_cache, self._silent)
        
    def mk_csv_dir(self, path):
        
        self._mk_csv_dir = "{}| Making ref dir for .csv files: {}".format(self._info_prefix, path)
        _print_message(self._mk_csv_dir, self._silent)
