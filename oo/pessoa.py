class Pessoa:
    def __init__(self, *filhos, nome=None, idade=25):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    barth = Pessoa(nome='Barth')
    joao = Pessoa(barth, nome='João')
    print(Pessoa.cumprimentar(joao))
    print(id(joao))
    print(joao.cumprimentar())
    print(joao.nome)
    print(joao.idade)
    for filho in joao.filhos:
        print(filho.nome)
