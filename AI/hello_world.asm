section .data
    hello db 'Hello, World!',0 ; Matn (string) saqlash
    hello_len equ $ - hello     ; Matn uzunligini hisoblash

section .text
    global _start

_start:
    ; Matnni ekranga chiqarish
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, hello_len
    int 0x80

    ; Dasturni tugatish
    mov eax, 1
    int 0x80
