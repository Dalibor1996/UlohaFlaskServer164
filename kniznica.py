from flask import Flask, jsonify, request

books = [
    {'id': 1, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald'},
    {'id': 2, 'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'}
]

app = Flask(__name__)

@app.route('/')
def home():
    return 'Nasa kniznica'

@app.route('/knihy/', methods=['GET'])
def get_books():
    return jsonify({'books': books})

@app.route('/knihy/', methods=['POST'])
def add_book():
    print(request)
    new_book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# @app.route('/books/<int:id>', methods=['GET'])
# def books(id):
#     # for i in id:
#     if id in id[books]:
#         return jsonify(books[id])

@app.route('/books/<int:id>', methods=['GET'])
def knihy(id):
    for book in books:
        if book['id'] == id:
            return jsonify(book)

if __name__ == "__main__":
    app.run()
