from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
#from flask_login import LoginManager, login_user, login_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customers.db'
db = SQLAlchemy(app)
#login_manager = LoginManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(300), nullable = False)
    '''
    def __repr__(self):
        return '<Article %r' %self.id
        '''
    
#class UserLogin():
#    def fromDB(self, user_id, db):
#        
##        self.__user = User.query.filter_by(id = user_id).all()[0]
#        for i in db.query.all():
#            if (i.id == user_id):
#                self.__user == i
#                break
#        return self
#    def create(self, user):
#        self.__user = user
#        return self
#    def is_authenticated(self):
#        return True
#    def is_active(self):
#        return True
#    def is_anonymous(self):
#        return False
#    def get_id(self):
#        return str(self.__user.id)
#    
#@login_manager.user_loader
#def load_user(user_id):
#    return UserLogin().fromDB(user_id, db)
#    

@app.route('/')
def index():
    print(db.session.query(User).filter(User.email == '1').all())
    #print(db.session.query(User).filter(User.id == 1).one())
    return render_template("index.html")
'''
@app.route('/about')
#@login_required
def about():
    return render_template("about.html")
'''


@app.route('/create-account', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        tit = request.form['title']
        hashe = generate_password_hash(request.form['intro'])
        user = User(email = tit, password = hashe)
        for i in User.query.all():
           if (i.email == tit):
               return "уже зарег"
        # if (len(db.query.filter_by(email = tit).all()) > 0):
        #     return "уже зарег"
        try:
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except:
            return "mistake"
    else:
        return render_template("create-account.html")

    
@app.route('/login', methods = ["POST", "GET"])
def login():
    if (request.method == "POST"):
        tit = request.form['title1']
        passw = request.form['intro1']
#        user = User(email = tit, password = passw)
        
        for i in User.query.all():
            if (check_password_hash(i.password, passw) and i.email == tit):
#                userlogin = UserLogin().create(user)
#                login_user(userlogin)
                return redirect('/')
        return "mistake"
    else:
        return render_template("login.html")

 
if __name__ == '__main__':
    
    app.run()
