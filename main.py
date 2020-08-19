from flask import Flask, render_template, request

app = Flask(__name__)

#handler/controller 1
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "GET":
        return render_template("index.html")

    elif request.method == "POST":
        name = request.form.get("your-name")
        return f"Hello {name}! :-)"


#handler 2
@app.route("/second-handler")
def second_handler():
    return "here's the second handler"

#handler 3
@app.route('/about')
def about():
    return 'Something about me'


#this is just a regular way how to run some Python files safely
if __name__ == '__main__':
    app.run()
