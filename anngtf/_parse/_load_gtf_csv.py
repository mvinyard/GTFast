
import os
import pandas as pd

def _read_gtf_path_file(GTF_csv_path, genes):
    
    """"""
    
    GTFPathDict = {}
    paths = ['gtf_path', 'gtf_csv_path', 'gene_gtf_csv_path']
    
    with open(GTF_csv_path, "r") as f:
        for n, line in enumerate(f.readlines()):
            GTFPathDict[paths[n]] = line.strip("\n")

    if genes:
        return pd.read_csv(GTFPathDict['gene_gtf_csv_path'], index_col=0)

    else:
        return pd.read_csv(GTFPathDict['gtf_csv_path'], index_col=0)
    
def _load_gtf_csv(genes=False, path=False):
    
    GTF_csv_path = os.path.join(os.path.dirname(__file__), "GTF_paths.txt")
        
    if os.path.exists(GTF_csv_path):
        return _read_gtf_path_file(GTF_csv_path, genes)
        
    else:
        assert path, "path (path to GTF) must be provided"
        from ._parse_gtf_to_csv import _parse_gtf_to_csv
        return _parse_gtf_to_csv(path, genes=genes, force=False, return_gtf=True)