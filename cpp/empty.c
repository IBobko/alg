#include <stdio.h>

void __attribute__((constructor)) p_init(void) {
    printf("init\n");
}

void __attribute__((destructor)) p_fini(void) {
    printf("fini\n");
}


int main() {
    return 0;
}

