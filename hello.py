from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():   
    return "hello world"

# @app.route('/pawan')
# def hello():
#     name = "Monkey D. Luffy"   
#     return render_template('about.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)
