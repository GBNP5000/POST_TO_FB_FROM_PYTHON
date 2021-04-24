import requests as req

pageid = ""
accesst = ""

msg = """
   THIS POST IS CREATED BY PYTHON ;-)
"""

post_url = "https://graph.facebook.com/{}/feed".format(pageid)
payload = {
    "message": msg,
    "access_token": accesst
}

r = req.post(post_url, data=payload)
print(r.text)
