from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    # need to check original app, it should already have the logic
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials!'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plot_chart')
def plot_chart():
    # if request.method == 'POST':
    #     # assuming there's a function that will ahndle the plotting - should check!
    #     # and the form will return all the values required to plot the chart
        
    return render_template('plot_chart.html')


if __name__ == '__main__':
    app.run(debug=True)