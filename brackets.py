from Stack_Array import ArrayStack

def check_brackets(expression) :
    stack = ArrayStack(len(expression)) 


    # dictionary를 사용하여 닫는 괄호와 여는 괄호의 쌍을 정의, key : 닫는 괄호, value : 여는 괄호
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['    
    }      

    # 문자열로 처리한다. 파이썬은 문자열을 순회할 수 있기 때문에, for 루프를 사용하여 expression의 각 문자에 접근한다.
    open_brackets = "({["
    close_brackets = ")}]"


    # 경우는 총 3가지다. 
    for ch in expression :
        if ch in open_brackets :
            stack.push(ch)
            
        elif ch in close_brackets :
            if stack.is_empty() :
                return False
            
            top_bracket = stack.pop()
            if pairs[ch] != top_bracket :
                return False
            
        else :
            pass

    return stack.is_empty()


# 테스트 케이스

def main() :
    exp1 = " { [ () () ] } "
    exp2 = " ( [ ) ] "
    exp3 = " ( ( () ) )"

    print(exp1, "->", check_brackets(exp1))  # True
    print(exp2, "->", check_brackets(exp2))  # False
    print(exp3, "->", check_brackets(exp3))  # True 


if __name__ == "__main__" : # __name__이 "__main__"인 경우, 즉 이 스크립트가 직접 실행될 때 main() 함수를 호출한다.
    main()

    