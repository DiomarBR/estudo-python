from datetime import date
atual = date.today().year
ano = int(input("Ano de nascimento:"))
idade = atual - ano
print("Quem nasceu {} tem {} anos em {}.".format(ano, idade, atual))
if idade == 18:
    print("Voce tem que se alistar imediatemente:")
elif idade < 18:
    tempo = 18 - idade
    print("Ainda faltam {} anos para o alistamento.".format(tempo))
else:
    tempo = idade - 18
    print("Voce ja deveria ter se alistado há {}".format(tempo))