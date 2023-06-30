/**
 *
 * <a href="https://leetcode.com/problems/valid-palindrome/submissions/941304333/">leetcode page</a>
 */
public class ValidPalindrome {

    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        String reversed = new StringBuilder(s).reverse().toString();
        return s.equals(reversed);
    }

    /**
     * Using Two-pointer approach.
     *
     * @param s
     * @return
     */
    public boolean isPalindrome2(String s) {
        s = s.toLowerCase();
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }
            if (s.charAt(left) != s.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static void main(String[] args) {

    }

}
