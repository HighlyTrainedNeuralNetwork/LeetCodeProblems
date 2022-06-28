def rotatedDigits(n):
    good = 0
    for int in range(1, n + 1):
        string = str(int)
        mapped = "".join(map(lambda i: i if i in ["0", "1", "8"] else ("2" if i == "5" else ("5" if i == "2" else ("6" if i == "9" else
                 ("9" if i == "6" else "*")))), string))
        if mapped != string and "*" not in mapped:
            good += 1
    return good


n = 10
print(rotatedDigits(n))