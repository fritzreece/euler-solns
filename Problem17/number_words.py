
def to_words(n):
    if n == 0:
        return ""
    if n >= 100:
        digit = n // 100
        res = ["one","two","three",
                "four","five","six",
                "seven","eight","nine"][digit-1]
        res += "hundred"
        if n % 100 != 0:
            return res + "and" + to_words(n%100)
        return res
    elif n >= 20:
        digit = n // 10
        res = ["twenty","thirty","forty",
                "fifty","sixty","seventy",
                "eighty","ninety"][digit-2]
        return res + to_words(n%10)
    else:
        return ["one","two","three","four","five","six",
                "seven","eight","nine","ten","eleven",
                "twelve","thirteen","fourteen","fifteen",
                "sixteen","seventeen","eighteen","nineteen"][n-1]



