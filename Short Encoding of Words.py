def minimumLengthEncoding(words):
    words.sort(key=lambda x: len(x), reverse=True)
    output = ""
    for word in words:
        if word + "#" not in output:
            output += word + "#"
    print(len(output))

words = ["time", "me", "bell"]
minimumLengthEncoding(words)