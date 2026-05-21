class Stack {
public: 
    char arr[10000];
    int top;
    Stack() {top = -1;}
    void push(char c) {
        arr[++top] = c;
    }
    char pop() {
        int elem = arr[top--];
        return elem;
    }
    char peek() {
        return arr[top];
    }
    char isEmpty() {
        return (top==-1) ? true : false;
    }
};

class Solution {
public:
    bool isValid(string s) {
        if (s.length() == 1) {
            return false;
        } else {
            Stack stack;
            bool result=false;
            int count=0;
            for (char i : s) {
                if (i == '[' || i == '(' || i == '{') {
                    stack.push(i);
                
                } else {
                    if (not stack.isEmpty()) {
                        char a = stack.pop();
                        switch (i)
                        {
                        case '}':
                            count += (a == '{') ? 1 : 0;
                            break;
                        case ']':
                            count += (a == '[') ? 1 : 0;
                            break;
                        case ')':                
                            count += (a == '(') ? 1 : 0;
                        default:
                            break;
                        }
                    } else {
                        result = false;
                    }
                }
            }
            if (count*2 == s.length()) {
                return true;
            } else {
                return result;
            }

        }   

    }
};