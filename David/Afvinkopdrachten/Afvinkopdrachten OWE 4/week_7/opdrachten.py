from flask import Flask, render_template

app = Flask(__name__)


@app.route("/opdrachten")
def opdrachten():
    return render_template("2021OpdrachtenJavaScript.html")

if __name__ == '__main__':
    app.run()