import mlab
from flask import Flask, render_template
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

# f = Faker ()
#
# for _  in range (20):
#     g = Girl(   name = f.name(),
#                 image = "https://source.unsplash.com/500x300/?girl",
#                 description = f.text(),
#                 rating = 4.1   )
#     g.save()


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


@app.route('/dict')
def dict_demo():
    dicts = {
    'name': 'Huỳnh Tuấn Kiệt',
    'image': 'http://www.tieuthien.com/wp-content/uploads/2016/10/hot-girl-gai-xinh-facebook-tieuthien.com-5.jpg'
    }
    return render_template('girls_dict.html',
        girl = dicts)


@app.route('/css-demo')
def css_demo():
    return render_template('css_demo.html')

@app.route('/test')
def test():
    return render_template('test.html')


if __name__ == '__main__':
  app.run(debug=True)
