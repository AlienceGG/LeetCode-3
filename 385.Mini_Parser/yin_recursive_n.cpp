class Solution {
public:
    NestedInteger deserialize(string s)
    {
        // end condition
        if (s.empty()) return NestedInteger(); // empty list
        if (s[0] != '[') return NestedInteger(stoi(s)); // number value
        
        // res
        NestedInteger res;
        for (int i = 1; i < s.size();)
        {
            // value ni || list ni
			if (isNumber(s[i]) || s[i] == '[')
			{
				int j = i;
				if (isNumber(s[i])) // value ni
					while (isNumber(s[j])) ++j;
				
				if (s[i] == '[') // list ni
				{
					// get pos of correspondent ']'
					int cnt = 1;
					while (cnt > 0) { ++j; cnt = s[j] == '[' ? cnt + 1 : s[j] == ']' ? cnt - 1 : cnt; }
				}
				
				res.add(deserialize(s.substr(i, j - i)));
				i = j;
			}
			else
                ++i;
        }
        return res;
    }
    
    bool isNumber(char c) { return isdigit(c) || c == '-'; }
};