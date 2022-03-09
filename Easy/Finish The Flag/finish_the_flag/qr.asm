; COMPILE: nasm -f elf -O0 qr.asm
; LINK: ld -m elf_i386 qr.o -o qr
; RUN: ./qr

SECTION .data
random db '9éỳü{jn==}  <\:  __  P0', 0h
eflag db 'F', 'EHa', 24h, 27h, 'j', 0h ; "QR_v30}" XORed by 23
random2 db 'QóA8dúp0m99rǹ040V05ff1Llk9\0oO\C/\00', 0h
sflag db 43h, 54h, 46h, 6Ch, 65h, 61h, 72h, 6Eh, 7Bh, 0Ah, 0h ; "CTFlearn{\n"

SECTION .text
global _start

_start:
	mov edx, 10
	mov ecx, sflag
	mov ebx, 1
	mov eax, 4
	int 80h

	xor eax, eax

loop:
	
	cmp al, 7
	je done
	
	mov edx, [eflag+eax]
	inc eax
	jmp bite_of_flag

bite_of_flag:

	push ebp
	mov ebp, esp
	push eax

	xor dl, 23
    mov [ebp], dl

	; SYS_WRITE (debug prints flag)
	; mov edx, 1
	; lea ecx, [ebp]
	; mov ebx, 1
	; mov eax, 4
	; int 80h

	pop eax
	pop ebp

	jmp loop

done:
	; SYS_EXIT
	mov ebx, 0
	mov eax, 1
	int 80h

