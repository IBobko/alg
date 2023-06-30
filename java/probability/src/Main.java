import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;


class T {
    Map<Character, Integer> next = new HashMap<>();
    Integer count = 1;
}

public class Main {
    public static void main(String[] args) throws IOException {

        InputStream declaration = Main.class.getResourceAsStream("declaration.txt");

        BufferedReader br = new BufferedReader(new InputStreamReader(declaration, StandardCharsets.UTF_8));

        Map<Character, T> letters = new HashMap<>();

        String line;
        int total = 0;
        while ((line = br.readLine()) != null) {
            Character current = null;
            for (char x: line.toCharArray()) {
                total++;
                if (current!=null) {
                    T n = letters.get(current);
                    if (n.next.get(x)!=null) {
                        int value = n.next.get(x);
                        value++;
                        n.next.put(x,value);

                    } else {
                        n.next.put(x,1);
                    }
                }


                if (letters.get(x)!=null) {
                    T value = letters.get(x);
                    value.count++;
                    letters.put(x,value);
                } else {
                    letters.put(x, new T());
                }

                current = x;

            }


        }

        if (total!=0) {

            for (Map.Entry<Character, T> entry : letters.entrySet()) {
                System.out.printf("Probability of %s (count=%d) is  %f %n", entry.getKey(),entry.getValue ().count,(double)entry.getValue().count / total);
                for (Map.Entry<Character, Integer> next : entry.getValue().next.entrySet()) {
                    System.out.printf("\t\tProbability of %s (count=%d) is  %f %n", next.getKey(), next.getValue(), (double)next.getValue() / total);
                }
            }
        }


        System.out.printf("Total: %d", total);

//        declaration.read();
//        while(true) {
//            int current = declaration.read();
//            if (current == -1) {
//                break;
//            }
//            char x = (char)current;
//            System.out.print(x);
//            if (declaration.read() == -1) {
//                break;
//            }
//        }
//


    }
}
