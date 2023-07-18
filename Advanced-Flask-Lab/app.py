from flask import Flask, jsonify, request, render_template, url_for
import random
import requests, json

app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Variables for tasks
image_link = "https://uploads-ssl.webflow.com/5dd64bd3a930f9d04abd1363/5de254f85f1762feee30d664_meet_logo_red.png"

user_bio = "Ryan Thomas Gosling is a Canadian actor. Prominent in both independent film and major studio features of varying genres, his films have accrued a worldwide box office gross of over 1.9 billion USD. "

posts = {
    "https://i.imgur.com/1dSgGnG.png": "The cohort of 2022!",
    "https://i.imgur.com/CPEvMk0.jpg": "MEET graduation!",
    "https://i.imgur.com/Cb7LK9o.jpg": "#MEET_HACKATHON",
    "https://i.imgur.com/S5A93Wt.jpg": "Class of 2024's Y1 closing event cohort"}


#####


@app.route('/')  # '/' for the default page
def home():
    return render_template('index.html',link = image_link ,userbio = user_bio,  posts = posts)


@app.route('/about')  # '/' for the default page
def about():
    return render_template('about.html')


if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
