from flask import Flask, render_template
import random

app = Flask(__name__)

books = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "mood": "inspirational"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "mood": "thoughtful"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "mood": "romantic"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "mood": "melancholic"},
    {"title": "1984", "author": "George Orwell", "mood": "intense"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "mood": "tragic"},
    {"title": "Harry Potter and the Sorcerer's Stone", "author": "J.K. Rowling", "mood": "adventurous"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "mood": "adventurous"},
    {"title": "The Road", "author": "Cormac McCarthy", "mood": "dark"},
    {"title": "Life of Pi", "author": "Yann Martel", "mood": "survival"},
    {"title": "The Book Thief", "author": "Markus Zusak", "mood": "thoughtful"},
    {"title": "The Fault in Our Stars", "author": "John Green", "mood": "romantic"},
    {"title": "The Girl on the Train", "author": "Paula Hawkins", "mood": "suspenseful"},
    {"title": "The Night Circus", "author": "Erin Morgenstern", "mood": "magical"},
    {"title": "Gone Girl", "author": "Gillian Flynn", "mood": "suspenseful"},
    {"title": "The Hunger Games", "author": "Suzanne Collins", "mood": "thrilling"},
    {"title": "The Handmaid's Tale", "author": "Margaret Atwood", "mood": "dystopian"},
    {"title": "The Martian", "author": "Andy Weir", "mood": "survival"},
    {"title": "The Kite Runner", "author": "Khaled Hosseini", "mood": "heart-wrenching"},
    {"title": "The Shining", "author": "Stephen King", "mood": "horror"},
    {"title": "Little Women", "author": "Louisa May Alcott", "mood": "nostalgic"},
    {"title": "Moby Dick", "author": "Herman Melville", "mood": "intense"},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "mood": "tragic"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "mood": "romantic"},
    {"title": "Frankenstein", "author": "Mary Shelley", "mood": "gothic"},
    {"title": "Dracula", "author": "Bram Stoker", "mood": "gothic"},
    {"title": "The Odyssey", "author": "Homer", "mood": "epic"},
    {"title": "The Iliad", "author": "Homer", "mood": "epic"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "mood": "philosophical"},
    {"title": "Brave New World", "author": "Aldous Huxley", "mood": "dystopian"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "mood": "dark"},
    {"title": "The Secret Garden", "author": "Frances Hodgson Burnett", "mood": "uplifting"},
    {"title": "Anne of Green Gables", "author": "L.M. Montgomery", "mood": "nostalgic"},
    {"title": "The Chronicles of Narnia", "author": "C.S. Lewis", "mood": "fantasy"},
    {"title": "Percy Jackson & the Olympians", "author": "Rick Riordan", "mood": "adventurous"},
    {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "mood": "humorous"},
    {"title": "The Giver", "author": "Lois Lowry", "mood": "thoughtful"},
    {"title": "Ender's Game", "author": "Orson Scott Card", "mood": "thrilling"},
    {"title": "Dune", "author": "Frank Herbert", "mood": "epic"},
    {"title": "A Game of Thrones", "author": "George R.R. Martin", "mood": "epic"},
    {"title": "The Da Vinci Code", "author": "Dan Brown", "mood": "mysterious"},
    {"title": "Memoirs of a Geisha", "author": "Arthur Golden", "mood": "romantic"},
    {"title": "The Wind-Up Bird Chronicle", "author": "Haruki Murakami", "mood": "surreal"},
    {"title": "American Gods", "author": "Neil Gaiman", "mood": "mythical"},
    {"title": "The Color Purple", "author": "Alice Walker", "mood": "empowering"},
    {"title": "The Lovely Bones", "author": "Alice Sebold", "mood": "tragic"},
    {"title": "The Bell Jar", "author": "Sylvia Plath", "mood": "melancholic"},
    {"title": "Beloved", "author": "Toni Morrison", "mood": "heart-wrenching"},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel Garcia Marquez", "mood": "magical"},
]

mood_books = {
    'inspirational': [],
    'thoughtful': [],
    'romantic': [],
    'melancholic': [],
    'intense': [],
    'tragic': [],
    'adventurous': [],
    'dark': [],
    'survival': [],
    'suspenseful': [],
    'magical': [],
    'thrilling': [],
    'dystopian': [],
    'nostalgic': [],
    'gothic': [],
    'epic': [],
    'philosophical': [],
    'humorous': [],
    'fantasy': [],
    'mysterious': [],
    'surreal': [],
    'mythical': [],
    'empowering': [],
    'heart-wrenching': [],
    'horror': [],
    'uplifting': [],
}

# Populate mood_books with books
for book in books:
    mood_books[book['mood'].lower()].append(f"{book['title']} by {book['author']}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mood/<string:mood>')
def get_recommendations(mood):
    mood_lower = mood.lower()
    if mood_lower in mood_books:
        recommended_books = random.sample(mood_books[mood_lower], min(2, len(mood_books[mood_lower])))
    else:
        recommended_books = []
    return render_template('recommendations.html', mood=mood.capitalize(), books=recommended_books)

if __name__ == '__main__':
    app.run(debug=True)
