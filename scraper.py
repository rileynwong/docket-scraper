### Scrape PDFs from UJS Portal.

import requests

# TODO iterate through all dockets
url = 'https://ujsportal.pacourts.us/DocketSheets/MDJReport.ashx?docketNumber=MJ-51301-CR-0000010-2018'
response = requests.get(url, stream=True)

with open ('test.pdf', 'wb') as f:
    f.write(response.content)
