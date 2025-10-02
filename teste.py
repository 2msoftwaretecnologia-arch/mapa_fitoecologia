posicoes = [
    ("23,2921","1,876","0,9878","0,3125"),
    ("27,8184","1,8989","0,8466","0,3125")
]

informacoes = ["teste1", "teste2"]

for coords, info in zip(posicoes, informacoes):
    print("Coordenadas:", coords[0])
    print("Informação:", info)
    print("---")
