import java.util.Optional;

public class Main4 {
    public static void main(String[] args) {
        System.out.println(Optional.ofNullable(null).equals(Optional.empty()));
    }
}
