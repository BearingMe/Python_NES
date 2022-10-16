







self.lookup = {
    { "BRK", self.BRK, self.IMM, 7 },{ "ORA", self.ORA, self.IZX, 6 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 3 },{ "ORA", self.ORA, self.ZP0, 3 },{ "ASL", self.ASL, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "PHP", self.PHP, self.IMP, 3 },{ "ORA", self.ORA, self.IMM, 2 },{ "ASL", self.ASL, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.NOP, self.IMP, 4 },{ "ORA", self.ORA, self.ABS, 4 },{ "ASL", self.ASL, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BPL", self.BPL, self.REL, 2 },{ "ORA", self.ORA, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "ORA", self.ORA, self.ZPX, 4 },{ "ASL", self.ASL, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "CLC", self.CLC, self.IMP, 2 },{ "ORA", self.ORA, self.ABY, 4 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "ORA", self.ORA, self.ABX, 4 },{ "ASL", self.ASL, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
    { "JSR", self.JSR, self.ABS, 6 },{ "AND", self.AND, self.IZX, 6 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "BIT", self.BIT, self.ZP0, 3 },{ "AND", self.AND, self.ZP0, 3 },{ "ROL", self.ROL, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "PLP", self.PLP, self.IMP, 4 },{ "AND", self.AND, self.IMM, 2 },{ "ROL", self.ROL, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "BIT", self.BIT, self.ABS, 4 },{ "AND", self.AND, self.ABS, 4 },{ "ROL", self.ROL, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BMI", self.BMI, self.REL, 2 },{ "AND", self.AND, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "AND", self.AND, self.ZPX, 4 },{ "ROL", self.ROL, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "SEC", self.SEC, self.IMP, 2 },{ "AND", self.AND, self.ABY, 4 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "AND", self.AND, self.ABX, 4 },{ "ROL", self.ROL, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
    { "RTI", self.RTI, self.IMP, 6 },{ "EOR", self.EOR, self.IZX, 6 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 3 },{ "EOR", self.EOR, self.ZP0, 3 },{ "LSR", self.LSR, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "PHA", self.PHA, self.IMP, 3 },{ "EOR", self.EOR, self.IMM, 2 },{ "LSR", self.LSR, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "JMP", self.JMP, self.ABS, 3 },{ "EOR", self.EOR, self.ABS, 4 },{ "LSR", self.LSR, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BVC", self.BVC, self.REL, 2 },{ "EOR", self.EOR, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "EOR", self.EOR, self.ZPX, 4 },{ "LSR", self.LSR, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "CLI", self.CLI, self.IMP, 2 },{ "EOR", self.EOR, self.ABY, 4 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "EOR", self.EOR, self.ABX, 4 },{ "LSR", self.LSR, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
    { "RTS", self.RTS, self.IMP, 6 },{ "ADC", self.ADC, self.IZX, 6 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 3 },{ "ADC", self.ADC, self.ZP0, 3 },{ "ROR", self.ROR, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "PLA", self.PLA, self.IMP, 4 },{ "ADC", self.ADC, self.IMM, 2 },{ "ROR", self.ROR, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "JMP", self.JMP, self.IND, 5 },{ "ADC", self.ADC, self.ABS, 4 },{ "ROR", self.ROR, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BVS", self.BVS, self.REL, 2 },{ "ADC", self.ADC, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "ADC", self.ADC, self.ZPX, 4 },{ "ROR", self.ROR, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "SEI", self.SEI, self.IMP, 2 },{ "ADC", self.ADC, self.ABY, 4 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "ADC", self.ADC, self.ABX, 4 },{ "ROR", self.ROR, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
    { "???", self.NOP, self.IMP, 2 },{ "STA", self.STA, self.IZX, 6 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 6 },{ "STY", self.STY, self.ZP0, 3 },{ "STA", self.STA, self.ZP0, 3 },{ "STX", self.STX, self.ZP0, 3 },{ "???", self.XXX, self.IMP, 3 },{ "DEY", self.DEY, self.IMP, 2 },{ "???", self.NOP, self.IMP, 2 },{ "TXA", self.TXA, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "STY", self.STY, self.ABS, 4 },{ "STA", self.STA, self.ABS, 4 },{ "STX", self.STX, self.ABS, 4 },{ "???", self.XXX, self.IMP, 4 },
    { "BCC", self.BCC, self.REL, 2 },{ "STA", self.STA, self.IZY, 6 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 6 },{ "STY", self.STY, self.ZPX, 4 },{ "STA", self.STA, self.ZPX, 4 },{ "STX", self.STX, self.ZPY, 4 },{ "???", self.XXX, self.IMP, 4 },{ "TYA", self.TYA, self.IMP, 2 },{ "STA", self.STA, self.ABY, 5 },{ "TXS", self.TXS, self.IMP, 2 },{ "???", self.XXX, self.IMP, 5 },{ "???", self.NOP, self.IMP, 5 },{ "STA", self.STA, self.ABX, 5 },{ "???", self.XXX, self.IMP, 5 },{ "???", self.XXX, self.IMP, 5 },
    { "LDY", self.LDY, self.IMM, 2 },{ "LDA", self.LDA, self.IZX, 6 },{ "LDX", self.LDX, self.IMM, 2 },{ "???", self.XXX, self.IMP, 6 },{ "LDY", self.LDY, self.ZP0, 3 },{ "LDA", self.LDA, self.ZP0, 3 },{ "LDX", self.LDX, self.ZP0, 3 },{ "???", self.XXX, self.IMP, 3 },{ "TAY", self.TAY, self.IMP, 2 },{ "LDA", self.LDA, self.IMM, 2 },{ "TAX", self.TAX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "LDY", self.LDY, self.ABS, 4 },{ "LDA", self.LDA, self.ABS, 4 },{ "LDX", self.LDX, self.ABS, 4 },{ "???", self.XXX, self.IMP, 4 },
    { "BCS", self.BCS, self.REL, 2 },{ "LDA", self.LDA, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 5 },{ "LDY", self.LDY, self.ZPX, 4 },{ "LDA", self.LDA, self.ZPX, 4 },{ "LDX", self.LDX, self.ZPY, 4 },{ "???", self.XXX, self.IMP, 4 },{ "CLV", self.CLV, self.IMP, 2 },{ "LDA", self.LDA, self.ABY, 4 },{ "TSX", self.TSX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 4 },{ "LDY", self.LDY, self.ABX, 4 },{ "LDA", self.LDA, self.ABX, 4 },{ "LDX", self.LDX, self.ABY, 4 },{ "???", self.XXX, self.IMP, 4 },
    { "CPY", self.CPY, self.IMM, 2 },{ "CMP", self.CMP, self.IZX, 6 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "CPY", self.CPY, self.ZP0, 3 },{ "CMP", self.CMP, self.ZP0, 3 },{ "DEC", self.DEC, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "INY", self.INY, self.IMP, 2 },{ "CMP", self.CMP, self.IMM, 2 },{ "DEX", self.DEX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 2 },{ "CPY", self.CPY, self.ABS, 4 },{ "CMP", self.CMP, self.ABS, 4 },{ "DEC", self.DEC, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BNE", self.BNE, self.REL, 2 },{ "CMP", self.CMP, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "CMP", self.CMP, self.ZPX, 4 },{ "DEC", self.DEC, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "CLD", self.CLD, self.IMP, 2 },{ "CMP", self.CMP, self.ABY, 4 },{ "NOP", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "CMP", self.CMP, self.ABX, 4 },{ "DEC", self.DEC, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
    { "CPX", self.CPX, self.IMM, 2 },{ "SBC", self.SBC, self.IZX, 6 },{ "???", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "CPX", self.CPX, self.ZP0, 3 },{ "SBC", self.SBC, self.ZP0, 3 },{ "INC", self.INC, self.ZP0, 5 },{ "???", self.XXX, self.IMP, 5 },{ "INX", self.INX, self.IMP, 2 },{ "SBC", self.SBC, self.IMM, 2 },{ "NOP", self.NOP, self.IMP, 2 },{ "???", self.SBC, self.IMP, 2 },{ "CPX", self.CPX, self.ABS, 4 },{ "SBC", self.SBC, self.ABS, 4 },{ "INC", self.INC, self.ABS, 6 },{ "???", self.XXX, self.IMP, 6 },
    { "BEQ", self.BEQ, self.REL, 2 },{ "SBC", self.SBC, self.IZY, 5 },{ "???", self.XXX, self.IMP, 2 },{ "???", self.XXX, self.IMP, 8 },{ "???", self.NOP, self.IMP, 4 },{ "SBC", self.SBC, self.ZPX, 4 },{ "INC", self.INC, self.ZPX, 6 },{ "???", self.XXX, self.IMP, 6 },{ "SED", self.SED, self.IMP, 2 },{ "SBC", self.SBC, self.ABY, 4 },{ "NOP", self.NOP, self.IMP, 2 },{ "???", self.XXX, self.IMP, 7 },{ "???", self.NOP, self.IMP, 4 },{ "SBC", self.SBC, self.ABX, 4 },{ "INC", self.INC, self.ABX, 7 },{ "???", self.XXX, self.IMP, 7 },
}

