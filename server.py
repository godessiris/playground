from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html", color= "cornflowerblue", times=3)

@app.route('/play/<x>')
def repeat(x):
  
    return render_template('index.html',color="cornflowerblue", times= int(x))

@app.route('/play/<x>/<color>')
def color(x,color):
    return render_template('index.html', color= color, times = int(x))
    


if __name__== "__main__":
    app.run(debug=True)

