import requests
import sys

r = requests.get(sys.argv[1])
word = sys.argv[2]
status = r.status_code
#print(status);
#print(r.text)

if status == 200:
    print(r.text.count(word));
else:
    print('ERROR：' + str(status));
