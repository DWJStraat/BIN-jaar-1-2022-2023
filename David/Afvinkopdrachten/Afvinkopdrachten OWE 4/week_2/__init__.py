import secrets

from flask import Flask, render_template, redirect, url_for, session
from flask_bootstrap import Bootstrap5

from dna_convert import dna_convert
from forms import *
from student_db import handler as student_db_handler
from sequence_identifier import sequence_identifier

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)
app.secret_key = app.config['SECRET_KEY']

bootstrap = Bootstrap5(app)
# csrf = CSRFProtect(app)





@app.route('/dna_to_prot', methods=['GET', 'POST'])
def index():
    form = DNAForm()
    message = ''
    if form.validate_on_submit():
        dna = form.dna.data.upper()
        return render_template('dna_to_prot.html', form=form, message=dna_convert(dna))
    return render_template('dna_to_prot.html', form=form, message=message)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student_db_login', methods=['GET', 'POST'])
def student_db_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        session["username"] = username
        session["password"] = password
        return redirect(url_for('student_db'))
    return render_template('log_in.html', form=form)

@app.route('/student_db', methods=['GET', 'POST'])
def student_db():
    try:
        username = session["username"]
        password = session["password"]
        form = StudentForm()
        if form.validate_on_submit():
            id = form.student_id.data
            student = student_db_handler(username, password, id)
            return render_template('student_db.html', username = username, form = form,
                                   student_nr = student["student_nr"], name = student["name"],
                                   geb_datum = student["geb_datum"], woonplaats = student["woonplaats"],
                                   email = student["email"], telefoon = student["telefoon"],
                                   klas = student["klas"], slber = student["slber"])
        return render_template('student_db.html', username = username, form = form)
    except KeyError:
        return redirect(url_for('student_db_login'))
    except Exception as e:
        return render_template('student_db.html', username = username, form = form, message = "Incorrect login")

@app.route('/identifier', methods=['GET', 'POST'])
def identifier():
    form = IdentifierForm()
    message = ''
    if form.validate_on_submit():
        sequence = form.sequence.data.upper()
        output = sequence_identifier(sequence)
        return render_template('identifier.html', form=form, dna=output["DNA"], rna=output["RNA"],
                               protein=output["Protein"], type = output["Type"])
    return render_template('identifier.html', form=form, message=message)

if __name__ == '__main__':
    app.run(debug=True)