class Solution {
    public int smallestNumber(int n) {
        String binary = Integer.toBinaryString(n);
        // System.out.printf(binary);

        return (1 << binary.length()) - 1;
    }
}