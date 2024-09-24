section .data
    message db 'xin chao! chuc ban mot ngay moi vui ve!', 0

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, message
    mov rdx, 50
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall
