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

parser = argparse.ArgumentParser(description='TLiMe: TSV Line Merger')
parser.add_argument('-i', '--input', help = 'inserire il file TSV di input')
parser.add_argument('-o', '--output', default = 'output.txt', help = 'inserire il file di output')
#~ parser.add_argument('-C', '--locus_tag', default = 0, help ='inserire la colonna dei Locus Tag (PRIMA COLONNA = 0), di default PRIMA COLONNA (=0)')
#~ parser.add_argument('-c', '--data', default = 1, help='inserire la colonna deid ati da ordinare (PRIMA COLONNA = 0), di default SECONDA COLONNA (=1)')
args = parser.parse_args()

TSV_file = args.input
output_file = args.output
output=[]
locus_tag_precedente = ''
term_precedente = []
line_merged = []
# ~ print('LOCUS TAG PRECEDENTE', locus_tag_precedente)
# ~ print('TERM PRECEDENTE', term_precedente)
#~ c1 = int(args.locus_tag)
#~ c2 = int(args.data)

def list_to_string(lista):
	outString=[]
	outString2=[]
	str1=''
	# ~ flag =False
	for elem in lista:
		outString.append(elem)
		outString2 = [sublist for sublist in outString if any(sublist)] #ripulisce le sottoliste vuote contenute in una lista
		# ~ print (outString2)
		# ~ outString[:] = [item for item in outString if item != '']
		str1='|'.join(str(r) for v in outString2 for r in v)
		# ~ print(str1)
	return str1
	
def print_output(output):
	for row in output:
		print(row[0],';',list_to_string(row[1]), file=fo)


flag_first = True
with open (output_file, 'w', newline = '') as fo:
	with open(TSV_file, 'r') as fi:
		fi = csv.reader(fi, delimiter=';', quoting=csv.QUOTE_NONE)
		for line in fi:
			line[1] = line[1].split('|')
			# ~ line[1] = [i for i in line[1] if i != '']
			# ~ for i in line[1]:
				# ~ line_merged += i

			if flag_first:
				locus_tag_precedente =line[0]
				flag_first = False
			if line[0] == locus_tag_precedente:
				if line[1] != '':
					# ~ print(line[1])
					if not line[1] in term_precedente:
						# ~ term_precedente = line[1].split('|')
						term_precedente.append(line[1])
						# ~ print(term_precedente)

						# ~ term_precedente = '|'.join(line[1])
						# ~ print(term_precedente)
			else:
				output.append([locus_tag_precedente, term_precedente])
				term_precedente=[]
				locus_tag_precedente = line[0]
				if line[1] != '':
					if not line[1] in term_precedente:
						term_precedente.append(line[1])
		output.append([locus_tag_precedente, term_precedente])
		print_output(output)

tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale
print('RUNNING')
print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')




