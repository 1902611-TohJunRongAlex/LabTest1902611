from flask import Flask, render_template

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def main():
	if request.method == 'POST':
        searchvalue = request.form['search']
		return render_template('done.html',searchvalue = searchvalue)
    return render_template('index.html')
	
@app.route("/done", methods=['GET', 'POST'])
def done():
    return render_template('done.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 80)
