from cpu import CPU

cpu = CPU()

while cpu.complete != 1:
    cpu.clock()


