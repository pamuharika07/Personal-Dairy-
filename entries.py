
from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from models import Entry
from app import db

entries_bp = Blueprint('entries', __name__)

@entries_bp.route('/', methods=['GET','POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        entry = Entry(
            title=request.form['title'],
            content=request.form['content'],
            user_id=current_user.id
        )
        db.session.add(entry)
        db.session.commit()
        return redirect('/')

    entries = Entry.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', entries=entries)
