string = list(filter(lambda x: x not in "aeiouy", input().lower()))
print("."+".".join(string))