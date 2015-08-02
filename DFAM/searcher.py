#-*- coding: utf-8 -*-

__author__ = 'kyeongwookma'
import json, urllib

search_keyword = ["android design", "android gui", "android ui", "android usability"]

base_url = "https://api.github.com/search/issues"
query = "?q="
opt = "+language:java+state:closed"
page_idx = "&page="
per_page = "&per_page=100"

def filter_google(issues):
    return filter(lambda x:x["user"]["login"] != "GoogleCodeExporter", issues)

for keyword in search_keyword:

    for idx in range(1,100):
        url = base_url + query + keyword + opt + page_idx + str(idx) + per_page

        try:
            issues = json.loads(urllib.urlopen(url).read(), "utf-8")["items"]
            issues = filter_google(issues)

            for issue in issues:
                url = issue["html_url"]
                body = issue["body"]
                if url is not None and body is not None:
                    print "url : " + url.encode("utf-8") + "\n" + "body : " + body.encode("utf-8") + "\n"

        except KeyError, KeyboardInterrupt:
            pass
