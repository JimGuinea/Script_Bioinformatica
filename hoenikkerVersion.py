import os

query_file = "lista.txt"
sequences_file = "multifasta.txt"

with open(query_file, 'r') as file_query_input:
    lista_query = file_query_input.read().splitlines()

with open(sequences_file, 'r') as file_multiF_input:
    # print(lista_query)
    usefull_seq_flag = False #flag che indica quando un titolo utile è stato trovato
    seq_string = ""
    for line in file_multiF_input:
        line_to_check = line.strip()
        # print(line.strip() + " - ")
        #prima mi occupo della seq precedente, poi eventualmente della successiva
        if usefull_seq_flag:
            if line_to_check[0]==">":
                print("SEQ - " + seq_string)
                if line_to_check in lista_query:
                    usefull_seq_flag = True
                    print("TITLE " + line_to_check)
                else:
                    usefull_seq_flag = False
                seq_string = "" # ho terminato una sequenza
            else: #sto stampando una seq
                seq_string += line_to_check
        else: #not usefull_seq_flag
            if line_to_check in lista_query:
                print("TITLE " + line_to_check)
                usefull_seq_flag = True
                seq_string = ""
        # resta in sospeso un eventuale ultima sequenza
    if usefull_seq_flag:
        print("SEQ - " + seq_string)
