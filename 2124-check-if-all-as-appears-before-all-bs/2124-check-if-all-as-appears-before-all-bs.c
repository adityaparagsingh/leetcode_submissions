bool checkString(char* s) {
    for (int i = 1; s[i]; i++) {
        if (s[i - 1] == 'b' && s[i] == 'a')
            return false;
    }
    return true;
}