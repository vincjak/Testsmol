from flask import render_template, request
from app import app
from models import DataSchema

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    new_data = DataSchema(data)
    try:
        db.session.add(new_data)
        db.session.commit()
        return "Success", 200
    except:
        return "Failed", 400

@app.route('/data', methods=['GET'])
def get_data():
    data = DataSchema.query.all()
    return render_template('data.html', data=data)