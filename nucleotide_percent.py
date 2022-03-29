import re, sys
from argparse import ArgumentParser

parser = ArgumentParser(description = "Computes the percentage of each nucleotide in a DNA or RNA sequence.")
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1: # In case the user executes just the script name, help show up
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper() #Makes seq uppercases

length= len(args.seq)

if 'U' in args.seq and 'T' in args.seq: #If the sequence has both 'U' and 'T'
        print("The sequence provided is ambiguous, pleas enter DNA or RNA sequence.")

#In the case of an RNA sequence:
elif 'U' in args.seq: #When it finds 'U' in the sequence saved in args.seq
        percent = {'A': 0, 'C': 0, 'G': 0, 'U': 0}
        for nt in args.seq:
                percent[nt] += 1
        for key in percent:
                percent[key] = 100*percent[key]/float(length) #Compute the percent through this formula
        print("Percentages are: ")
        print(percent) #Print the percent obtained

#In the case of a DNA sequence:
elif 'T' in args.seq: #When it finds 'T' in the sequence saved in args.seq
        percent = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nt in args.seq:
                percent[nt] += 1
        for key in percent:
                percent[key] = 100*percent[key]/float(length)
        print("Percentages are: ")
        print(percent) #Print the percent obtained
