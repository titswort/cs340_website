from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.fields.core import FloatField, IntegerField
from wtforms.fields.simple import HiddenField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class AddMutualFundsForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    dollars = FloatField('dollars',validators=[DataRequired()])
    total_mf_sector = FloatField('total_mf_sector',validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class AddStocksForm(FlaskForm):
    ticker_symbol = StringField('ticker_symbol', validators=[DataRequired()])
    legal_name = StringField('legal_name', validators=[DataRequired()])
    total_shares = FloatField('total_shares',validators=[DataRequired()])
    current_price = FloatField('current_price',validators=[DataRequired()]) 
    submit = SubmitField('Submit')

