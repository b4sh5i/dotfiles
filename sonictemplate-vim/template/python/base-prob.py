from b4sh5i import *

e = ELF("./{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}")

def con():
    if len(sys.argv) == 2:
        s = process("./{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}")
        gdb.attach(s, 'c\n')
    else:
        s = remote()
    return s

s = con()
sa = s.sendafter
sla = s.sendlineafter

{{_cursor_}}

s.interactive()
