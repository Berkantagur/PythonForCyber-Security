# In programming and software development, fuzzing or fuzz testing is an automated software testing
# technique that involves providing invalid, unexpected, or random data as inputs to a computer program.
# In programming and software development, fuzzing or fuzz testing is an automated software testing 
# technique that involves providing invalid, unexpected, or random data as inputs to a computer program.

import requests

file = open("fuzzing.txt", "r")
content = file.read()
file.close()
header = {"Cookie": "scurity = low; PHPSESSID = ....................."}
for i in content.split("\n"):
    print(i)
    url = "http://10.10.10.10" + str(i)
    result = requests.get(url = url, headers = header)

    if "200" in str (result.status_code):
        print("There is a file or directory", i)

    else:
        print("There is not a file or directory", i)

