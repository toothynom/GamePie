
class GbCpu:

	self.registers = {
		"A": 0x00,
		"F": 0x00,
		"B": 0x00,
		"C": 0x00,
		"D": 0x00,
		"E": 0x00,
		"H": 0x00,
		"L": 0x00,
		"PC": 0x0000,
		"SP": 0x0000
	}

	def __init__(self):
		pass

	def nop(self):
		return True

	def rstAddr(self, addr):
		registers["PC"] = addr

		return True

	################################
	#
	# LOAD op codes implementation
	#
	################################

	def ldSregSreg(self, sreg1, sreg2):
		registers[sreg1] = registers[sreg2]

		return True

	def ldSregHL(self, sreg):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] = value

		return True

	def ldSregD8(self, sreg):
		value = readMemory(registers["PC"] + 0x01)

		registers[sreg] = value

		return True

	def ldHLSreg(self, sreg):
		doubleReg = (registers["H"] << 8) | registers["L"]
		
		writeMemory(doubleReg, registers[sreg])

		return True

	def ldSpDsix(self):
		lw = readMemory(registers["PC"] + 1)
		hw = readMemory(registers["PC"] + 2)
		value = (hw << 8) | lw

		registers["SP"] = value

		return True

	def ldDregDsix(self, sreg1, sreg2):
		lw = readMemory(registers["PC"] + 1)
		hw = readMemory(registers["PC"] + 2)

		registers[sreg1] = hw
		registers[sreg2] = lw

		return True

	###############################
	#
	# AND op codes implementation
	#
	###############################

	def andSreg(self, sreg):
		registers["A"] &= registers[sreg]

		return True

	def andMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] &= value

		return True

	def andDEit(self):
		value = readMemory(registers["PC"] + 0x01)

		registers["A"] &= value

		return True

	##############################
	#
	# OR op codes implementation
	#
	##############################

	def orSreg(self, sreg):
		registers["A"] |= registers[sreg]

		return True

	def orMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] |= value

		return True

	def orDEit(self):
		value = readMemory(registers["PC"] + 0x01)

		registers["A"] |= value

		return True

	###############################
	#
	# XOR op codes implementation
	#
	###############################

	def xorSreg(self, sreg):
		registers["A"] ^= registers[sreg]

		return True

	def xorMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] ^= value

		return True

	def xorDEit(self):
		value = readMemory(registers["PC"] + 0x01)

		registers["A"] ^= value

		return True

	####################################
	#
	# Increase op codes implementation
	#
	####################################

	def decDReg(self, regOne, regTwo):
		doubleReg = (regOne << 8) | regTwo
		doubleReg = (doubleReg + 0xFFFF) & 0xFFFF

		registers[regOne] = doubleReg >> 8
		registers[regTwo] = doubleReg & 0x00FF

		return True

	def decSP(self):
		registers["SP"] = (registers["SP"] + 0xFFFF) & 0xFFFF

		return True

	def decSreg(self, sreg):
		registers[sreg] = (registers[sreg] + 0xFF) & 0xFF

		return True

	def decMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		value = (value + 0xFF) & 0xFF

		writeMemory(doubleReg, value)

		return True

	####################################
	#
	# Increase op codes implementation
	#
	####################################

	def incDreg(self, dreg):
		doubleReg = (regOne << 8) | regTwo
		doubleReg = (doubleReg + 1) & 0xFFFF

		registers[regOne] = doubleReg >> 8
		registers[regTwo] = doubleReg & 0x00FF

		return True

	def incSP(self, dreg):
		registers["SP"] = (registers["SP"] + 1) & 0xFFFF

		return True

	def incSreg(self, sreg):
		registers[sreg] = (registers[sreg] + 1) & 0xFF

		return True

	def incMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		value = (value + 1) & 0xFF

		writeMemory(doubleReg, value)

		return True

	###############################
	#
	# ADD op codes implementation
	#
	###############################

	def addSreg(self, sreg):
		registers["A"] = (registers["A"] + registers[sreg]) & 0xFF

		return True

	def addMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] = (registers["A"] + value) & 0xFF

		return True

	def adcSreg(self, sreg):
		cf = registers["F"] >>
		registers["A"] = (registers["A"] + registers[sreg]) & 0xFF

		return True

	def adcMem(self):
		doubleReg = (registers["H"] << 8) | registers["L"]
		value = readMemory(doubleReg)

		registers["A"] = (registers["A"] + value) & 0xFF

		return True


