"""

CLosure e funções que retornam outras funções

"""

def criar_saudação(saudação):
    def saudar(nome):
        return f'{saudação},{nome}!' 
    return saudar

falar_bom_dia = criar_saudação('Bom dia')
falar_bom_noite = criar_saudação('Bom noite')


print(falar_bom_dia('Luiz'))
print(falar_bom_noite('Luiz'))

