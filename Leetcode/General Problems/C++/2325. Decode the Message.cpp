class Solution {
public:
    string decodeMessage(string key, string message) {
        char m[128] = {}, cur = 'a';
        for (char k : key)
            if (isalpha(k) && m[k] == 0)
                m[k] = cur++;
        for (int i = 0; i < message.size(); ++i)
            message[i] = m[message[i]] ?: message[i];
        return message;
    }
};