#Import libraries
import sys, re
from argparse import ArgumentParser

#Manage possible inputs on the comand line
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
#Get variables and uppercase seq variable
args = parser.parse_args()
args.seq = args.seq.upper()                

#Check sequence and classify it
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA either RNA')
else:
    print ('The sequence is not DNA nor RNA')

#If motif entered, looks for it
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print(f'The motif {arg.motif} is found in the input sequence')
    else:
        print(f'The motif {arg.motif} is not found in the input sequence')
