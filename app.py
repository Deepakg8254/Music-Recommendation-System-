from flask import Flask , render_template, request
from nIN2 import *
import time


app = Flask (__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        user_genre = request.form['usergenre']
        number = int(request.form['number'])
        # Generate music recommendations based on the user's selected genre and number of songs
        # and store them in a variable called `recommendations`
        recommendations = main(user_genre,number)
        print(user_genre, number)
        print("---",recommendations)
        
        return render_template("index.html", recommendations=recommendations,validSentiList=validSentiList)
    else:
        return render_template("index.html",validSentiList=validSentiList)


if __name__ == "__main__":
    app.run(debug=True, port = 8000)

