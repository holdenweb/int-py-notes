# -*- coding: utf-8 -*-
import json
import requests
response = requests.get("http://www.whitehouse.gov/facts/json/whatsnext/economy")
if response.ok:
    access_data = json.loads(response.content.decode("utf-8"))
    data = access_data[0]
    output = []
    for item in access_data:
        output.append('''<a href="{}" alt="{}">{}</a><br />'''.format(item['url'], item['body'], item['url_title']))
    output_string = """\
<html>
  <head><title>Whitehouse Data</title></head>
  <body>
  <h2>Economic Futures from the Whitehouse"</h2>
  {}
  </body>
<html>
""".format("\n".join(output))
    print(output_string)
else:
    import sys
    sys.exit("Server status code {}".format(response.status_code))