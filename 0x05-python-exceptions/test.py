#!/usr/bin/python3
Include/opcode.h
def myfunc(alist):
    return len(alist)
bytecode = dis.Bytecode(myfunc)
for instr in bytecode:
    print(instr.opname)
