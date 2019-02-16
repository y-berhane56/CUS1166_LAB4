import os
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import *

app = Flask(name)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    courses = Course.query.all()
    return render_template("index.html", courses=courses)

@app.route('/register_student/<int:course_id>', methods=["GET", "POST"])
def register(course_id):
    course = Course.query.get(course_id)
    if request.method == 'POST':
        name = request.form.get("name")
        seat = request.form.get("seat")
        # Use the utility method to add a new passenger in the database.
        flight.add_passenger(name,seat)
        # Use the relationships field in the flights model to retrieve
        # all passengers in the current flight.
        students = course.students
    return render_template("course_details.html", course=course, registeredstudent=registeredstudent)

@app.route('/add_course', methods=["POST"])
def add_course():
    courseno = request.form.get("coursenumber")
    coursetitle = request.form.get("coursetitle")
    course = Course(courseno=courseno, coursetitle=coursetitle)
    db.session.add(course)
    db.session.commit()
    courses = Course.query.all()
    return render_template('index.html', courses=courses)
