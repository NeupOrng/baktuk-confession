import facebook
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///confession.db'
db = SQLAlchemy(app)

class NumPost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    num = db.Column(db.Integer)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    msg = db.Column(db.String(10000))

def get_count():
    counter = NumPost.query.filter_by(id=1).first()
    num = counter.num
    counter.num = num+1
    db.session.commit()
    return num

def post_on_page(msg):
    access_key = 'EAAKJEacCS9IBAEPDmGyht9P2jZAqVLDqbtL0dWpF4YbmSozxivxqpbeKQPECn1ZBP6zbufxPBIGHRxzUxSDca4bY7GkUUMNXMKuKjtHziAZAsZCJKkpVuJL7iPqDrBQZCcNDAmAMRZARZBw6x7fThn8OyDCEHA6ylkb58mSqP6ZAZBwZDZD'
    page_id = '102460761568034'

    fb = facebook.GraphAPI(access_key)

    fb.put_object(
        page_id,'feed',message=msg
    )


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('confession')
        num = get_count()
        msg = f'#BTConfession{num}\n{msg}'
        post_on_page(msg)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)



