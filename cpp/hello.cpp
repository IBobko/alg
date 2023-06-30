#include <stdio.h>
#include <unistd.h>

int main() {
    // printf() displays the string inside quotation
    //printf("Hello, World!");
    char *const text = "Hello";
    write(1, text, 2);
    return 0;
}