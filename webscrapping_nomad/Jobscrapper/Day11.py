import requests
import re
import time
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

base_url = "https://www.reddit.com/r/{}/top/?t=month"
idx = 0

"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]


app = Flask("DayEleven")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/read")
def read():
  choose_subreddits = []
  results = []
  kinds = ""
  for subreddit in subreddits:
    if request.args.get(subreddit) == "on":
      choose_subreddits.append(subreddit)

  for choose_subreddit in choose_subreddits:
    kinds += "r/" + choose_subreddit + " "
    url = base_url.format(choose_subreddit)
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    contents = soup.find_all("div", attrs={"class":re.compile("^_1oQyIsiPHYt6nx7VOmd1sz")})
    for content in contents:
      try:
        if content.find("span", attrs={"class":re.compile("^_2oEYZXchPfHwcf9mTMGMg8")}).get_text() == "promoted":
          continue
      except:
        title = content.find("h3", attrs={"class":re.compile("^_eYtD2XCVieq6emjKBH3m")})
        title = title.get_text()
        
        link = content.find("a", attrs={"class":re.compile("^SQnoC3ObvgnGjWt90zD9Z")})["href"]
        link = "https://reddit.com" + link

        vote = content.find("div", attrs={"class":"_1rZYMD_4xY3gRcSS3p8ODO"}).get_text()
        print(vote)
        if "k" in vote:
          vote = vote.replace("k", "")
          vote = round(float(vote) * 1000)
          int(vote)
        else:
          vote = int(vote)
        
        kind = "r/" + choose_subreddit
        results.append({"title":title, "link":link, "vote":vote, "kind":kind})
  results.sort(key=lambda x: x['vote'], reverse=True)

  return render_template("read.html", datas=results, kinds=kinds)

app.run(host="0.0.0.0")