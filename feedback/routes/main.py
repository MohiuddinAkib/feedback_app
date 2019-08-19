from feedback.extensions import db
from feedback.models import Feedback
from feedback.forms import FeedbackForm
from flask import Blueprint, render_template, jsonify, request, redirect, flash, url_for

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    form = FeedbackForm()
    return render_template('index.html', form=form)


@main.route('/submit', methods=['POST'])
def submit():
    form = FeedbackForm(request.form)
    if form.validate_on_submit():
        data = form.data
        feedback = Feedback(data['customer_name'], data['dealer'],
                            data['rating'], data['comments'])
        db.session.add(feedback)
        db.session.commit()
        feedback.send_email()
        flash('Your feedback was succesfully submitted')
        return redirect(url_for('main.success'))
    else:
        flash(form.errors, 'error')
        return render_template('index.html', form=form)


@main.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
