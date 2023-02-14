import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main2 {
    public static void main(String[] args) {
//        Integer a = 1;//Integer.MIN_VALUE;
//        System.out.println(Integer.toBinaryString(a));
//        System.out.println(a);
//        a = a >>> -5;
//        System.out.println(Integer.toBinaryString(a));
//        System.out.println(a);

        Integer a = 5;

        for (int i = 0 ; i < 32; i++) {
            System.out.println(rotate(a,i));
        }

        for (int i = 0 ; i < 32; i++) {
            System.out.println(rotateViceVerse(a,i));
        }

        System.out.println("------------------");
        System.out.println(-32488);
        System.out.println(Integer.toBinaryString(-32488& 0xFFFF));
        System.out.println(rotateShort((short) -32488));
        System.out.println(Integer.toBinaryString(rotateShort((short)-32488)));
    }


    static int rotate(int bits, int k) {
        return (bits >>> k) | (bits << (Integer.SIZE - k));
    }

    static int rotateViceVerse(int bits, int k) {
        return (bits >>> Integer.SIZE - k) | (bits << k);
    }

    static short rotateShort(short bits) {
        return (short) (bits >> 8 &0x000000FF | bits << 8 & 0xFFFF);
    }
}
