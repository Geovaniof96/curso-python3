# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 900,
}

#print(pessoa.keys())
pessoa.setdefault(  'lua',0)
print(pessoa.items()) #usado para trabalhar com a chave e com o valor, exemplo em for
#print(list(pessoa))

for chave,valor in pessoa.items():
    print(chave,valor)