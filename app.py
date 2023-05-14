from flask import Flask,render_template,request,redirect

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

@app.route('/about/',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        print(request.form['text_1'])
        return '<h1>Some Error has occured!</h1>'
    else:
        return redirect('https://micvitc.github.io/')

if __name__ == "__main__":
    app.run(debug=True )   
