class Pessoa:
    def __init__(self, nome=None, idade=25):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Hello {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Barth')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
