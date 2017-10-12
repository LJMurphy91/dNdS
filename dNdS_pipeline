#GENERATE dNdS RATIOS AND dN VALUES FOR MTB / STB ORTHOLOGS
#PIPELINE USES NEEDLE, PAL2NAL, CODEML AND PYTHON SCRIPTS

#GENE AND PROTEIN SEQUENCES WERE EXTRACTED FROM MTB H37RV AND STB-A/D/J/K AND L GENBANK FILES USING dNdS_extract_seq.py

#SCRIPT NEEDS GENBANK FILES, LIST OF GENES OF INTEREST AND LIST OF ORTHOLOGS
#FILE1 - recomb_genes.txt --> recombination genes
#FILE2 - repair_genes.txt --> repair genes
#FILE3 - tr_genes.txt --> transcription regulator genes
#FILE4 - mtb_stb_orthologues.txt --> matrix of MTB / STB orthologs
#FILES5-8 - DNA and protein sequences

#Takes users input as files and asks whether user wants DNA or protein sequences.
#Uses the ortholog files to determine MTB / STB orthologs
#Produces files in the format <locus_tag_n1.txt, locus_tag_n2.txt, locus_tag_p1.txt, locus_tag_p2.txt

#########################################################################################################

#1. CREATE DIRECTORY FOR EACH GENE AND MOVE SEQUENCE FILES - FOLDERS START WITH Rv

for file1 in *_n1.txt; do file2=${i//1/2}; folder=${file1//\_n1.txt/}; mkdir $folder; mv $file1; mv $file2 $folder; done

for file1 in *_p1.txt; do fils2=${i//1/2}; folder=${file1//\_p1.txt/}; mv $file1; mv $file2 $folder; done

#########################################################################################################

#2. ALIGN PROTEIN SEQUENCES USING NEEDLE AND REMOVE ANY EMPTY FILES I.E. ANY FILES THAT #WERE NOT ALIGNED
#2A. CONVERT NEEDLE ALIGNMENTS TO FASTA ALIGNMENTS with needle2fasta.py

for proteinFile1 in */*p1.txt; do proteinFile2=${proteinFile1//p1/p2}; yes "" | needle $proteinFile1 $proteinFile2 -gapopen 10.0 -gapextend 0.5; done

for needleFile in *.needle; do folder=${needleFile//.needle/}; folder2=${folder//r/R}; mv needleFile $folder2; done

for folders in Rv*; do edit=${i//}needle=$i.needle; new_needle=${needle//R/r}; if ! [ -e $i/$new_needle ]; then echo "removing " $i; rm -r $i; fi; done

for i in Rv*/*.needle; do python needle2fasta.py $i; done

#########################################################################################################

#3. CONVERT PROTEIN TO DNA ALIGNMENTS

for i in Rv*/*.fasta; do aln=$i; nuc0=${aln//r/R}; nuc1=${nuc0//.fasta/_n1.txt}; nuc2=${nuc0//.fasta/_n2.txt}; perl ~/SNPS_project/pal2nal/pal2nal.pl $aln $nuc1 $nuc2 -output fasta -nogap > $aln.codon; done

#########################################################################################################

#4. BATCH CREATE TREE FILES FOR CODEML

for i in rv*/*.clustal; do python batch_edit.py $i ../../pal2nal/for_paml/test.cnt Rv*/*_n2.txt; done
for i in Rv*/*.codon; do python batch_edit.py $i ../../pal2nal/for_paml/test.cnt Rv*/*_n2.txt; done

#########################################################################################################

#5. RUN CODEML

for i in *.tree; do f=${i//.tree/}; folder=${f//r/R} mv $i $folder; done
for i in rv*; do cd $i; i0=${i//R/r} f=$i0.cnt; codeml $f; cd ../; done

#########################################################################################################

#6. EXTRACT dN VALUES FOR EACH MTB / STB ORTHOLOG

for i in Rv*/*.codeml; do f=${i//codeml/needle} python dn.py $i $f; done 



