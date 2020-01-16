from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    first_name = request.args.get('first_name')
    return render_template('_index.html', first_name=first_name)

@app.route("/contact")
def contact():
    return render_template('_contact.html', methods = ["POST"])

if __name__ == '__main__':
    app.run()