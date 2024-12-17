a = "HeLLo WoRLd"

def case(a):
    result = ""

    for x in a:
        if 'A' <= x <= 'Z':
            result = result + chr(ord(x) + 32)

        elif 'a' <= x <= 'z':
            result = result + chr(ord(x) - 32)

    return result

print("case:", case(a))
