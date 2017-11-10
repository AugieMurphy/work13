from flask import Flask, render_template
import json, urllib2

u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=KGU8ZkFdOtPVbGTpC2yLVg9FCvRlVbeS2VzlCoDO")
u_str = u.read()
d = json.loads(u_str)

my_app = Flask(__name__)
  
@my_app.route('/')
def root():
    return render_template("nasa.html", title=d['title'], picture=d['url'], description=d['explanation'])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
