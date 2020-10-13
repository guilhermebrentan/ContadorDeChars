arquivo = open('lorem.txt', 'r')
conteudo = arquivo.readlines()

arquivo = open('lorem.txt', 'r')
vogais = 0
espacos = 0
consoantes = 0

for line in arquivo:
    for char in line:
        if char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' or char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            vogais = vogais + 1
            
        if char == ' ':
            espacos = espacos+ 1
            
        else:
            consoantes = consoantes + 1
            
print("Numero de vogais: ", vogais, "|| Numero de espacos: ", espacos, "|| Numero de consoantes: ", consoantes)

texto = "Numero de vogais: ", vogais, "|| Numero de espacos: ", espacos, "|| Numero de consoantes: ", consoantes
conteudo.append(texto)

arquivo = open('lorem.txt', 'w')
arquivo.writelines(str(conteudo))
arquivo.close
    