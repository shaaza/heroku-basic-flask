from flask import Flask, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

@app.route('/optimizing-sql-queries')
def sql():
    return redirect("https://medium.com/@shaaz_a/how-to-choose-a-table-index-for-your-sql-database-d47715a35f34", code=302)

@app.route('/programming-with-purity')
def functional():
    return redirect("https://medium.com/@shaaz_a/methods-of-functional-programming-using-python-or-javascript-b3309bb2c807", code=302)

@app.route('/architecting-a-text-adventure-game')
def textgame():
    return redirect("https://medium.com/@shaaz_a/architecting-a-text-adventure-game-2e0dc4d49812", code=302)

@app.route('/seeing-responsibilities')
def responsibilities():
    return redirect("https://medium.com/@shaaz_a/latest", code=302)

@app.route('/string-matching-indic-text')
def indictext():
    return redirect("github.com/nilenso/kosha/blob/scrape-test-data/doc/stitching.org", code=302)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
