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
    access_key = 'EAAI2NU5TZAnEBAJ4ynZCA4t1y2Rl3aJclQnj3BVjrjGjKlQIUefyZCDjiSg8TbtFZAgRUbkHV8Ek2rXpJQpa6G3ec7s6JSToRC5Lb4jnKsMLhulvPPmsDFIRo34xfrZAButlhiatMSCBIgYhulqCrdb4XddgJOrJIFYbup8E8M5AQZCHtl3Q1IRHEByJAs65RGdYqNvwZAevgZDZD'
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
        msg = f'#Confession{num}\n{msg}'
        post_on_page(msg)

    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)



