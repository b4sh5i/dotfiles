from pwn import *

s = process("./{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}")
gdb.attach(s, 'tracemalloc on\nc')

{{_cursor_}}

s.interactive()
