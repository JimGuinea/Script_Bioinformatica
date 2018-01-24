#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Tokio.py
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
args = parser.parse_args()

TSV_file = args.input
output_file = args.output
go_split_new=''
output=[]
go_split_output=[]

with open (output_file, 'w') as fo:
	with open(TSV_file, 'r') as fi:
		fi = csv.reader(fi, delimiter='\t')
		# ~ fo = csv.writer(fo)
		locus_tag_precedente = ''
		go_split_precedente = ''
		flag = False
		for line in fi:
			# ~ go_split_new = ''
			locus_tag = str(line[0])
			# ~ locus_tag = list(enumerate(locus_tag, 1))
			go = str(line[1])
			go_split = go.split('|')
			print('LOCUS TAG ', locus_tag)
			# ~ print('GO ', go)
			# ~ print('GO SPLITTED', go_split)
			
			if flag : #iterazioni successive
				
				if locus_tag == locus_tag_precedente :
					go_split_new='' #condizione di uguaglianza tra due locus_tag successivi
					go_split_new=go_split + go_split_precedente
					go_split_output = [output.append(item) for item in go_split_new if item not in output]
					print('GO SPLIT NEW ', go_split_new)
					print(locus_tag,'\t', output, file=fo)
				else:
					print(locus_tag,'\t', go, file=fo)
					flag = False
			else: #prima iterazione
				locus_tag_precedente = locus_tag
				go_split_precedente = go_split
				flag = True
				print('LOCUS TAG PRECEDENTE', locus_tag_precedente)
			print('FLAG' ,flag)
			print('-------')





