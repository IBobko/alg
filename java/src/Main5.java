import javax.swing.text.Style;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.util.Random;
import java.util.Optional;

/**
 * Проблема работы с шумами.
 */
public class Main5 {
    public static void main(String[] args) {
        byte[] data = {1,2,3,4};

        Random rand = new Random();



        ByteArrayInputStream a = new ByteArrayInputStream(data);

        System.out.print("");
        for (int i = 0; i < 100; i++) {
            int randomNumber = rand.nextInt(10);
            if (randomNumber == 5) {
                System.out.print(1);
            } else {
                System.out.print(0);
            }
        }


        ByteArrayOutputStream b = new ByteArrayOutputStream();

        b.write(4);
        System.out.println(b.toByteArray()[0]);
    }
}
