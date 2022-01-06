

def _add_gtf_annotations_to_adata(adata, gtf_df, index_col="index", gene_id="gene_ids", chr_name="seqname"):

    """"""

    var_df = adata.var

    var_df = (
        var_df.rename({gene_id: "gene_id"}, axis=1)
        .reset_index()
        .rename({index_col: "gene_name"}, axis=1)
    )
    var_df = var_df.merge(gtf_df, on=["gene_name", "gene_id"], how="left").rename(
        {chr_name: "chr"}, axis=1
    )

    return var_df