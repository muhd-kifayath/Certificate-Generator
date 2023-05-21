from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login/')
def login_page():
    return render_template('login.html')

@app.route('/signup/')
def signup():
    return render_template('signup.html')

@app.route('/landing/')
def landing():
    return render_template('landing.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run(debug=True )   
