def circular(fila_de_processos, quantum, tc):
    turn_around = [0] * len(fila_de_processos)  # vai receber o tempo_atual em que cada processo terminou a execucao

    trocasDeContexto = 0
    tempo_atual = 0  # tamanho da fatia executada + troca de contexto
    processo_que_executou_antes = 0
    while True:
        if sum(fila_de_processos) <= 0:
            print("Todos os processos foram executados!")
            break
        else:
            for i in range(len(fila_de_processos)):
                if fila_de_processos[i] <= 0:
                    # print(f"Processo P{i} terminou em T-{tempo_atual}")
                    print(f"P{i} ja Finalizado")
                elif fila_de_processos[i] <= quantum:
                    tempo_atual += fila_de_processos[i]
                    fila_de_processos[i] -= fila_de_processos[i]
                    print(f"P{i} executa")
                    print(f"Termino em T-{tempo_atual}")
                    if fila_de_processos[i] == 0:
                        turn_around[i] = tempo_atual
                        print(f"Processo P{i} terminou em T-{tempo_atual}")
                    elif fila_de_processos.count(0) > 0:
                        trocasDeContexto += 1
                        tempo_atual += tc
                else:
                    processo_que_executou_antes = i
                    tempo_atual += quantum
                    fila_de_processos[i] -= quantum
                    print(f"P{i} executa")
                    print(f"Termino em T-{tempo_atual}")
                    if fila_de_processos.count(0) > 0:
                        trocasDeContexto += 1
                        tempo_atual += tc
                    turn_around[i] = tempo_atual
            print("-"*30)

    print(f"Total de trocas de contexto> {trocasDeContexto}")
    print(f"tempo onde Terminou cada processo: {turn_around}")
    return turn_around

def tempo_atual_medio_turnaround(lista_de_processos, lista_de_tempos):
    resultado = sum(lista_de_tempos) / (len(lista_de_processos))
    print(f"Tempo Medio de Turnaround = {resultado}")


if __name__ == '__main__':
    fila_de_processos = [40, 20, 50, 30]
    # fila_de_processos = [40, 20]
    quantum = 20
    troca_contexto = 5
    turnAround = circular(fila_de_processos, quantum, troca_contexto)
    tempo_atual_medio_turnaround(fila_de_processos, turnAround)
