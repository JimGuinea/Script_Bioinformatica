#Script Madrid. Dato un file in input multifasta e un altro file con la lista di accession number o cmq nomi in formato fasta, ricerca nel primo file multifasta tutte le sequenze con i nomi presenti nel file "lista" e le riscrive in un file multifasta di output.

import argparse
import os
import itertools
import time

tempo_iniziale=time.time()


parser = argparse.ArgumentParser()
# ~ parser.add_argument('echo', help='echo la stringa che usi qua')
parser.add_argument('-i', '--input', help = 'inserire il file multifasta di input')
parser.add_argument('-L', '--List', help  = 'inserire il file lista dove sono presenti gli Accession Number da ricercare')
parser.add_argument('-l', '--list', help = 'inserire l\'Accession Number singolo da ricercare')
parser.add_argument('-o', '--output', help = 'inserire il file di output')
args = parser.parse_args()

#la differenza tra open() e with open e' che il secondo caso chiude automaticamente il file, mentre con open() poi bisogna fare close()

accN_esatto = str()
accN_successivo = str()
fp_elenco_input = args.List
sequenza = str()

#apri il file di Elenco e salvalo come lista_query
with open(fp_elenco_input, 'r') as file_query_input:  
	lista_query =file_query_input.readlines()
	lista_query = [elem.strip() for elem in lista_query]
	print ('Lista query: ',lista_query)

fp_multiF_input = args.input
fp_output = args.output 
print('ARGS OUTPUT' , args.output)
if fp_output == None :
	fp_output = 'output.fasta'
	
	
'''
with open(fp_elenco_input) as e1:  
	lista1 = []
	for query in e1:
		if query.startswith('>'):
			lista1.append(query) 	
'''

#apri il file Multifasta e salvalo in lista_multifasta

with open(fp_multiF_input, 'r') as file_multiF_input:
	file_cleaned = [word.replace('\n','') for word in file_multiF_input]
	fasta_completo =[]
	for v3 in file_cleaned:
		fasta_completo.append(v3)
	
	file_multiF_input.seek(0) #questo comando riporta il puntatore all'inizio del file
	 
	accessionN_multifasta = []
	for v2 in file_cleaned:
		if v2.startswith('>'):
			accessionN_multifasta.append(v2) #in accessionN_multifasta ci sono tutti gli accession Number del file multifasta
		
	
	print('Accession number mutlifasta: ',accessionN_multifasta)
	counter_accessionN = 0
	#~ counter_multiF = 0

	with open(fp_output, 'w') as file_output:
		for counter_accessionN, accessionN in enumerate(accessionN_multifasta):
			
			for query in lista_query:
				#~ counter_multiF +=1
				if query == accessionN : #condizione di uguaglianza tra query e accession number
					
					#~ accN_esatto = accessionN_multifasta[counter_accessionN+1]
					accN_index = fasta_completo.index(query)
					

					print('accN_index: ', accN_index)		#debug
					#~ print('accN_esatto: ', accN_esatto)  #debug
					
					#~ try:
					print('hello') #debug
					complete_seq=""
					print("COUNTE ACCESSION", counter_accessionN)
					print("LEN FASTA COMPLETO" , len(fasta_completo))
					
					if accN_index >= len(fasta_completo): #caso EOF
						for index in range(accN_index+1, fasta_completo[len(fasta_completo)]): #<-----E' qui il problema!
							complete_seq += fasta_completo[index]
						with open('debug.txt','a') as file_backup: print ('Nel caso EOF', file=file_backup)

					else:
						accN_successivo = accessionN_multifasta[counter_accessionN]
						accN_index_succ = fasta_completo.index(accN_successivo)
						for index in range(accN_index, accN_index_succ):
							complete_seq += fasta_completo[index]
						with open('debug.txt','a') as file_backup: print ('NON nel caso EOF', file=file_backup)

					
					print(query, file=file_output)			
					print(complete_seq, file=file_output)
					
					with open('debug.txt', 'a') as file_backup:
						print ('\nCounter accession Number: ',counter_accessionN, file=file_backup)	
						print ('Query: ',query, file=file_backup)
						print ('Output fasta: ', fasta_completo[accN_index], file=file_backup)
						print ('accN_index: ', accN_index, file=file_backup)
						print ('accN_index_successivo: ', accN_index_succ, file=file_backup)
						#~ print ('accN_esatto: ', accN_esatto, file= file_backup)
						print ('accN_successivo: ', accN_successivo, file= file_backup)
						print ('-------------------------', file=file_backup)

							
						'''
						fasta_sequenza_finale = []
						for v4 in fasta_completo:
							while accN_index != accN_index_succ:
								counter_accN_index = accN_index +1
								sequenza = fasta_sequenza_finale[accN_index]
								sequenza = fasta_sequenza_finale.append(counter_accN_inde)
								accN_index +=1
						print('Sequenza finale: ', sequenza, file=file_output)
						'''
					#~ except IndexError:
						#~ with open('debug.txt', 'a') as file_backup:
							#~ print('NELLA ECCEZIONE', file=file_backup)
							#~ print ("INDEX ERROR")
							#~ print ('\nCounter accession Number: ',counter_accessionN,  file=file_backup)	
							#~ print ('Query: ',query, file=file_backup)
							#~ print ('Output fasta: ', fasta_completo[accN_index], file=file_backup)
							#~ print('accN_index: ', accN_index, file=file_backup)
							#~ print('accN_index_successivo: ', accN_index_succ, file=file_backup)
							#~ #print('accN_esatto: ', accN_esatto, file= file_backup)
							#~ print('accN_successivo: ', accN_successivo, file= file_backup)
							
		#~ counter_accessionN -=1				
	with open('debug.txt','a') as file_backup:
		print ('-------------------------', file=file_backup)

tempo_finale=time.time()
tempo_esecuzione= tempo_finale-tempo_iniziale
print('Tempo di esecuzione: ', tempo_esecuzione, 'Seconds')
#~ with open('output.txt', 'a') as file_output:
	#~ print ('---------------------------------------------\n', file=file_output)
						
				

#NO print([e for e in id if e in '\n'.join(word)])


#https://www.dotnetperls.com/split-python per stampare array
#http://stackabuse.com/read-a-file-line-by-line-in-python/ leggere righe nel file
