class Batata:
    def __init__(self):
        self.bata = 'ta'

        self.lookup = {
            0x00:{ "OPCODE": self.BRK, "ADDR": self.IMM, "CYCLES": 7 }, 0x01:{ "OPCODE": self.ORA, "ADDR": self.IZX, "CYCLES": 6 }, 0x02:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x03:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x04:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 3 }, 0x05:{ "OPCODE": self.ORA, "ADDR": self.ZP0, "CYCLES": 3 }, 0x06:{ "OPCODE": self.ASL, "ADDR": self.ZP0, "CYCLES": 5 }, 0x07:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x08:{ "OPCODE": self.PHP, "ADDR": self.IMP, "CYCLES": 3 }, 0x09:{ "OPCODE": self.ORA, "ADDR": self.IMM, "CYCLES": 2 }, 0x0A:{ "OPCODE": self.ASL, "ADDR": self.IMP, "CYCLES": 2 }, 0x0B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x0C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x0D:{ "OPCODE": self.ORA, "ADDR": self.ABS, "CYCLES": 4 }, 0x0E:{ "OPCODE": self.ASL, "ADDR": self.ABS, "CYCLES": 6 }, 0x0F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0x10:{ "OPCODE": self.BPL, "ADDR": self.REL, "CYCLES": 2 }, 0x11:{ "OPCODE": self.ORA, "ADDR": self.IZY, "CYCLES": 5 }, 0x12:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x13:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x14:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x15:{ "OPCODE": self.ORA, "ADDR": self.ZPX, "CYCLES": 4 }, 0x16:{ "OPCODE": self.ASL, "ADDR": self.ZPX, "CYCLES": 6 }, 0x17:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x18:{ "OPCODE": self.CLC, "ADDR": self.IMP, "CYCLES": 2 }, 0x19:{ "OPCODE": self.ORA, "ADDR": self.ABY, "CYCLES": 4 }, 0x1A:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x1B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0x1C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x1D:{ "OPCODE": self.ORA, "ADDR": self.ABX, "CYCLES": 4 }, 0x1E:{ "OPCODE": self.ASL, "ADDR": self.ABX, "CYCLES": 7 }, 0x1F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
            0x20:{ "OPCODE": self.JSR, "ADDR": self.ABS, "CYCLES": 6 }, 0x21:{ "OPCODE": self.AND, "ADDR": self.IZX, "CYCLES": 6 }, 0x22:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x23:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x24:{ "OPCODE": self.BIT, "ADDR": self.ZP0, "CYCLES": 3 }, 0x25:{ "OPCODE": self.AND, "ADDR": self.ZP0, "CYCLES": 3 }, 0x26:{ "OPCODE": self.ROL, "ADDR": self.ZP0, "CYCLES": 5 }, 0x27:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x28:{ "OPCODE": self.PLP, "ADDR": self.IMP, "CYCLES": 4 }, 0x29:{ "OPCODE": self.AND, "ADDR": self.IMM, "CYCLES": 2 }, 0x2A:{ "OPCODE": self.ROL, "ADDR": self.IMP, "CYCLES": 2 }, 0x2B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x2C:{ "OPCODE": self.BIT, "ADDR": self.ABS, "CYCLES": 4 }, 0x2D:{ "OPCODE": self.AND, "ADDR": self.ABS, "CYCLES": 4 }, 0x2E:{ "OPCODE": self.ROL, "ADDR": self.ABS, "CYCLES": 6 }, 0x2F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0x30:{ "OPCODE": self.BMI, "ADDR": self.REL, "CYCLES": 2 }, 0x31:{ "OPCODE": self.AND, "ADDR": self.IZY, "CYCLES": 5 }, 0x32:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x33:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x34:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x35:{ "OPCODE": self.AND, "ADDR": self.ZPX, "CYCLES": 4 }, 0x36:{ "OPCODE": self.ROL, "ADDR": self.ZPX, "CYCLES": 6 }, 0x37:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x38:{ "OPCODE": self.SEC, "ADDR": self.IMP, "CYCLES": 2 }, 0x39:{ "OPCODE": self.AND, "ADDR": self.ABY, "CYCLES": 4 }, 0x3A:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x3B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0x3C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x3D:{ "OPCODE": self.AND, "ADDR": self.ABX, "CYCLES": 4 }, 0x3E:{ "OPCODE": self.ROL, "ADDR": self.ABX, "CYCLES": 7 }, 0x3F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
            0x40:{ "OPCODE": self.RTI, "ADDR": self.IMP, "CYCLES": 6 }, 0x41:{ "OPCODE": self.EOR, "ADDR": self.IZX, "CYCLES": 6 }, 0x42:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x43:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x44:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 3 }, 0x45:{ "OPCODE": self.EOR, "ADDR": self.ZP0, "CYCLES": 3 }, 0x46:{ "OPCODE": self.LSR, "ADDR": self.ZP0, "CYCLES": 5 }, 0x47:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x48:{ "OPCODE": self.PHA, "ADDR": self.IMP, "CYCLES": 3 }, 0x49:{ "OPCODE": self.EOR, "ADDR": self.IMM, "CYCLES": 2 }, 0x4A:{ "OPCODE": self.LSR, "ADDR": self.IMP, "CYCLES": 2 }, 0x4B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x4C:{ "OPCODE": self.JMP, "ADDR": self.ABS, "CYCLES": 3 }, 0x4D:{ "OPCODE": self.EOR, "ADDR": self.ABS, "CYCLES": 4 }, 0x4E:{ "OPCODE": self.LSR, "ADDR": self.ABS, "CYCLES": 6 }, 0x4F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0x50:{ "OPCODE": self.BVC, "ADDR": self.REL, "CYCLES": 2 }, 0x51:{ "OPCODE": self.EOR, "ADDR": self.IZY, "CYCLES": 5 }, 0x52:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x53:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x54:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x55:{ "OPCODE": self.EOR, "ADDR": self.ZPX, "CYCLES": 4 }, 0x56:{ "OPCODE": self.LSR, "ADDR": self.ZPX, "CYCLES": 6 }, 0x57:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x58:{ "OPCODE": self.CLI, "ADDR": self.IMP, "CYCLES": 2 }, 0x59:{ "OPCODE": self.EOR, "ADDR": self.ABY, "CYCLES": 4 }, 0x5A:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x5B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0x5C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x5D:{ "OPCODE": self.EOR, "ADDR": self.ABX, "CYCLES": 4 }, 0x5E:{ "OPCODE": self.LSR, "ADDR": self.ABX, "CYCLES": 7 }, 0x5F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
            0x60:{ "OPCODE": self.RTS, "ADDR": self.IMP, "CYCLES": 6 }, 0x61:{ "OPCODE": self.ADC, "ADDR": self.IZX, "CYCLES": 6 }, 0x62:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x63:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x64:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 3 }, 0x65:{ "OPCODE": self.ADC, "ADDR": self.ZP0, "CYCLES": 3 }, 0x66:{ "OPCODE": self.ROR, "ADDR": self.ZP0, "CYCLES": 5 }, 0x67:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x68:{ "OPCODE": self.PLA, "ADDR": self.IMP, "CYCLES": 4 }, 0x69:{ "OPCODE": self.ADC, "ADDR": self.IMM, "CYCLES": 2 }, 0x6A:{ "OPCODE": self.ROR, "ADDR": self.IMP, "CYCLES": 2 }, 0x6B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x6C:{ "OPCODE": self.JMP, "ADDR": self.IND, "CYCLES": 5 }, 0x6D:{ "OPCODE": self.ADC, "ADDR": self.ABS, "CYCLES": 4 }, 0x6E:{ "OPCODE": self.ROR, "ADDR": self.ABS, "CYCLES": 6 }, 0x6F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0x70:{ "OPCODE": self.BVS, "ADDR": self.REL, "CYCLES": 2 }, 0x71:{ "OPCODE": self.ADC, "ADDR": self.IZY, "CYCLES": 5 }, 0x72:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x73:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0x74:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x75:{ "OPCODE": self.ADC, "ADDR": self.ZPX, "CYCLES": 4 }, 0x76:{ "OPCODE": self.ROR, "ADDR": self.ZPX, "CYCLES": 6 }, 0x77:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x78:{ "OPCODE": self.SEI, "ADDR": self.IMP, "CYCLES": 2 }, 0x79:{ "OPCODE": self.ADC, "ADDR": self.ABY, "CYCLES": 4 }, 0x7A:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x7B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0x7C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0x7D:{ "OPCODE": self.ADC, "ADDR": self.ABX, "CYCLES": 4 }, 0x7E:{ "OPCODE": self.ROR, "ADDR": self.ABX, "CYCLES": 7 }, 0x7F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
            0x80:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x81:{ "OPCODE": self.STA, "ADDR": self.IZX, "CYCLES": 6 }, 0x82:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x83:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x84:{ "OPCODE": self.STY, "ADDR": self.ZP0, "CYCLES": 3 }, 0x85:{ "OPCODE": self.STA, "ADDR": self.ZP0, "CYCLES": 3 }, 0x86:{ "OPCODE": self.STX, "ADDR": self.ZP0, "CYCLES": 3 }, 0x87:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 3 }, 0x88:{ "OPCODE": self.DEY, "ADDR": self.IMP, "CYCLES": 2 }, 0x89:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0x8A:{ "OPCODE": self.TXA, "ADDR": self.IMP, "CYCLES": 2 }, 0x8B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x8C:{ "OPCODE": self.STY, "ADDR": self.ABS, "CYCLES": 4 }, 0x8D:{ "OPCODE": self.STA, "ADDR": self.ABS, "CYCLES": 4 }, 0x8E:{ "OPCODE": self.STX, "ADDR": self.ABS, "CYCLES": 4 }, 0x8F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 },
            0x90:{ "OPCODE": self.BCC, "ADDR": self.REL, "CYCLES": 2 }, 0x91:{ "OPCODE": self.STA, "ADDR": self.IZY, "CYCLES": 6 }, 0x92:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0x93:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0x94:{ "OPCODE": self.STY, "ADDR": self.ZPX, "CYCLES": 4 }, 0x95:{ "OPCODE": self.STA, "ADDR": self.ZPX, "CYCLES": 4 }, 0x96:{ "OPCODE": self.STX, "ADDR": self.ZPY, "CYCLES": 4 }, 0x97:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 }, 0x98:{ "OPCODE": self.TYA, "ADDR": self.IMP, "CYCLES": 2 }, 0x99:{ "OPCODE": self.STA, "ADDR": self.ABY, "CYCLES": 5 }, 0x9A:{ "OPCODE": self.TXS, "ADDR": self.IMP, "CYCLES": 2 }, 0x9B:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x9C:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 5 }, 0x9D:{ "OPCODE": self.STA, "ADDR": self.ABX, "CYCLES": 5 }, 0x9E:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0x9F:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 },
            0xA0:{ "OPCODE": self.LDY, "ADDR": self.IMM, "CYCLES": 2 }, 0xA1:{ "OPCODE": self.LDA, "ADDR": self.IZX, "CYCLES": 6 }, 0xA2:{ "OPCODE": self.LDX, "ADDR": self.IMM, "CYCLES": 2 }, 0xA3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0xA4:{ "OPCODE": self.LDY, "ADDR": self.ZP0, "CYCLES": 3 }, 0xA5:{ "OPCODE": self.LDA, "ADDR": self.ZP0, "CYCLES": 3 }, 0xA6:{ "OPCODE": self.LDX, "ADDR": self.ZP0, "CYCLES": 3 }, 0xA7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 3 }, 0xA8:{ "OPCODE": self.TAY, "ADDR": self.IMP, "CYCLES": 2 }, 0xA9:{ "OPCODE": self.LDA, "ADDR": self.IMM, "CYCLES": 2 }, 0xAA:{ "OPCODE": self.TAX, "ADDR": self.IMP, "CYCLES": 2 }, 0xAB:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0xAC:{ "OPCODE": self.LDY, "ADDR": self.ABS, "CYCLES": 4 }, 0xAD:{ "OPCODE": self.LDA, "ADDR": self.ABS, "CYCLES": 4 }, 0xAE:{ "OPCODE": self.LDX, "ADDR": self.ABS, "CYCLES": 4 }, 0xAF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 },
            0xB0:{ "OPCODE": self.BCS, "ADDR": self.REL, "CYCLES": 2 }, 0xB1:{ "OPCODE": self.LDA, "ADDR": self.IZY, "CYCLES": 5 }, 0xB2:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0xB3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0xB4:{ "OPCODE": self.LDY, "ADDR": self.ZPX, "CYCLES": 4 }, 0xB5:{ "OPCODE": self.LDA, "ADDR": self.ZPX, "CYCLES": 4 }, 0xB6:{ "OPCODE": self.LDX, "ADDR": self.ZPY, "CYCLES": 4 }, 0xB7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 }, 0xB8:{ "OPCODE": self.CLV, "ADDR": self.IMP, "CYCLES": 2 }, 0xB9:{ "OPCODE": self.LDA, "ADDR": self.ABY, "CYCLES": 4 }, 0xBA:{ "OPCODE": self.TSX, "ADDR": self.IMP, "CYCLES": 2 }, 0xBB:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 }, 0xBC:{ "OPCODE": self.LDY, "ADDR": self.ABX, "CYCLES": 4 }, 0xBD:{ "OPCODE": self.LDA, "ADDR": self.ABX, "CYCLES": 4 }, 0xBE:{ "OPCODE": self.LDX, "ADDR": self.ABY, "CYCLES": 4 }, 0xBF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 4 },
            0XC0:{ "OPCODE": self.CPY, "ADDR": self.IMM, "CYCLES": 2 }, 0xC1:{ "OPCODE": self.CMP, "ADDR": self.IZX, "CYCLES": 6 }, 0xC2:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0xC3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0xC4:{ "OPCODE": self.CPY, "ADDR": self.ZP0, "CYCLES": 3 }, 0xC5:{ "OPCODE": self.CMP, "ADDR": self.ZP0, "CYCLES": 3 }, 0xC6:{ "OPCODE": self.DEC, "ADDR": self.ZP0, "CYCLES": 5 }, 0xC7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0xC8:{ "OPCODE": self.INY, "ADDR": self.IMP, "CYCLES": 2 }, 0xC9:{ "OPCODE": self.CMP, "ADDR": self.IMM, "CYCLES": 2 }, 0xCA:{ "OPCODE": self.DEX, "ADDR": self.IMP, "CYCLES": 2 }, 0xCB:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0xCC:{ "OPCODE": self.CPY, "ADDR": self.ABS, "CYCLES": 4 }, 0xCD:{ "OPCODE": self.CMP, "ADDR": self.ABS, "CYCLES": 4 }, 0xCE:{ "OPCODE": self.DEC, "ADDR": self.ABS, "CYCLES": 6 }, 0xCF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0XD0:{ "OPCODE": self.BNE, "ADDR": self.REL, "CYCLES": 2 }, 0xD1:{ "OPCODE": self.CMP, "ADDR": self.IZY, "CYCLES": 5 }, 0xD2:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0xD3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0xD4:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0xD5:{ "OPCODE": self.CMP, "ADDR": self.ZPX, "CYCLES": 4 }, 0xD6:{ "OPCODE": self.DEC, "ADDR": self.ZPX, "CYCLES": 6 }, 0xD7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0xD8:{ "OPCODE": self.CLD, "ADDR": self.IMP, "CYCLES": 2 }, 0xD9:{ "OPCODE": self.CMP, "ADDR": self.ABY, "CYCLES": 4 }, 0xDA:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0xDB:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0xDC:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0xDD:{ "OPCODE": self.CMP, "ADDR": self.ABX, "CYCLES": 4 }, 0xDE:{ "OPCODE": self.DEC, "ADDR": self.ABX, "CYCLES": 7 }, 0xDF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
            0XE0:{ "OPCODE": self.CPX, "ADDR": self.IMM, "CYCLES": 2 }, 0xE1:{ "OPCODE": self.SBC, "ADDR": self.IZX, "CYCLES": 6 }, 0xE2:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0xE3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0xE4:{ "OPCODE": self.CPX, "ADDR": self.ZP0, "CYCLES": 3 }, 0xE5:{ "OPCODE": self.SBC, "ADDR": self.ZP0, "CYCLES": 3 }, 0xE6:{ "OPCODE": self.INC, "ADDR": self.ZP0, "CYCLES": 5 }, 0xE7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 5 }, 0xE8:{ "OPCODE": self.INX, "ADDR": self.IMP, "CYCLES": 2 }, 0xE9:{ "OPCODE": self.SBC, "ADDR": self.IMM, "CYCLES": 2 }, 0xEA:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0xEB:{ "OPCODE": self.SBC, "ADDR": self.IMP, "CYCLES": 2 }, 0xEC:{ "OPCODE": self.CPX, "ADDR": self.ABS, "CYCLES": 4 }, 0xED:{ "OPCODE": self.SBC, "ADDR": self.ABS, "CYCLES": 4 }, 0xEE:{ "OPCODE": self.INC, "ADDR": self.ABS, "CYCLES": 6 }, 0xEF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 },
            0XF0:{ "OPCODE": self.BEQ, "ADDR": self.REL, "CYCLES": 2 }, 0xF1:{ "OPCODE": self.SBC, "ADDR": self.IZY, "CYCLES": 5 }, 0xF2:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 2 }, 0xF3:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 8 }, 0xF4:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0xF5:{ "OPCODE": self.SBC, "ADDR": self.ZPX, "CYCLES": 4 }, 0xF6:{ "OPCODE": self.INC, "ADDR": self.ZPX, "CYCLES": 6 }, 0xF7:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 6 }, 0xF8:{ "OPCODE": self.SED, "ADDR": self.IMP, "CYCLES": 2 }, 0xF9:{ "OPCODE": self.SBC, "ADDR": self.ABY, "CYCLES": 4 }, 0xFA:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 2 }, 0xFB:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 }, 0xFC:{ "OPCODE": self.NOP, "ADDR": self.IMP, "CYCLES": 4 }, 0xFD:{ "OPCODE": self.SBC, "ADDR": self.ABX, "CYCLES": 4 }, 0xFE:{ "OPCODE": self.INC, "ADDR": self.ABX, "CYCLES": 7 }, 0xFF:{ "OPCODE": self.XXX, "ADDR": self.IMP, "CYCLES": 7 },
        }

        print(self.lookup[0x00]['ADDR'])

b = Batata()