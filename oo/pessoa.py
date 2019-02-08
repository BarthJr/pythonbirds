class Pessoa:
    olhos = 2
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
    joao.sobrenome = 'Barth'
    del joao.filhos
    joao.olhos = 1
    print(barth.__dict__)
    print(joao.__dict__)
    Pessoa.olhos = 1
    print(Pessoa.olhos)
    print(barth.olhos)
    print(joao.olhos)
    print(id(Pessoa.olhos), id(barth.olhos), id(joao.olhos), id(1))

