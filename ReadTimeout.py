import requests
from requests.exceptions import ReadTimeout
try:
    re = requests.get('http://httpbin.org/get', timeout=0.6)
    print(re.status_code)
except ReadTimeout:
    print('Timeout')
# ReadTimeout
# ConnectionError
# RequestException