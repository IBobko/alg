#include <stdio.h>
#include <stdint.h>

uint64_t getsp( void )
{
    uint64_t sp;
    asm( "mov %%rsp, %0" : "=rm" ( sp ));
    return sp;
}

int main(void)
{
    printf("main is : %p\n", &main);
    printf("stack pointer is : %ld\n", getsp());
    return 0;
}