; 32 bit nasm style x86 assembly
; build command:
; 		nasm -f elf -F stabs x86.asm
;			ld -o x86 x86.o

section .data
str:		db 'Hello World', 0Ah
str_len equ $ - str

section .text
global _start

_start:
				mov		eax, 4
				mov		ebx, 1

				mov   ecx, str
				mov		edx, str_len
				int   80h

				mov   eax, 1
				mov   ebx, 0
				int   80h