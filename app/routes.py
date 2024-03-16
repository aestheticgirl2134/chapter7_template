from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    
   """Index URL"""
   return render_template('index.html',title='Index Page')             


@app.route('about-me')
def about_me():
      """About me URL"""
      return render_template('About_me.html,titlt=About Me Page')
