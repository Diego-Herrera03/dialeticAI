from random import randint
import matplotlib as plt
#plano geral do código


#definição da quantidade pesos
#definição dos pesos
#avaliação
#alteração dos pesos baseada na avaliação
#Reprodução
#repetição, repetição, repetição...
#+/- resultado perfeito

#AVISO PARA EU LER DEPOIS: debuggar e expandir a ideia, adicionar mais pesos, adicionar mais funções, adicionar mais ciclos de avaliação, alteração e reprodução dos pesos

#Avaliação dos pesos, a função avaluate é a função que vai avaliar os pesos pela distância entre o peso e a meta
def avaluate(weights, objective):
    for i in weights:
        #se a diferença for maior que 0
        if  objective - i[0] >= 0:
            #A avaliação é igual a diferença
            i[1] = float(objective - i[0])

        #se a diferença for menor que 0
        else:
            i[1] = -float(objective - i[0])

#Função que vai alterar os pesos, a função gen_alter é a função que vai alterar os pesos aleatoriamente
def gen_alter(weights):
    for i in range(0, len(weights)):
        if randint(0, 1) == 1:
            weights[i][0] += 0.01

        else:
            weights[i][0] -= 0.01

#Função que vai aprimorar os pesos, a função gen_reproduce é a função que vai aprimorar os pesos pela distância entre os pesos e a meta
def gen_reproduce(weights):
    weights.sort(key = lambda x: x[1])
    
    coin = randint(0, 1)

    fathers = [weights[0], weights[1]]
    mothers = [weights[2], weights[3]]

    #Aprimorando os pesos de acordo com os pesos dos pais e mães, aprimoramento estável e seguro, mantém a qualidade dos pesos
    weights[0][0] = (fathers[0][0] + mothers[0][0]) / 2
    weights[1][0] = (fathers[1][0] + mothers[1][0]) / 2
    weights[2][0] = (fathers[0][0] + mothers[1][0]) / 2
    weights[3][0] = (fathers[1][0] + mothers[0][0]) / 2

    #Aprimorando os pesos de acordo com os pesos dos pais e mães, aprimoramento instável e arriscado para o aumento dos pesos
    if coin == 1:
        weights[4][0] = (fathers[0][0] + mothers[0][0]) * 2
        weights[5][0] = (fathers[1][0] + mothers[1][0]) * 2.2
        weights[6][0] = (fathers[0][0] + mothers[1][0]) * 2.3
        weights[7][0] = (fathers[1][0] + mothers[0][0]) * 2.4
        
        weights[8][0] = (fathers[0][0] + mothers[0][0]) * 3
        weights[9][0] = (fathers[1][0] + mothers[1][0]) * 3.2
        weights[10][0] = (fathers[0][0] + mothers[1][0]) * 3.3
        weights[11][0] = (fathers[1][0] + mothers[0][0]) * 3.4
        
        weights[12][0] = (fathers[0][0] + mothers[0][0]) * 4
        weights[13][0] = (fathers[1][0] + mothers[1][0]) * 4.1
        weights[14][0] = (fathers[0][0] + mothers[1][0]) * 4.2
        weights[15][0] = (fathers[1][0] + mothers[0][0]) * 4.3

    #Aprimorando os pesos de acordo com os pesos dos pais e mães, aprimoramento instável e arriscado para a diminuição dos pesos
    else:
        weights[4][0] = (fathers[0][0] + mothers[0][0]) / 2
        weights[5][0] = (fathers[1][0] + mothers[1][0]) / 2.2
        weights[6][0] = (fathers[0][0] + mothers[1][0]) / 2.3
        weights[7][0] = (fathers[1][0] + mothers[0][0]) / 2.4
        
        weights[8][0] = (fathers[0][0] + mothers[0][0]) / 2.5
        weights[9][0] = (fathers[1][0] + mothers[1][0]) / 2.6
        weights[10][0] = (fathers[0][0] + mothers[1][0]) / 2.7
        weights[11][0] = (fathers[1][0] + mothers[0][0]) / 2.9
        
        weights[12][0] = (fathers[0][0] + mothers[0][0]) / 3
        weights[13][0] = (fathers[1][0] + mothers[1][0]) / 3.1
        weights[14][0] = (fathers[0][0] + mothers[1][0]) / 3.2
        weights[15][0] = (fathers[1][0] + mothers[0][0]) / 3.3

    return weights[0]

def show(weights):
    for i in weights:
        print("{0:10f} {1:10f}".format(i[0], i[1]))


objective = int(input("objective: "))

weights = [[float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)],
           [float(randint(0, 1000)), float(0)]]

rounds = int(input("rounds: "))
rounds += 1

results = []
best = []

for i in range(0, rounds):
    print("Ciclo: ", i, "\n\n")

    #Avaliação dos pesos
    avaluate(weights, objective)

    #Alteração dos pesos aleatoriamente
    gen_alter(weights)

    #Aprimoramento dos pesos
    best = gen_reproduce(weights)
    results.append(best[0])
    
    #Exibição dos pesos
    show(weights)

    print("\n\n")

print("\n\n")

plt.plot(results)#= array pluridimensional???
plt.ylabel("melhores indivíduos")
plt.show()
