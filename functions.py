###  M-MINI Interpreter Functions
###  These are the Functions that will be executed by the interpreter upon
###  reading a keyword. No "actual" interpreter code.
###  Mike Hensley, 2023

def NULL_OP():
  ### No Operation Instruction ###
  pass

def LOAD_MEM(reg_num, lo_byte, hi_byte):
  ### Loads a value from a given memory address into a given register ###
  if(reg_num >= 8):
    raise IndexError("Invalid register number")
  else:
    if(lo_byte < 0 or lo_byte > 255):
      raise ValueError("Low byte too high or low")
    elif(hi_byte < 0 or hi_byte > 255):
      raise ValueError("High byte too high or low")
    else:
      offset = lo_byte + (16 * hi_byte)
      global registers[reg_num] = memory[offset]
      pass
    pass
  pass

def LOAD_IND(reg_num, byte1):
  ### Loads a value from memory indirectly ###
  if(reg_num >= 8):
    raise IndexError("Invalid register Number")
  else:
    if(byte1 < 0 or (byte1 + 1) > 255):
      raise ValueError("Given low byte or generated high byte not within zeropage")
    else:
      lo = memory[byte1]
      hi = memory[byte1 + 1]
      LOAD_MEM(reg_num, lo, hi)
      pass
    pass
  pass

def LOAD_ABS(reg_num, value):
  ### Takes a supplied value and sets the given register to that value ###
  if(reg_num >= 8):
    raise IndexError("Invalid register number")
  else:
    if(value < 0 or value > 255):
      raise ValueError("Given value is too high or low")
    else:
      registers[reg_num] = value
      pass
    pass
  pass

def SAVE_MEM(reg_num, lo_byte, hi_bye):
  ### Write the value of a register to a given memory location ###
  if(reg_num >= 8):
    raise IndexError("Invalid register number")
  else:
    if(lo_byte < 0 or lo_byte > 255):
      raise ValueError("Low byte too high or low")
    elif(hi_byte < 0 or hi_byte > 255):
      raise ValueError("High byte too high or low")
    else:
      offset = lo_byte + (16 * hi_byte)
      memory[offset] = registers[reg_num]
      pass
    pass
  pass
