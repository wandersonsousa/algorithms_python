class Entrada:
    quantidade_de_recursos = 3
    quantidade_de_processos = 5

    # coluna recurso alocados + qntd recurso disponível
    quantidade_total_de_cada_recurso = [10, 5, 7]

    matriz_de_recursos_ja_alocados = [ 
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]
    matriz_de_recursos_solicitados_por_cada_processo = [ # Max - qntd recurso alocado por processo
        [7, 4, 3],
        [1, 2, 2],
        [6, 0, 0],
        [0, 1, 1],
        [4, 10, 1]
    ]
