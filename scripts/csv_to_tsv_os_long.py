"""Scripts to parse .csv file of sequencing data to .tsv format
Need to include only: SAMPLE_ID and FASTQ_FILE,
where FASTQ_FILE: SAMPLE_ID.Experiment_Name.INDEX_ID.fastq.gz

Author: Sukhanova Xenia
"""

import os
import sys
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

#Function for experiment name search and description size estimation:
def start_search(filename):
    """Performs search of Experiment_Name and counts number of descriptive strings
    Parametres:
    filename: csv dataframe
        The .csv dataset which should be parsed

    Returns
    count: numeric
        number of lines before Data start
    exp: string
        Experiment Name
    """
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
    count += 3
    return count, exp

#Long script for file parsing with extended file creation:
def os_csv_tsv_convert_long(inpt, c, exp):
    """Performs file parsing and formatting
    Parametres:
    inpt: csv dataframe
        The .csv dataset which should be parsed

    Returns
    .tsv file with columns: sample_id, fastq_file,
    the name of input file is saved
    """
    
    # Step 2: parse and format with bash mode
    out_test = inpt.split('.')[0] + '.test.tsv'
    out = inpt.split('.')[0] + '.tsv'
    os.system('echo "sample_id\tfastq_file" > {0}'.format(out_test))
    cmd = """tail +{0} {1} | awk -F, -O\t '{{print $1,$1".{2}."$5".fastq.gz"}}' | cat {3} - > {4}""".format(c,inpt,exp,out_test,out)
    os.system(cmd)
    os.system(f"rm {out_test}")

# Main to execute code:
def main():
    c, exp = start_search(inpt)
    os_csv_tsv_convert_long(inpt, c, exp)

# Run scripts
if __name__ == "__main__":
    main()
