import argparse
import os
import random
import time 

def list_to_string(lista):
	if len(lista) == 0:
		return ""
	return "|".join(map(str,lista))

start_time = time.time()

parser = argparse.ArgumentParser(description='TGAM CSV GENERATOR')

parser.add_argument('-r', '--rows', default=100, help = 'Number of rows for output file', type=int)
parser.add_argument('-g', '--go', default=10, help = 'Max of random GO per row', type=int)
parser.add_argument('-o', '--output', default="auto_generated.csv", help = 'Output file name')

args = parser.parse_args()
rows = args.rows if args.rows < 100000000 and args.rows >= 0 else 100000000
gos = args.go if args.go < 100 and args.go >= 0 else 100
output_file = args.output
verbose = True
with open (output_file, 'w', newline = '') as fo:
    one_percent = rows/100
    if one_percent == 0:
        one_percent = 1
    for title in range(rows):
        if verbose:
            progress = title % one_percent
            if progress == 0: 
                print(str((int(title/one_percent))) + "%...")
        for num_title in range(0, 5): # num_title: number of occurrances of the same title
            num_go = random.randint(0, gos)
            go_list = []
            for x in range(num_go):
                go = random.randint(0,10000)
                go = '{0:05d}'.format(go)
                go_list.append("GO_"+ str(go))
            print("TGAM_"+'{num:0{width}}'.format(num=title, width=len(str(rows))) +";"+  list_to_string(go_list), file=fo)
            go_list = []
print(output_file + " generated in: " + str(time.time()-start_time) + " secs")