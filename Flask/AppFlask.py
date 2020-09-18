from flask import Flask, request, jsonify, render_template, make_response
from flask_jsglue import JSGlue
app =Flask(__name__)
jsglue = JSGlue(app)

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

@app.route('/', methods = ["GET"])
def home():
    return render_template('app.html')

@app.route('/thanks', methods = ["GET"])
def home():
    return

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')