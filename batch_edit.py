from sys import argv

codon_file = argv[1]
sp_codon_file = codon_file.split('/')
cnt_name = codon_file.replace('.clustal.codon', '')
sp_cnt_name = cnt_name.split('/')
file_name = sp_cnt_name[1]

cnt_file = open(argv[2],'rU')

this_tree_file = argv[3]
for_tree_file = open(this_tree_file, 'rU')

new_cnt_file = open(cnt_name+'.cnt', 'a')

tree_file = open(file_name+'.tree', 'a')


for stuff in for_tree_file:
	if stuff.startswith('>'):
		gene = stuff.replace('>', '')
		tree_file.write('(' + file_name + ',' + gene + ');')

for lines in cnt_file:
    if 'seqfile' in lines:
        newline = lines.replace('test.codon', sp_codon_file[1])
        new_cnt_file.write(str(newline))
    elif 'outfile' in lines:
        outline = lines.replace('test.codeml', file_name+'.codeml')
        new_cnt_file.write(str(outline))
    elif 'treefile' in lines:
    	treeline = lines.replace('test.tree', file_name+'.tree')
    	new_cnt_file.write(str(treeline))
    elif 'model' in lines:
	    modelline = lines.replace('2', '0')
	    new_cnt_file.write(str(modelline))
    else:
    	all_lines = lines
        new_cnt_file.write(str(all_lines))

