from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')
def level_1():
    return render_template('index.html',row=8, col=8, color_1='#904c77', color_2='#e49ab0')



@app.route('/<int:x>')
def row(x):
    return render_template('index.html',row=x, col=8, color_1='#904c77', color_2='#e49ab0')


@app.route('/<int:x>/<int:i>')
def col(x,i):
    return render_template('index.html',row=x, col=i, color_1='#904c77', color_2='#e49ab0')


#ALWAYS INCLUDE!! 
if __name__=="__main__":
    app.run(debug=True)