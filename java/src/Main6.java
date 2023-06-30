import javax.swing.text.Style;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.util.Random;
import java.util.Optional;

/**
 * Проблема работы с шумами.
 */
public class Main6 {
    public static void main(String[] args) {
        Random rand = new Random();

        int sum = 0;
        for (int i = 0; i < 100; i++) {
            int noise = 0;
            for (int j = 0; j < 100; j++) {
                int randomNumber = rand.nextInt(10);
                if (randomNumber == 5) {
                    noise = noise + 1;
                }
            }
            System.out.print(noise + " ");
            sum = sum + noise;
        }
        System.out.print("\n\n" + sum + " ");

    }
}
