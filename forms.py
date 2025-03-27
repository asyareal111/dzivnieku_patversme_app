from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import SubmitField

class UploadCSVForm(FlaskForm):
    file = FileField('CSV File', validators=[FileRequired()])
    submit = SubmitField('Upload')