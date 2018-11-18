from flask import Flask, render_template, request
from urllib.parse import urlparse
import os
import redis

app = Flask(__name__)

@app.route('/_db', methods=['GET','POST'])
def _db():
	val = None
	if request.method == 'POST':
		r = redis.from_url(os.environ.get('REDISCLOUD_URL'))
		val = eval(r.get(request.form['key']))
	return render_template('db.html', val=val)

if __name__ == '__main__':
    app.run(debug=True)
