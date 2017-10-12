# dNdS

Pipeline to identify dNdS ratios for <i> Mycobacterium tuberculosis H37Rv </i> and <i> Mycobacterium canettii </i> various strain orthologs

This method was utilised to generate dN values or relative values for the number of non-synonymous substitutions in MTB / STB orthologs to get an overview of gene divergence between the two species. 

<u><b>METHOD:</u></b>
Step 1. Extract DNA and protein sequences using dNdS_extract_seq.py
Step 2. Create directory for each gene and move DNA & protein sequences into directory
Step 3. Align protein sequences using needle
Step 4. Remove any gene that were not aligned
Step 5. Convert needle alignments to fasta alignments using needle2fasta.py
Step 6. Batch create .tree files needed for Codeml
Step 7. Run Codeml
Step 8. Extract each dN value using parse_dN_value.py
