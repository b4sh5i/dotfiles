#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/ioctl.h>

int main() {
	int driver1 = open("/dev/{{_expr_:substitute('{{_input_:name}}', '\w\', '\u\0', '')}}", O_RDWR);
	if (!driver1){
		exit(1);	
	}

	{{_cursor_}}
	return 0;
}
