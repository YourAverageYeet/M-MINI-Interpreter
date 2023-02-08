###  M-MINI Interpreter Functions
###  These are the Functions that will be executed by the interpreter upon
###  reading a keyword. No "actual" interpreter code.
###  Mike Hensley, 2023

def NULL_OP():
  ### No Operation Instruction ###
  pass

def LOAD_VAR(lo_byte, hi_byte):
  ### Loads a value from a given memory address ###
  