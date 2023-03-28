import builtins

_print = builtins.print
_input = builtins.input

def alter():
    builtins.print = _input
    builtins.input = _print

def alter_back():
    builtins.print = _print
    builtins.input = _input

# print('This is a General Print Statement')
# _print('This is a General Print Statement')
# input('I Want to grab some info > ')
# _input('I Want to grab some info > ')
alter()
# _print('This is a General Print Statement or am I?: ')
# print('This is a General Print Statement or am I?: ')
#
# _input('I Want to grab some info > ')
# input('Wait, What just happen there?')
#
alter_back()
#
print('Am I back to Print?')
input('Can I grab info again?: ')
