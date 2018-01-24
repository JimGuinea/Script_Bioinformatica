<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Palermo_debug.py
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
<<<<<<< HEAD
=======
=======
#title           :Palermo.py
#description     :Dato un file multifasta e una lista di Accession Number in formasto fasta, lo script cerca tutte le sequenze della lista nel MultiFasta e le scrive in un secondo file MultiFasta
#author          :Luca M. e Luca P.
#date            :20180123
#version         :1.0
#usage           :
#notes           :
#python_version  :3.6.0 
#==============================================================================
>>>>>>> 1b854d24b63e12ed6506cb18cbd2f39d853b25b2
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355

import os
import argparse
import time

tempo_iniziale = time.time()

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
parser = argparse.ArgumentParser(description='Cercatore di sequenze in Multifasta')
# ~ parser.add_argument('echo', help='echo la stringa che usi qua')
parser.add_argument('-i', '--input', help = 'inserire il file multifasta di input')
parser.add_argument('-L', '--List', help  = 'inserire il file lista dove sono presenti gli Accession Number da ricercare')
parser.add_argument('-l', '--list', help = 'inserire l\'Accession Number singolo da ricercare')
parser.add_argument('-o', '--output', help = 'inserire il file di output')
<<<<<<< HEAD
=======
=======

parser = argparse.ArgumentParser(description = 'Script for searching Accession Number in a Multifasta file')
parser.add_argument('-i', '--input', metavar='', help = 'file multifasta di input')
parser.add_argument('-L', '--List', metavar='', help  = 'file lista dove sono presenti gli Accession Number da ricercare')
parser.add_argument('-o', '--output', metavar='', help = 'nome del file di output')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')
>>>>>>> 1b854d24b63e12ed6506cb18cbd2f39d853b25b2
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
args = parser.parse_args()

query_file = args.List
sequences_file = args.input
output_file = args.output

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
with open(output_file, 'w') as fo:

	with open(query_file, 'r') as file_query_input:   		#apre il file delle Query
		lista_query = file_query_input.read().splitlines() #salva tutte le righe in una lista chiamata "lista_query"

	with open(sequences_file, 'r') as file_multiF_input: 	#apre il file delle sequenze da analizzare
		#~ print('LISTA QUERY',  lista_query)					#DEBUG
		#~ print(' FILE MULTIF INPUT ', file_multiF_input) 	#DEBUG
<<<<<<< HEAD
=======
=======

with open(output_file, 'w') as fo:

	with open(query_file, 'r') as file_query_input:		   #apre il file delle Query
		lista_query = file_query_input.read().splitlines() #salva tutte le righe in una lista chiamata "lista_query"

	with open(sequences_file, 'r') as file_multiF_input: 	#apre il file delle sequenze da analizzare
		print('LISTA QUERY',  lista_query)					#DEBUG
		print(' FILE MULTIF INPUT ', file_multiF_input) 	#DEBUG
>>>>>>> 1b854d24b63e12ed6506cb18cbd2f39d853b25b2
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
		usefull_seq_flag = False							#flag che indica quando un titolo utile è stato trovato
		seq_string = "" 									#Stringa dove metterci la stringa da stampare alla fine
		for line in file_multiF_input: 						#ciclo che passa tutte le righe nel file multifasta (>nomi e sequenze)
			line_to_check = line.strip() 					#la funzione .strip() rimuove tutti gli spazi vuoti in una stringa
			#print('LINE ', line) 							#DEBUG
			#print(line.strip() + " - ") 					#DEBUG
															#prima mi occupo della seq precedente, poi eventualmente della successiva
			if usefull_seq_flag: 							#IF di tutte le stringhe che mi interessano, TITOLI o SEQUENZE. se la bandierina è Vera (la prima volta è falsa di default)
				if line_to_check[0]==">": 					#se la linea del file multifasta inizia con > 
					print(seq_string, file=fo) 
					if line_to_check in lista_query: 		#if X in Y è vero se X è in Y, se la linea della lista query (che in questo caso è un titolo perchè inizai con > è uguale alla linea della lista delle query (che sono tutti titoli >)
						usefull_seq_flag = True 			#metti la bandierina Vera, ovvero un titolo utile è stato trovato
						print(line_to_check, file= fo) 	#stampa il titolo
					else: 									#la linea che ho trovato non è un titolo, ma una sequenza
						usefull_seq_flag = False 			#un titolo utile NON è stato trovato
					seq_string = ""							# ho terminato una sequenza
				else: 										#sto stampando una seq. La linea che ho trovato NON è un titolo, ma una sequenza
					seq_string += line_to_check 			#aggiunge alla stringa da stampare la sequenza, perchè è utile ma non è un titolo
			else: 											#not usefull_seq_flag
				if line_to_check in lista_query: 			#se la linea nel multifasta è uguale alla query
					print(line_to_check, file=fo) 
<<<<<<< HEAD
					#~ print("TITLE " + line_to_check) 		#stampa la linea del multifasta 
=======
<<<<<<< HEAD
					#~ print("TITLE " + line_to_check) 		#stampa la linea del multifasta 
=======
					print("TITLE " + line_to_check) 		#stampa la linea del multifasta 
>>>>>>> 1b854d24b63e12ed6506cb18cbd2f39d853b25b2
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
					usefull_seq_flag = True 				#bandierina True
					seq_string = "" 
	if usefull_seq_flag:
		print(seq_string, file=fo)

tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale
<<<<<<< HEAD
print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')
=======
<<<<<<< HEAD
print('Tempo di esecuzione: ', tempo_esecuzione, 'secondi')
=======
print('Tempo di esecuzione: ', tempo_esecuzione, 'Seconds')
>>>>>>> 1b854d24b63e12ed6506cb18cbd2f39d853b25b2
>>>>>>> 6b1bd3b276f2e5850b3b5d548a80be9147200355
