
from argparse import ArgumentParser

#Make input argument
parser = ArgumentParser()
parser.add_argument('-i','--input', const = 'single-end-colliding-sample-ids.csv',
                    metavar = 'STRING',
                    type = str,
                    nargs = '?',
                    help = 'the input file of reads data')
#Initialize input argument as used variable
args = parser.parse_args()
inpt = args.input

#Set the counter and experiment name var:
count = 0
exp = 0
#Define number of description lines and the experiment name
with open(inpt, 'r') as infile:
    for line in infile.readlines():
        if 'Data' not in line:
            count += 1
            if 'Experiment Name' in line:
                exp = line.rstrip().split(',')[1]
        else:
            count += 2
            break
#Initialize output file and start parsing .csv
out = inpt.split('.')[0] + '.tsv'
with open(inpt, 'r') as infile2, open(out,'w') as output:    
    output.write('sample_id\tfastq_file\n')
    for line2 in infile2.readlines()[count:]:
        sample_id = line2.rstrip().split(',')[0]
        index_id = line2.rstrip().split(',')[5]
        output.write(str(sample_id) + '\t' + str(sample_id) + '.' + str(exp) + '.' + str(index_id) + '.fastq.gz\n')
