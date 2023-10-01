from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for books and reservations
books = [
    {"id": 1, "title": "Romeo and Juliet", "author": "William Shakespeare", "available": 5},
    {"id": 2, "title": "Harry Potter", "author": "J.K Rowling", "available": 3},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee", "available": 2},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "available": 7},
    {"id": 5, "title": "The Catcher in the Rye", "author": " J. D. Salinger", "available": 0},
    {"id": 6, "title": "Wuthering Heights", "author": "Emily Brontë", "available": 4},
    {"id": 7, "title": "Nineteen Eighty-Four", "author": "George Orwell", "available": 6},
    {"id": 8, "title": "The Adventures of Huckleberry Finn", "author": "Mark Twain", "available": 1},
    {"id": 9, "title": "Pride and Prejudice", "author": "Jane Austen", "available": 5},
]

reservations = []

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/reservations')
def list_reservations():
    return render_template('reservations.html', reservations=reservations)

@app.route('/reserve', methods=['POST'])
def reserve():
    book_id = int(request.form.get('book_id'))
    quantity = int(request.form.get('quantity'))
    name = request.form.get('name')  # Get the name from the form

    book = next((b for b in books if b['id'] == book_id), None)

    if book and book['available'] >= quantity:
        book['available'] -= quantity
        reservations.append({'book_id': book_id, 'quantity': quantity, 'name': name})
        return 'Reservation successful!'
    else:
        return 'Reservation failed. Not enough available copies.'

if __name__ == '__main__':
    app.run(debug=True)
