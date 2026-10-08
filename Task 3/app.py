from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return ("<h1>You are welcome</h1> "
            "<p>We are learning Flask here</p>")



@app.route('/hello/<name>')
def hello(name: str):
    return (f"<h1> Hello my friend {name}</h1> <p> How are you? </p>")


@app.route('/search')
def search():
    q = request.args.get('q', '')
    return f'<p>Ищем {q}</p>'

@app.route('/about')
def about():
    return render_template('Template.html')

@app.route("/contacts")
def contact():
    return "<h1>Контакты</h1> <p>свяжитесь с нами</p>"



@app.route("/greet",methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"<h1>Приятно {name}</h1>"
    return '''
        <form method="post">
            <input name = "name" placeholder = "Как вас зовут?">
            <button>Отправить</button>
            </form>
            '''
app.run(debug=True)
