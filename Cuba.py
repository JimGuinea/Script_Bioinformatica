#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cuba.py
#  
#  Copyright 2018 luca <luca@G580>
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

tempo_iniziale = time.time()

#sezione dei Parser
parser = argparse.ArgumentParser(description='Cercatore di sequenze in Multifasta')
# ~ parser.add_argument('echo', help='echo la stringa che usi qua')
parser.add_argument('-i', '--input', help = 'inserire il file multifasta di input')
parser.add_argument('-o', '--output', help = 'inserire il file di output')
args = parser.parse_args()

multi_fasta_file = args.input
output_file = args.output
#fine parse

with open(output_file, 'w') as fo:
	with open(multi_fasta_file, 'r') as mff:
		seq_string= ''
		for line in mff :
			line_to_check=line.strip()
			if line_to_check[0]=='>':
				print(line_to_check, file=fo)
			
tempo_finale=time.time()
tempo_esecuzione = tempo_finale - tempo_iniziale

print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')

	
