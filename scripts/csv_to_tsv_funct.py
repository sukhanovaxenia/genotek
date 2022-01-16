
#imports

from argparse import ArgumentParser

#Arguments

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
    # Parse file line by line till 'Data' pattern is met,
    # 'Data' - start point of information
    while 'Data' not in line:
        count += 1
        if line.startswith('Experiment Name'):
            exp = line.rstrip().split(',')[1]
        line = infile.readline()
    count += 2
    return count, exp

#Function of fromats convertation:
def csv_tsv_converter(inpt):

    # Initialize output file to write in it in parallel:
    out = inpt.split('.')[0] + '.tsv'
    with open(inpt, 'r') as infile2, open(out,'w') as output:
        # Step 1: call tart point and experiment name search function
        c, e = start_search(inpt)
        # Add header to ouput
        output.write('sample_id\tfastq_file\n')
        # Step 2: parse and format with base python
        for line2 in infile2.readlines()[c:]:
            fastq = line2.rstrip().split(',')[0]
            index_id = line2.rstrip().split(',')[5]
            output.write(str(fastq) + '\t' + str(fastq) + '.' + str(e) + '.' + str(index_id) + '.fastq.gz\n')


# Main to execute code:
def main():
    csv_tsv_converter(inpt)

# Run script
if __name__ == "__main__":
    main()
