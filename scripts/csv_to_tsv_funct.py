
from argparse import ArgumentParser

#Make input argument
parser = ArgumentParser()
parser.add_argument('-i','--input', default = 'single-end-colliding-sample-ids.csv',
                    metavar = 'STRING',
                    type = str,
                    help = 'the input file of reads data')
#Initialize input argument as used variable
args = parser.parse_args()
inpt = args.input

#Function for search of starting table's line and experiment name
def start_search(filename):
    count = 0
    exp = 0
    infile = open(filename, 'r')
    line = infile.readline()
    while 'Data' not in line:
        count += 1
        if line.startswith('Experiment Name'):
            exp = line.rstrip().split(',')[1]
        line = infile.readline()
    count += 2
    return count, exp

#Function of fromats convertation:
def csv_tsv_converter(inpt):
    out = inpt.split('.')[0] + '.tsv'
    with open(inpt, 'r') as infile2, open(out,'w') as output:
        c, e = start_search(inpt)
        output.write('sample_id\tfastq_file\n')
        for line2 in infile2.readlines()[c:]:
            fastq = line2.rstrip().split(',')[0]
            index_id = line2.rstrip().split(',')[5]
            output.write(str(fastq) + '\t' + str(fastq) + '.' + str(exp) + '.' + str(index_id) + '.fastq.gz\n')
                                                                                                                        #Launch the script with argument
def main():
    csv_to_converter(inpt)
