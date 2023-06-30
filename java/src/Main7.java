
// nums = [2,6,3,4]
public class Main7 {
    /**
     * Greatest Common Divisor.
     *
     * @param a first number;
     * @param b second number;
     * @return Greatest Common Divisor.
     */
    static int gcd(int a, int b) {
        int remainder = Math.max(a, b) % Math.min(a, b);
        if (remainder == 0) {
            return Math.min(a, b);
        } else {
            return gcd(Math.min(a, b), remainder);
        }
    }


    public static void main(String[] args) {
        //System.out.println(gcd(50, 15));


        int[] nums = {2,6,3,4};

        //See list of all combination;

        for (int i = 0; i < nums.length-1; i++) {
            System.out.printf("(%d,%d). NOD is %d%n", nums[i],nums[i+1],gcd(nums[i], nums[i+1]));
        }
    }
}
