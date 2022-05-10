
__module_name__ = "_Messages.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


# import packages #
# --------------- #
import licorice_font


class _Messages:
    def __init__(self):

        self._info_prefix = licorice_font.font_format(" - INFO - ", ["BOLD"])
        
    def gtfparse(self, path):
        
        self._gtfparse = "{}| Reading GTF from {} to pd.DataFrame using `gtfparse.read_gtf()`".format(
            self._info_prefix, path
        )
        print(self._gtfparse)
        
    def filtering(self, col, selection):
        
        self._filtering = "{}| Filtering GTF on GTF[{}]=={}".format(
            self._info_prefix, col, selection
        )
        print(self._filtering)
        
    def writing(self, path):
        self._writing = "{}| Writing GTF DataFrame to: {}".format(self._info_prefix, path)
        print(self._writing)

    def read_csv(self):
        self._read_gtf_csv = "{}| Reading GTF .csv file to pd.DataFrame".format(
            self._info_prefix
        )
        print(self._read_gtf_csv)

    def read_gene_csv(self):
        self._read_gene_csv = (
            "{}| Reading GTF (gene only) .csv file to pd.DataFrame".format(
                self._info_prefix
            )
        )
        print(self._read_gene_csv)

    def cache_found(self, path):
        self._cache_found = "{}| Cached paths to GTF .csv files found: {}".format(
            self._info_prefix, path
        )
        print(self._cache_found)

    def assert_GTF_path(self):

        self._assert_GTF_path = (
            "{}| No .csv found. Path (path to GTF) must be provided".format(
                self._info_prefix
            )
        )
        print(self._assert_GTF_path)

    def remember_paths(self, path):
        self._read_cache = "{}| Caching paths to {} for later reading".format(
            self._info_prefix, path
        )
        print(self._read_cache)
        
    def mk_csv_dir(self, path):
        
        self._mk_csv_dir = "{}| Making ref dir for .csv files: {}".format(self._info_prefix, path)
        print(self._mk_csv_dir)