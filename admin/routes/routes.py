from flask import render_template
from admin import admin

@admin.route("/")
def home():
    return render_template("admin/admin.html")

@admin.route("/home_links")
def home_links():
    return render_template("admin/home_links.html")

@admin.route("/service")
def service():
    return render_template("admin/service.html")

@admin.route("/about")
def about():
    return render_template("admin/about.html")

@admin.route("/statistic")
def statistic():
    return render_template("admin/statistic.html")

@admin.route("/choose")
def choose():
    return render_template("admin/choose.html")

@admin.route("/skill")
def skill():
    return render_template("admin/skill.html")

@admin.route("/study")
def study():
    return render_template("admin/study.html")

@admin.route("/testimonial")
def testimonial():
    return render_template("admin/testimonial.html")

@admin.route("/brand")
def brand():
    return render_template("admin/brand.html")

@admin.route("/team")
def team():
    return render_template("admin/team.html")

@admin.route("/news")
def news():
    return render_template("admin/news.html")