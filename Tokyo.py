#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Tokyo.py
#  
#  Copyright 2018 Luca Malfatti <malfatti.luca.sky@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import argparse
import time
import csv 

tempo_iniziale = time.time()

parser = argparse.ArgumentParser(description='TLiMe: TSV Line Merger. Questo programma permette di unire tutti gli elementi appartenenti ad uno stesso locus tag in un file CSV')

parser.add_argument('-i', '--input', help = 'inserire il file TSV di input', metavar='')
parser.add_argument('-o', '--output', default = 'output.txt', help = 'inserire il file di output', metavar='')
parser.add_argument('-d', '--divider', default = ',', help= 'divisore delle colonne per il file CSV di output (default= , )', metavar='')
parser.add_argument('-D', '--Divider', default = '|', help= 'divisore per i terms della seconda colonna (default = | )', metavar='')
parser.add_argument('-C', '--Character', default = ';', help = 'divisore delle colonne per file CSV di input (default= ;)', metavar='') 
args = parser.parse_args()


TSV_file = args.input
output_file = args.output
divider = args.divider
Divisor = args.Divider
char= args.Character

output=[]
locus_tag_precedente = ''
term_precedente = []
line_merged = []

def list_to_string(lista):
	if len(lista) == 0:
		return ""
	return "|".join(map(str,lista))
	
def print_output(output):
	for row in output:
		print(row[0] + divider + list_to_string(row[1]), file=fo) # row1: [go1, go2, ..]

print('RUNNING')
flag_first = True
with open (output_file, 'w', newline = '') as fo, open(TSV_file, 'r') as fi:
	fi = csv.reader(fi, delimiter=char, quoting=csv.QUOTE_NONE)
	for line in fi:
		line[1] = line[1].split(Divisor)
		for go in line[1]:
			print("GO", go)
			if flag_first:
				locus_tag_precedente =line[0]
				flag_first = False
			if line[0] == locus_tag_precedente:
				if go != '':
					# print('LINE 1 ', line[1])
					# print('TERM 1 ', term_precedente)
					if go not in term_precedente:
						term_precedente.append(go)
			else:
				output.append([locus_tag_precedente, term_precedente])
				term_precedente=[]
				locus_tag_precedente = line[0]
				if go != '':
					if go not in term_precedente:
						term_precedente.append(go)
	#~ term_precedente = list(set(term_precedente))
	

	output.append([locus_tag_precedente, term_precedente])
	# print(output)
	print_output(output)

tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale

print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')




