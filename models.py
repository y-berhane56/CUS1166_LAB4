from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_number = db.Column(db.String, nullable=False)
    course_title = db.Column(db.String, nullable=False)
    students = db.relationship("RegisteredStudent", secondary="coursestudent")

    #backref does two things. It creates a collection of objects of the RegisteredStudent and they can be reached by
    #the command ClassName.nameoftherelationship. It also allows you to reach the course for a student by calling
    #ClassName.nameofhteotherclass

class RegisteredStudent(db.Model):
    __tablename__ = "registeredstudents"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    courses = db.relationship("RegisteredStudent", secondary="coursestudent")

class CourseStudent(db.Model):
    __tablename__ = "coursestudent"
    id = db.Column(db.Integer, primary_key=True)
    registeredstudents_id = db.Column(db.Integer, db.ForeignKey('registeredstudents.id'), primary_key=True)
    courses_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    course = db.relationship(Course, backref=backref("orders", cascade="all, delete-orphan"))
    registerdstudent = db.relationship(RegisteredStudent, backref=backref("orders", cascade="all, delete-orphan"))
