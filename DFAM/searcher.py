__author__ = 'kyeongwookma'
import json, urllib

search_keyword = ["android gui", "android ui", "android usability"]

base_url = "https://api.github.com/search/issues"
query = "?q="
opt = "+language:java+state:closed"

def filter_google(issues):
    return filter(lambda x:x["user"]["login"] != "GoogleCodeExporter", issues)

for keyword in search_keyword:
    issues = json.loads(urllib.urlopen(base_url + query + keyword + opt).read(), "utf-8")["items"]
    issues = filter_google(issues)

    for issue in issues:
        print "url : " + issue["html_url"] + "\n" + "body : " + issue["body"] + "\n"