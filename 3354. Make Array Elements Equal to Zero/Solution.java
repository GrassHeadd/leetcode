class Solution {
    public int countValidSelections(int[] nums) {
        int prefix = 0;
        int suffix = 0;
        int res = 0;
        
        for (int i = 0; i < nums.length; i++) {
            suffix += nums[i];
        }

        for (int i = 0; i < nums.length; i++) {
            suffix -= nums[i];
            if (nums[i] == 0) {
                int diff = Math.abs(suffix - prefix);
                // System.out.printf("%d%n", diff);
                if (diff == 0) {
                    res += 2;
                } else if (diff == 1) {
                    res += 1;
                }
            }
            prefix += nums[i];
        }

        return res;
    }
}