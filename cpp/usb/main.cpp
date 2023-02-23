#include <stdio.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

int main(int argc, char *argv[]) {
    const char *filepath = "/dev/sda1";
    const char *dest_path = "/home/igor/usb.data";
    int fd = open(filepath, O_WRONLY);

    int dest = open(dest_path, O_CREAT | O_WRONLY, 644);
    if (fd < 0) {
        printf("\n\"%s \" could not open\n", filepath);
        exit(1);
    }

    if (dest < 0) {
        printf("\n\"%s \" could not open\n", filepath);
        exit(1);
    }

    char buf[2];

    for (int i = 0; i < 512; i++) {
        read(fd, buf, 2);
        write(dest, buf, 2);
    }

    close(dest);
    close(fd);
}