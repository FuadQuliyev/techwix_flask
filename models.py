from run import db

class HomeLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    icon = db.Column(db.String(50))
    sublink = db.relationship('SubLink', backref='homelink', lazy=True)

class SubLink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_name = db.Column(db.String(100), unique=True, nullable=False)
    sub_url = db.Column(db.String(200), unique=True, nullable=False)
    homelink_id = db.Column(db.ForeignKey('homelink.id'), nullable=False) 

class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100), nullable=False)
    month = db.Column(db.Integer(3), nullable=False)
    credit = db.Column(db.Integer(10), nullable=False)

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    icon = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)

class About(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    about_url = db.Column(db.String(100), nullable=False)
    about_image = db.relationship('AboutImage', backref='about', lazy=True)

class AboutImage(db.Model):
    image = db.Column(db.String(100), nullable=False)
    about_id = db.Column(db.ForeignKey('about.id'), nullable=False)

class Statictic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Integer(10), nullable=False)
    icon = db.Column(db.String(100), nullable=False)

class Choose(db.Model):
    image = db.Column(db.String(200), nullable=False)
    choose_url = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)

class Skill(db.Model):
    skill_name = db.Column(db.String(100), nullable=False)
    performance = db.Column(db.Integer(5), nullable=False)

class Study(db.Model):
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.Integer(100), nullable=False)
    text = db.Column(db.Text(), nullable=False)
    study_url = db.Column(db.String(100), nullable=False)

class Testimonial(db.Model):
    image = db.Column(db.String(200), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

class Brand(db.Model):
    image = db.Column(db.String(200), nullable=False)

class Team(db.Model):
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    person_url = db.Column(db.String(200), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    team_social = db.relationship('TeamSocial', backref='team', lazy=True)

class TeamSocial(db.Model):
    icon = db.Column(db.String(200), nullable=False)
    icon_url = db.Column(db.String(200), nullable=False)
    team_id = db.Column(db.ForeignKey('team.id'), nullable=False)


class News(db.Model):
    image = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    name_url = db.Column(db.String(200), nullable=False)
    title = db.Column(db.String(50), nullable=False)
    news_url = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date(), nullable=False)
    month = db.Column(db.Date(), nullable=False)
