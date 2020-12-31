import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

db = {}
app = Flask("DayNine")

@app.route("/")
def home():
  order_by = request.args.get('order_by', '')
  if order_by == "new":
    is_new_exist = db.get("new")
    if is_new_exist:
      pass
    else:
      new_db = {}
      json_new = requests.get(new).json()
      for idx, data in enumerate(json_new['hits']):
        new_db[idx] = [data['objectID'], data['title'], data['url'], data['author'], data['points'], data['num_comments']]
      db["new"] = new_db
    return render_template("index.html", db=db["new"], state=1)   

  elif order_by == "popular":
    is_popular_exist = db.get("popular")
    if is_popular_exist:
      pass
    else:
      popular_db = {}
      json_popular = requests.get(popular).json()
      for idx, data in enumerate(json_popular['hits']):
        popular_db[idx] = [data['objectID'], data['title'], data['url'], data['author'], data['points'], data['num_comments']]
      db["popular"] = popular_db
    return render_template("index.html", db=db["popular"], state=0)

  else:
    is_popular_exist = db.get("popular")
    if is_popular_exist:
      pass
    else:
      popular_db = {}
      json_popular = requests.get(popular).json()
      for idx, data in enumerate(json_popular['hits']):
        popular_db[idx] = [data['objectID'], data['title'], data['url'], data['author'], data['points'], data['num_comments']]
      db["popular"] = popular_db
    return render_template("index.html", db=db["popular"], state=0)

@app.route("/<id>")
def potato(id):
  detail_db = {}
  comment_db = {}
  json_detail = requests.get(make_detail_url(id)).json()
  detail_db['title'] = json_detail.get('title')
  detail_db['points'] = json_detail.get('points')
  detail_db['author'] = json_detail.get('author')
  detail_db['url'] = json_detail.get('url')
  for idx, comment in enumerate(json_detail['children']):
    if comment['author']: # 해당 값이 존재하면
      comment_db[idx] = [comment['author'], comment['text']]
    else: # 해당 값이 null이라서 delete된거임
      comment_db[idx] = "[deleted]"
      
  return render_template("detail.html", db=detail_db, comment_db=comment_db)

app.run(host="0.0.0.0")