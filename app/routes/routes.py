from flask import render_template
from app import app

@app.route("/")
def home():
    return render_template("app/home.html")

@app.route("/home_main")
def home_main():
    return render_template("app/home_main.html")


@app.route("/ai_solutions")
def ai():
    return render_template("app/ai_solutions.html")

@app.route("/cybersecurity")
def cyber():
    return render_template("app/cybersecurity.html")

@app.route("/it_solutions")
def it_solution():
    return render_template("app/it_solutions.html")

@app.route("/software")
def software():
    return render_template("app/software.html")

@app.route("/agency")
def agency():
    return render_template("app/agency.html")

@app.route("/about")
def about():
    return render_template("app/about.html")

@app.route("/pages")
def pages():
    return render_template("app/pages.html")

@app.route("/team")
def team():
    return render_template("app/team.html")

@app.route("/service")
def service():
    return render_template("app/service.html")

@app.route("/choose")
def choose():
    return render_template("app/choose.html")

@app.route("/testimonial")
def testimonial():
    return render_template("app/testimonial.html")

@app.route("/price")
def price():
    return render_template("app/price.html")

@app.route("/login_register")
def login_register():
    return render_template("app/login_register.html")

@app.route("/blog")
def blog():
    return render_template("app/blog.html")

@app.route("/blog_grid")
def blog_grid():
    return render_template("app/blog_grid.html")

@app.route("/blog_standart")
def blog_standart():
    return render_template("app/blog_standart.html")

@app.route("/blog_detail")
def blog_detail():
    return render_template("app/blog_detail.html")

@app.route("/contact")
def contact():
    return render_template("app/contact.html")

@app.route("/study")
def study():
    return render_template("app/study.html")

@app.route("/news")
def news():
    return render_template("app/news.html")