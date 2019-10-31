.section .data 
hello:
	.string "Hello World!\n"
longhello:
	.int .-hello

.section .text
.global _start

_start:

	mov $4, %eax
	mov $1, %ebx
	mov $hello, %ecx
	mov longhello, %edx
	int $0x80

	mov $1, %eax
	mov $0, %ebx
	int $0x80
