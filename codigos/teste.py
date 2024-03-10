def cria_multiplicador(multiplicador):
    def multiplica(numero):
         return numero * multiplicador
    return multiplica



dobro = cria_multiplicador(2)

print(dobro(2))