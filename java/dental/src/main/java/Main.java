import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        InputStream declaration = Main.class.getResourceAsStream("dental_addresses.dat");
        if (declaration != null) {
            BufferedReader br = new BufferedReader(new InputStreamReader(declaration));
            String line;
            int counter = 0;
            boolean done = false;
            StringBuilder addressBuilder = new StringBuilder();
            HashSet<String> addresses = new HashSet<>();
            while ((line = br.readLine()) != null) {

                if (line.contains("Office #")) {
                    counter = 0;
                    System.out.println();
                }
                if (counter == 2 || counter == 3 || (counter == 4 && !line.contains("Office Hours:"))) {
                    done = false;
                    System.out.println("\t\t\t" + line);
                    addressBuilder.append(line);
                } else {
                    System.out.println(line);
                    if (counter >=4 && !done) {
                        addresses.add(addressBuilder.toString());
                        addressBuilder.setLength(0);
                        done = true;
                    }
                }


                counter++;
            }
            br.close();

            for (String a: addresses) {
                System.out.println(a);
            }
        }
        declaration.close();



    }
}
