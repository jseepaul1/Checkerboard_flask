from flask import Flask, render_template
app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route('/')
def index():
    return render_template("index.html", x=8, y=8, color1="red", color2="black")

# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route('/<int:x>')
def accept_columns(x):
    return render_template("index.html", x=x, y=8, color1="red", color2="black")

# NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:x>/<int:y>')
def accept_rows_and_columns(x, y):
    return render_template("index.html", x=x, y=y, color1="red", color2="black")

# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") 
# and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def accept_four_parmameters(x, y, color1, color2):
    return render_template("index.html", x=x, y=y, color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
