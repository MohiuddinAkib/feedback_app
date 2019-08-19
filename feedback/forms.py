from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class FeedbackForm(FlaskForm):
    customer_name = StringField('Customer name', validators=[
                                DataRequired('Plesase enter customer name')])
    dealer = SelectField('Dealer', validators=[
        DataRequired('Plesase select your dealer')], choices=[
            ('', 'Select Value'),
            ('Tom Smith', 'Tom Smith'),
            ('Karen Swanson', 'Karen Swanson'),
            ('Jim Johnson', 'Jim Johnson'),
            ('Shauna Gifford', 'Shauna Gifford'),
    ])

    rating = RadioField(
        'Please rate your dealer',
        validators=[
            DataRequired('Please rate your dealer')
        ],
        choices=[
            ('1', 1),
            ('2', 2),
            ('3', 3),
            ('4', 4),
            ('5', 5),
            ('6', 6),
            ('7', 7),
            ('8', 8),
            ('9', 9),
            ('10', 10)
        ],
        render_kw={
            'style': 'list-style: none; display: flex; flex-direction: row; justify-content: space-between'
        },
        default=10
    )
    comments = TextAreaField('Customer name')
    submit = SubmitField(
        'Submit',
        render_kw={
            'class': 'btn'
        }
    )
