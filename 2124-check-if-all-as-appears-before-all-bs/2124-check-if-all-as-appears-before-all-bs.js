var checkString = function(s) {
    for (let i = 1; i < s.length; i++) {
        if (s[i - 1] === 'b' && s[i] === 'a')
            return false;
    }
    return true;
};