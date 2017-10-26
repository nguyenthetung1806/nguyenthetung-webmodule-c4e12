import mlab
from flask import Flask, render_template, request
from mongoengine import *
from faker import Faker

app = Flask(__name__)

#connect to mlab file
mlab.connect()

class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    rating = FloatField()

# mongoengine
# 1. Find record base on ID
# mongoengine lazy loading
# girl = Girl.objects().with_id('59e3342e7456e32cc4c79299')
# # 2. Delete
# if girl is None:
#     print("Not found")
# else:
#     girl.delete()


# f = Faker ()
#
# for _  in range (20):
#     g = Girl(   name = f.name(),
#                 image = "https://source.unsplash.com/500x300/?girl",
#                 description = f.text(),
#                 rating = 4.1   )
#     g.save()

@app.route('/admin')
def admin():
    return render_template('admin.html' , girls = Girl.objects())


@app.route('/add-girl', methods=['GET', 'POST'])
def add_girl():
    if request.method == "GET":
        return render_template('add_girl.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        image = form['image']
        description = form['description']
        girl = Girl(name=name, image=image, description=description, rating=4.1)
        girl.save()
        return "Added"


@app.route('/list')
def list_demo():
    n_lists = ['Huy', 'Tuấn Anh', 'Linh', 'Trường', 'Những người bạn khác']
    return render_template('girls_list.html',
        names = n_lists)

@app.route('/')
def index():

    return render_template('homepage.html')


@app.route('/girls_page')
def girl_page():
    girl_list = Girl.objects()
    return render_template('girls.html', girls = girl_list)


@app.route('/delete-girl/<girl_id>')
def delete_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if girl is None:
        return("Not found")
    else:
        girl.delete()
        return "Deleted " + girl_id



@app.route('/edit-girl/<girl_id>', methods=['GET', 'POST'])
def edit_girl(girl_id):
    if request.method == "GET":
        girl = Girl.objects().with_id(girl_id)

        return render_template('edit-girl.html', girl = girl )
    elif request.method == "POST":
        form = request.form
        name = form['name']
        image = form['image']
        description = form['description']
        rating = form['rating']
        Girl.objects().with_id(girl_id).update(name=name, image=image, description=description, rating = rating)
        return "Added"












if __name__ == '__main__':
  app.run(debug=True)
