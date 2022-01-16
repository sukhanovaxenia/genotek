"""Scripts to parse .csv file of sequencing data to .tsv format
Need to include only: SAMPLE_ID and FASTQ_FILE,
where FASTQ_FILE: SAMPLE_ID.Experiment_Name.INDEX_ID.fastq.gz

Author: Sukhanova Xenia
"""

# imports 

from argparse import ArgumentParser
from urllib.request import urlopen

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
def csv_to_tsv_url(inpt):
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
    # Step 0: check if URL or not
    try:
        infile, infile2 = urlopen(inpt), urlopen(inpt)
        # Step 1: estimate description size and identify experiment name:
        for line in infile.readlines():
        if 'Data' not in line.decode('utf-8'):
            count += 1
            if 'Experiment Name' in line.decode('utf-8'):
                exp = line.rstrip().split(',')[1]
        else:
            count += 2
            break
        infile.close()
        # Step 2: Initialize output file and start parsing .csv
        out = inpt.split('.')[0] + '.tsv'
        with open(out,'w') as output:    
            output.write('sample_id\tfastq_file\n')
            for line2 in infile2.readlines()[count:]:
              line2 = line2.decode('utf-8')
              sample_id = line2.rstrip().split(',')[0]
              index_id = line2.rstrip().split(',')[5]
              output.write(str(sample_id) + '\t' + str(sample_id) + '.' + str(exp) + '.' + str(index_id) + '.fastq.gz\n')

    except ValueError:
        infile, infile2 = open(inpt, 'r'), open(inpt, 'r')
        # Step 1: estimate description size and identify experiment name:
        for line in infile.readlines():
            if 'Data' not in line:
                count += 1
            if 'Experiment Name' in line:
                exp = line.rstrip().split(',')[1]
        else:
            count += 2
            break
        infile.close()
        # Step 2: Initialize output file and start parsing .csv
        out = inpt.split('.')[0] + '.tsv'
        with open(out,'w') as output:    
            output.write('sample_id\tfastq_file\n')
            for line2 in infile2.readlines()[count:]:
                sample_id = line2.rstrip().split(',')[0]
                index_id = line2.rstrip().split(',')[5]
                output.write(str(sample_id) + '\t' + str(sample_id) + '.' + str(exp) + '.' + str(index_id) + '.fastq.gz\n')
    


# Main to execute code:
def main():
    csv_to_tsv_url(inpt)

# Run script
if __name__ == "__main__":
    main()
