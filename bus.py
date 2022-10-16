class BUS:
    def __init__(self, cpu):
        self.cpu = cpu
        self.ram = [0] * (64*1024)

        rom = 'jogos/teste.4444'
        #rom = 'jogos/4444.bin'
        #rom = 'jogos/o6502-2022-10-15-161248.bin'
        #rom = 'jogos/Castlevania.nes'
        # rom = ['A2', '0A', '8E', '00', '00', 'A2', '03', '8E', '01', '00', 'AC', '00', '00', 'A9', '00', '18', '6D', '01', '00', '88', 'D0', 'FA', '8D', '02', '00', 'EA', 'EA', 'EA']

        # for i in range(len(rom)):
        #     self.ram[0x8000 + i] = hex(rom[i])
        # print(self.ram[0x800:0x8020])
        # input()


        with open(rom, 'rb') as f:
            byte = f.read()
            print(byte)
            input()
            for i in range(len(byte)):
                self.ram[0x8000 + i] = byte[i]
        print(self.ram[0x8000:0x802C])
        print(self.ram[0x8010:0x8016])
        self.ram[0xFFFC] = 0x00
        self.ram[0xFFFD] = 0x80

    
        


    def write(self, addr, data):
        if(addr >= 0x0000 and addr <= 0xFFFF):
            self.ram[addr] = data

    def read(self, addr, readonly = False):
        if addr >= 0x0000 and addr <= 0xFFFF:
            return self.ram[addr]
        return 0x00
        

    def load(self):

        with open(rom, 'rb') as f:
            byte = f.read()
            print(byte)
            input()
            for i in range(len(byte)):
                self.ram[0x8000 + i] = byte[i]