import bs4
import re
import requests
import sys

urls = sys.argv[1:]
url_pattern = re.compile(r'https://codeforces.com/contest/(\d+)/submission/(\d+)')
data_url = 'https://codeforces.com/data/submitSource'
ids = [] # list of (contestId,submissionId)
for url in urls:
    try:
        contestId,submissionId = url_pattern.fullmatch(url).groups()
    except:
        sys.stderr.write('invalid url: %s\n'%url)
        quit()
    ids.append((contestId,submissionId))

if len(urls) == 0:
    sys.stderr.write('no urls provided\n')
    quit()

with requests.Session() as session:
    # get first page to extract csrf_token
    page = session.get(urls[0])
    if not page.ok:
        sys.stderr.write('failed first page request\n')
        quit()
    soup = bs4.BeautifulSoup(page.text,'html.parser')
    csrf_token = soup.select_one('meta[name="X-Csrf-Token"]')['content']
    sys.stderr.write('csrf_token = %s\n'%csrf_token)
    for i in range(len(ids)):
        contestId,submissionId = ids[i]
        data = {'submissionId':submissionId,'csrf_token':csrf_token}
        sys.stderr.write('post data = %s\n'%str(data))
        req = session.post(data_url,data)
        if not req.ok:
            sys.stderr.write('request failed\n')
            quit()
        with open('codeforces_submission_%s.json'%submissionId,'w') as outfile:
            outfile.write(req.text)

