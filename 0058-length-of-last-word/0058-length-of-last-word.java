class Solution {
    public int lengthOfLastWord(String s) {
    int count = 0;
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s.charAt(i) == ' ' && count > 0)
            break;
        if (s.charAt(i)!=' '){
            count++;
        }
    };
    return count;
}
}