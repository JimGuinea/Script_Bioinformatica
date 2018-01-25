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
go_split_new=''
output=[]
output_printable = ''
c1 = int(args.locus_tag)
c2 = int(args.data)

with open (output_file, 'w') as fo:
	with open(TSV_file, 'r') as fi:
		fi = csv.reader(fi, delimiter='\t')
		locus_tag_precedente = ''
		go_split_precedente = ''
		flag = False
		for line in fi:
			# ~ go_split_new = ''
			locus_tag = str(line[c1])
			go = str(line[c2])
			go_split = go.split('|')
			# ~ print('LOCUS TAG ', locus_tag)
			# ~ print('GO ', go)
			# ~ print('GO SPLITTED', go_split)
			if flag : #iterazioni successive
				if locus_tag == locus_tag_precedente : #condizione di uguaglianza tra due locus_tag successivi
					go_split_new=go_split + go_split_precedente #unisce gli elementi precedenti agli elementi attuali
					[output.append(item) for item in go_split_new if item not in output] #cerca tutti gli elementi della lista uguali e ne lascia solo 1
					output_printable='|'.join(output)
				else:
					print(locus_tag_precedente,'\t', output_printable, file=fo)
					print(locus_tag,'\t', go, file =fo) #<--------- perfetto
					flag = False
					# ~ go_split_precedente=''
			else: #prima iterazione
				locus_tag_precedente = locus_tag
				go_split_precedente = go_split
				flag = True
				output=[]
				# ~ print('LOCUS TAG PRECEDENTE', locus_tag_precedente)
			# ~ print('GO SPLIT NEW ', go_split_new)
			# ~ print('FLAG' ,flag)
			# ~ print('-------')
tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale
print('RUNNING')
print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')




