from flask import render_template, request
from .models import DataSchema

def index():
    return render_template('index.html')

def save_data():
    data = request.form
    new_data = DataSchema(data)
    new_data.save()
    return render_template('index.html', message="Data saved successfully")

def get_data():
    data = DataSchema.query.all()
    return render_template('index.html', data=data)