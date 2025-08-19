from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=100)])
    content = TextAreaField("Content", validators=[DataRequired(), Length(min=10)])
    author = StringField("Author", validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField("Submit")
