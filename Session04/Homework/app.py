import mlab
from flask import Flask, render_template, request
from mongoengine import *
from faker import Faker


app = Flask(__name__)

#connect to mlab file
mlab.connect()



class Booklist(Document):
    book_name = StringField()
    author = StringField()
    description = StringField()
    image = StringField()
    rating = FloatField()


# f = Faker ()
#
# for _  in range (20):
#     g = Girl(   name = f.name(),
#                 image = "https://source.unsplash.com/500x300/?girl",
#                 description = f.text(),
#                 rating = 4.1   )
#     g.save()

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == "GET":
        return render_template('admin.html' , books = Booklist.objects())



@app.route('/<int:id>', methods=['POST'])
def delete_book(id):
    form=request.form
    book_id = form['book_id']
    Booklist.objects( _id = book_id).delete()
    return "Deleted"






@app.route('/add-book', methods=['GET', 'POST'])
def add_book():
    if request.method == "GET":
        return render_template('add-book.html')
    elif request.method == "POST":
        form = request.form
        book_name = form['book_name']
        author = form['author']
        description = form['description']
        image = form['image']
        rating = form['rating']
        booklist = Booklist(book_name = book_name, author = author, image = image, description = description, rating = rating)
        booklist.save()
        return "Added"



@app.route('/')
def index():

    return render_template('homepage.html')


@app.route('/books-page')
def girl_page():
    book = Booklist.objects()
    return render_template('books-page.html', books = book)



if __name__ == '__main__':
  app.run(debug=True)
