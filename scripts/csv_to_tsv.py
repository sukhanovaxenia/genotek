"""Scripts to parse .csv file of sequencing data to .tsv format
Need to include only: SAMPLE_ID and FASTQ_FILE,
where FASTQ_FILE: SAMPLE_ID.Experiment_Name.INDEX_ID.fastq.gz

Author: Sukhanova Xenia
"""

# imports 

from argparse import ArgumentParser

# Argument
parser = ArgumentParser()
parser.add_argument('-i','--input', const = 'single-end-colliding-sample-ids.csv',
                    metavar = 'STRING',
                    type = str,
                    nargs = '?',
                    help = 'the input file of reads data')
# Initialize input argument as used variable
args = parser.parse_args()
inpt = args.input

#Set the counter and experiment name var:
def csv_to_tsv(inpt):
    """Performs description estimation,
    Experiment name search,
    file parsing and fomatting
    
    Parameters
    inpt: csv dataframe
        The .csv dataset to parse

    Returns
    .tsv file with columns: sample_id, fastq_file,
    the name of input file is saved
    """

    count = 0
    exp = 0
    # Step 1: define number of description lines and the experiment name
    with open(inpt, 'r') as infile:
        for line in infile.readlines():
            if 'Data' not in line:
                count += 1
                if 'Experiment Name' in line:
                    exp = line.rstrip().split(',')[1]
            else:
                count += 2
                break
    # Step 2: Initialize output file and start parsing .csv
    out = inpt.split('.')[0] + '.tsv'
    with open(inpt, 'r') as infile2, open(out,'w') as output:    
        output.write('sample_id\tfastq_file\n')
        for line2 in infile2.readlines()[count:]:
            sample_id = line2.rstrip().split(',')[0]
            index_id = line2.rstrip().split(',')[5]
            output.write(str(sample_id) + '\t' + str(sample_id) + '.' + str(exp) + '.' + str(index_id) + '.fastq.gz\n')


# Main to execute code:
def main():
    csv_to_tsv(inpt)

# Run script
if __name__ == "__main__":
    main()
