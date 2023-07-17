numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

carros2= {"palio", "gol", "celta", "palio"}
print(f' Este é o carros {carros2}')
for indice,carro in enumerate(carros2):
    print(f' carro - {indice} {carro}')

lista_carro = list(carros2)

print(lista_carro[2])