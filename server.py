from flask import Flask, flash, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

def setSession():
    session['num'] = random.randint(1,100)

@app.route('/')
def index():
    if 'num' not in session:
        setSession()
    print (session['num'])
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def checkNumber():
    if 'num' not in session:
        setSession()
    print (session['num'])
    return redirect('/')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    def reset():
        setSession()
    return redirect('/')

app.run(debug=True)