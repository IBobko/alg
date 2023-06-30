import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        String directory = System.getProperty("user.home");
        String fileName = "IdeaProjects/alg/java/img.bmp";
        String saved = "IdeaProjects/alg/java/img_saved.bmp";

        Path path = Paths.get(directory, fileName);
        try {
            byte[] data = Files.readAllBytes(path);
            ByteArrayInputStream inputStream = new ByteArrayInputStream(data);
            String bm = new String(inputStream.readNBytes(2));
            int size = readInt(inputStream.readNBytes(8));
            int offset = readInt(inputStream.readNBytes(4));

            long skip = inputStream.skip(offset - 14);

            for (int i = data.length - 1; i >= offset; i = i - 3) {
                if (((i - data.length - 1) - 1) % 8 == 0) {
                    System.out.println();
                }
                if (data[i] == -1) {
                    System.out.print("\u2586");
                } else {
                    System.out.print(" ");
                }

            }

            for (int i = data.length - 1; i >= offset; i = i - 3) {
                System.out.print(data[i]);
            }

            System.out.println(bm);
            System.out.println("Size: " + size);
            System.out.println("Offset: " + offset);
            Path savedPath = Paths.get(directory, saved);
            Files.write(savedPath, data);

        } catch (IOException e) {
            // exception handling
        }

    }

    public static long bytesToLong(byte[] bytes) {
        r(bytes);
        return ByteBuffer.wrap(bytes).getLong();
    }

    public static void r(byte[] bytes) {
        for (int i = 0; i < bytes.length / 2; i++) {
            byte temp = bytes[i];
            bytes[i] = bytes[bytes.length - i - 1];
            bytes[bytes.length - i - 1] = temp;
        }
    }

    private static int readInt(byte[] data) {
        int resultInt = 0;
        for (int i = 3; i >= 0; i--) {
            resultInt = resultInt << Byte.SIZE | (data[i] & 0x000000FF);
        }
        return resultInt;
    }

}