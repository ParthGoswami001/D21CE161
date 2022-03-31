def swap_case(String):
    str = ""
    for let in String:
        if let.isupper() == True:
            str += (let.lower())
        else:
            str += (let.upper())
    return str


if __name__ == '__main__':
    String = input()
    result = swap_case(String)
    print(result)