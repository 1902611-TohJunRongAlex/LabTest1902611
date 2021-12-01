from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def main():
    return render_template('index.html', methods=['GET', 'POST'])
	
@app.route("/done")
def done():
    return render_template('done.html', methods=['GET', 'POST'])


if __name__ == "__main__":
    app.run(host="0.0.0.0")
