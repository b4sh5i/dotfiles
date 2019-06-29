from b4sh5i import *

proc = "./{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}"
s = process(proc, aslr=False)
e = ELF(proc)
gdb_pie_attach(s, [{{_cursor_}}],'tracemalloc on\n')



s.interactive()
