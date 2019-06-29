from b4sh5i import *

proc = "./{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}"
s = process(proc, aslr=False)
e = ELF(proc)
gdb.attach(s, 'tracemalloc on\nc')

{{_cursor_}}

s.interactive()
