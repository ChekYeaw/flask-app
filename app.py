from flask import Flask

app = Flask(__name__)

@app.route("/")
def chek():
    return "<p>Hello, Chek!How is it going</p>"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)