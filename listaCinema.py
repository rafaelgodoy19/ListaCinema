lugares = int((input("Digite a quantidade de lugares: "))) #pede pro usuario escolher quantos lugares quer no cinema

cinema = [] #inicializando posicoes vazias

for i in range(lugares): #preenche as posicoes ignorando o 0 zero (iniciando com 1) ex: 1 a ...
    cinema.append(i+1)
print(cinema)

assento= int(input("\n\nEscolha um lugar disponivel: ")) #pede pro usuario escolher um lugar

#repeticao ate que todas as posicoes sejam preenchidas
while (cinema[i] == lugares):
   
    for i in range(lugares): #lendo os lugares e trocando o assento selecionado por 'X'
        if (assento == cinema[i]):
            cinema[i] = 'X'
            if cinema[i] == 'X':
                print (cinema)
       
    print("Assento",assento, "Reservado") #mostrando pro usuario que o assento esta Reservado
   
    print("\n", cinema) #mostra os lugares reservados e disponiveis para o usuario
    assento= int(input("Escolha um lugar disponivel: ")) #pede pro usuario escolher um lugar
   
print("\nCinema lotado! A sessao ira iniciar!") #Fim do programa