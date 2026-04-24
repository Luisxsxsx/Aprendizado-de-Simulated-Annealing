import Ponto2d as P
import random as Rd
import math

def simulated_annealing(pontos, t_inical, resfriamento):
    
    n = len(pontos)

    solucao_atual = list(range(n))
    custo_atual = func_avaliacao(pontos, solucao_atual)

    melhor_solucao = solucao_atual.copy()
    melhor_custo = custo_atual

    temperatura = t_inical
    temperatura_final = 0.05

    while(temperatura > temperatura_final):
        
        nova_solucao = trocar_vizinho(solucao_atual)
        novo_custo = func_avaliacao(pontos,nova_solucao)

        delta_e = novo_custo - custo_atual

        if delta_e < 0:
            solucao_atual = nova_solucao
            custo_atual = novo_custo

            if custo_atual < melhor_custo:
                melhor_solucao = solucao_atual.copy()
                melhor_custo = custo_atual

        else:
            prob = math.exp(-delta_e/temperatura)
            if Rd.random() < prob:
                solucao_atual = nova_solucao
                custo_atual = novo_custo

        temperatura *= resfriamento

    return melhor_solucao, melhor_custo


def trocar_vizinho(rota):

    vizinho = rota.copy()
    i = Rd.randint(1, len(rota)-1)
    j = Rd.randint(1, len(rota)-1)
    
    vizinho[i], vizinho[j] = vizinho[j], vizinho[i]

    return vizinho

def func_avaliacao(pontos, rota):
    dist_total = 0.0

    for i in range(len(rota)-1):
        ponto_atual = pontos[rota[i]]
        ponto_prox = pontos[rota[i+1]]
        dist_total +=ponto_atual.distance_to(ponto_prox)

    return dist_total



base = P.Ponto2d()
pontos_entrega = list()
pontos_entrega.append(base)

t_inicial = 100
resfriamento = 0.80

for i in range(10):
    ponto = P.Ponto2d(Rd.uniform(0.0,15.0),Rd.uniform(0.0,15.0))
    pontos_entrega.append(ponto)

solucao = simulated_annealing(pontos_entrega, t_inicial ,resfriamento)

print(f"Melhor rota encontrada entre pontos: {solucao[0]}\n")
print(f"Distancia calculada da rota: {solucao[1]:.2f}")

# print(f"Lista de pontos de entrega: {pontos_entrega}")