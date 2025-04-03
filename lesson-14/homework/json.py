 json = [
    {
        "name": "John Doe",
        "age": 20,
        "grade": "A"
    },
    {
        "name": "Jane Smith",
        "age": 22,
        "grade": "B"
    }
]

#task1: 
import json
def read_students():
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
        
        for student in students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Grade: {student['grade']}")
            print('-' * 30)
    except FileNotFoundError:
        print("students.json file not found.")
if __name__ == "__main__":
    print("Student Details:")
    read_students()

#task2:
import requests

def fetch_weather(city):
    api_key = 'your_api_key_here'
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
  try:
        response = requests.get(complete_url)
        data = response.json()
      if data['cod'] == 200:
            main_data = data['main']
            weather_data = data['weather'][0]
            
            print(f"Weather in {city}:")
            print(f"Temperature: {main_data['temp']}°C")
            print(f"Humidity: {main_data['humidity']}%")
            print(f"Weather: {weather_data['description']}")
            print('-' * 30)
        else:
            print("City not found or invalid API key.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter city name: ")
    fetch_weather(city)

json2 = [
    {
        "title": "Book 1",
        "author": "Author 1",
        "year": 2001
    },
    {
        "title": "Book 2",
        "author": "Author 2",
        "year": 2005
    }
]

#task3: 
import json

def load_books():
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(books):
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    year = int(input("Enter the publication year: "))
    books.append({"title": title, "author": author, "year": year})
    save_books(books)
    print("Book added successfully!")

def update_book(books):
    title = input("Enter the book title to update: ")
    for book in books:
        if book['title'].lower() == title.lower():
            book['author'] = input("Enter the new author: ")
            book['year'] = int(input("Enter the new publication year: "))
            save_books(books)
            print("Book updated successfully!")
            return
    print("Book not found.")

def delete_book(books):
    title = input("Enter the book title to delete: ")
    for book in books:
        if book['title'].lower() == title.lower():
            books.remove(book)
            save_books(books)
            print("Book deleted successfully!")
            return
    print("Book not found.")

def print_books(books):
    if books:
        print("Books in library:")
        for book in books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
        print('-' * 30)
    else:
        print("No books found.")

def main():
    books = load_books()
    while True:
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. View Books")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            update_book(books)
        elif choice == '3':
            delete_book(books)
        elif choice == '4':
            print_books(books)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

#task4: 
import requests
import random

def fetch_movie_by_genre(genre):
    api_key = 'your_api_key_here'  # Replace with your API key
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"

    try:
        response = requests.get(url)
        data = response.json()

        if data['Response'] == 'True':
            movies = data['Search']
            random_movie = random.choice(movies)
            print(f"Recommended Movie: {random_movie['Title']}")
            print(f"Year: {random_movie['Year']}")
            print(f"IMDB ID: {random_movie['imdbID']}")
            print(f"Poster: {random_movie['Poster']}")
            print('-' * 30)
        else:
            print("No movies found for this genre.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    genre = input("Enter movie genre (e.g., Action, Comedy, Drama): ")
    fetch_movie_by_genre(genre)

if __name__ == "__main__":
    main()

