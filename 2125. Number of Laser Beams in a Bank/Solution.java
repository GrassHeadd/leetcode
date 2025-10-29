class Solution {
    public int numberOfBeams(String[] bank) {
        int prev = counter(bank[0]);
        int curr = 0;
        int res = 0;

        for (int i = 1; i < bank.length; i++) {
            curr = counter(bank[i]);
            if (curr == 0) {
                continue;
            }

            res += curr * prev;
            prev = curr;
        }
        return res;
    }

    private int counter(String s) {
        int count = 0;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                count += 1;
            }
        }
        return count;
    }
}