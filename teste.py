class Teste:
    def __init__(self):
        self.lookup = {
            0x00: self.teste
        }

    def teste(self):
        print('4.444')

    def run(self, op):
        return self.lookup[op]()


t = Teste()
t.run(0x00)