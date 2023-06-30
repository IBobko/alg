import java.util.HashMap;
import java.util.List;
import java.util.function.BiConsumer;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.stream.Collector;

public class Main3 {
    public static void main(String[] args) {
        List<String> hi = List.of("Hi", "Hello", "Welcome");
        List<String> hi2 = List.of();

        Object result = hi2.stream().collect(Collector.of(() -> {
                    return new HashMap<>();
                },
                new BiConsumer<HashMap,String>() {

                    @Override
                    public void accept(HashMap o, String o2) {
                        o.put(Integer.toString(o.size()),o2);
                    }
                }, new BinaryOperator<HashMap>() {
                    @Override
                    public HashMap apply(HashMap o, HashMap o2) {
                        System.out.println(o.getClass());
                        return null;
                    }
                }, new Function<HashMap, HashMap>() {
                    @Override
                    public HashMap apply(HashMap o) {
                        if (o.size() == 0) {
                            return null;
                        } else {
                            return o;
                        }
                    }
                }));


        System.out.println("---------------------");
        //System.out.println(result.getClass());
        System.out.println(result);
    }
}
