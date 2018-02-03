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

parser.add_argument('-i', '--input', help = 'inserire il file TSV di INPUT', metavar='')
parser.add_argument('-o', '--output', default = '_OUTPUT.CSV', help = 'inserire il file di OUTPUT', metavar='')
parser.add_argument('-d', '--divider', default = ',', help= 'divisore delle colonne per il ile CSV di OUTPUT (default= , )', metavar='')
parser.add_argument('-D', '--Divider', default = '|', help= 'divisore per i terms della seconda colonna (default = | )', metavar='')
parser.add_argument('-C', '--Character', default = ';', help = 'divisore delle colonne per file CSV di INPUT (default= ;)', metavar='') 
parser.add_argument('-s', '--single', action = "store_true" , help = 'opzione che fa stampare i term singolarmente, riga per riga')
args = parser.parse_args()


TSV_file = args.input
if args.output == "_OUTPUT.CSV":
	print(args.output)
	output_file = os.path.splitext(args.input)[0]+args.output #leva l'estensione dal file di input e crea il file di output come "file_di_input_OUTPUT.csv"
else:
	output_file =args.output

divider = args.divider
Divisor = args.Divider
char= args.Character
flag_single = args.single

output=[]
locus_tag_precedente = ''
go_out_list = []
line_merged = []

def list_to_string(lista):
	if len(lista) == 0:
		return ""
	return "|".join(map(str,lista))
	
def print_mtag(title, go_list):
	if flag_single:					#Se è attiva l'opzione "single" stampa singolarmente per ogni GO con il rispettivo LOCUS_TAG
		#~ print('flag_single TRUE')
		for elem in go_list:
			print(title+divider+elem, file=fo)
	else:
		print(title + divider + list_to_string(go_list), file=fo)

print('RUNNING')
flag_first = True

with open (output_file, 'w', newline = '') as fo, open(TSV_file, 'r') as fi:
	fi = csv.reader(fi, delimiter=char, quoting=csv.QUOTE_NONE)
	for line in fi:
		if flag_first:
			locus_tag_precedente = line[0]
			flag_first = False
		go_in_list = line[1].split(Divisor)
		if line[0] == locus_tag_precedente:
			for go in go_in_list:
				if go != '' and go not in go_out_list:
						go_out_list.append(go)
		else:
			# new locus_tag fond -> print the old one
			print_mtag(locus_tag_precedente, go_out_list) 
			go_out_list=[]
			locus_tag_precedente = line[0]
			for go in go_in_list:
				if go != '' and go not in go_out_list:
						go_out_list.append(go)
	# print last mtag	
	print_mtag(line[0], go_out_list) # better print asap in order to free memory

tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale

print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')




