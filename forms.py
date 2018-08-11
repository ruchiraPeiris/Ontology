from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo
from flask_wtf import FlaskForm


class FindPhoneForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 64)])
    phone_brand = StringField('PhoneBrand', validators=[DataRequired(), Length(3, 64)])

    phone_type = BooleanField('Brand New')
    submit = SubmitField('Find Phone')
