import os
import warnings

import gtfparse
import pandas as pd
import pydk


warnings.filterwarnings("ignore")


def _create_gtf_csv_dir(path):

    """"""

    gtf_dir = os.path.dirname(path)
    csv_dir = os.path.join(gtf_dir, "csv")
    pydk.mkdir_flex(csv_dir)

    return gtf_dir, csv_dir

def _remember_gtf_csv_paths(gtf_path, gtf_csv_path, gene_gtf_csv_path):
    
    """"""
    
    GTF_paths = os.path.join(os.path.dirname(__file__), "GTF_paths.txt")
    with open(GTF_paths, "w") as f:
        f.write(gtf_path + "\n")
        f.write(gtf_csv_path + "\n")
        f.write(gene_gtf_csv_path + "\n")
        f.close()

class _FractionatedGTF:
    def __init__(self, path, write_csv=True):

        """
        Convert a .gtf file to a .csv file for much faster subsequent parsing with pandas.

        Parameters:
        -----------
        path
            path to GTF file.

        Notes:
        ------
        (1) Developed with the 10x cellranger-arc refdata.

        """
        
        self._gtf_path = path
        self._gtf_dir, self._csv_dir = _create_gtf_csv_dir(path)
        self._gtf_csv_path = os.path.join(self._csv_dir, "gtf.csv")
        self._gene_gtf_csv_path = os.path.join(self._csv_dir, "gtf.genes.csv")
        
        self._gene_columns_to_keep = [
            "seqname",
            "source",
            "feature",
            "start",
            "end",
            "strand",
            "frame",
            "gene_id",
            "gene_version",
            "gene_type",
            "gene_name",
            "level",
            "hgnc_id",
            "tag",
            "havana_gene",
        ]
    
    def parse_gtf(self, write_csv=True):
        
        """"""
        
        self._gtf = gtfparse.read_gtf(self._gtf_path)
        
        if write_csv:
            self._gtf.to_csv(self._gtf_csv_path)
    
    def parse_genes(self, write_csv=True):

        """"""

        
        self._gene_gtf = self._gtf.loc[self._gtf["feature"] == "gene"][
            self._gene_columns_to_keep
        ]
        
        if write_csv:
            self._gene_gtf.to_csv(self._gene_gtf_csv_path)
            del self._gtf
            del self._gene_gtf
    
    def remember(self):
        
        _remember_gtf_csv_paths(self._gtf_path, self._gtf_csv_path, self._gene_gtf_csv_path)
    
    def read_gtf_csv(self, genes):
        
        """ """
        
        if genes:
            return pd.read_csv(self._gene_gtf_csv_path, index_col=0)
        else:
            return pd.read_csv(self._gtf_csv_path, index_col=0)

def _parse_gtf_to_csv(path, genes=False, force=False, return_gtf=False):

    """"""
    
    gtf_ = _FractionatedGTF(path)
    
    if not os.path.exists(gtf_._gtf_csv_path) or not os.path.exists(gtf_._gene_gtf_csv_path) or force:
        gtf_.parse_gtf()
        gtf_.parse_genes()
        gtf_.remember()
    
    if return_gtf:
        return gtf_.read_gtf_csv(genes)
