
__module_name__ = "_add_GTF_annotations_to_adata.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


def _add_GTF_annotations_to_adata(adata, GTF_df, index_col="index", gene_id="gene_ids", chr_key="seqname"):

    """
    Add GTF annotations to an adata object.
    
    Parameters:
    -----------
    adata
        AnnData object for single-cell data.
        type: anndata.adata
    
    GTF_df
        DataFrame of a GTF file.
        type: pandas.DataFrame
        
    index_col
        type: str
    
    gene_id
        key for gene_ids
        type: str
    
    chr_key
        key for Chromosomes
        type: str
        
    Returns:
    --------
    adata.var dataframe
        type: pandas.DataFrame
    """

    var_df = adata.var

    var_df = (
        var_df.rename({gene_id: "gene_id"}, axis=1)
        .reset_index()
        .rename({index_col: "gene_name"}, axis=1)
    )
    var_df = var_df.merge(GTF_df, on=["gene_name", "gene_id"], how="left").rename(
        {chr_key: "chr"}, axis=1
    )

    return var_df