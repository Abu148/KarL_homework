class Post:
    def __init__(self,title,content,author):
        self.title = title
        self.content = content
        self.author = author 
    
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"
    

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(post)

    def display_posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(post) 


def main():
    blog = Blog() 

    while True:
        print("\nSimple Blog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete a Post")
        print("5. Edit a Post")
        print("6. Display Latest Posts")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter title: ")
            content = input("Enter content: ")
            author = input("Enter author: ")
            blog.add_post(Post(title, content, author))
            print("Post added successfully!")
        
        elif choice == "2":
            blog.list_all_posts()
        
        elif choice == "3":
            author = input("Enter author name: ")
            blog.display_posts_by_author(author)
        
        elif choice == "4":
            title = input("Enter the title of the post to delete: ")
            blog.posts = [post for post in blog.posts if post.title != title]
            print("Post has been deleted successfully!")
        
        elif choice == "5":
            title = input("Enter the title of the post to edit: ")
            for post in blog.posts:
                if post.title == title:
                    post.content = input("Enter new content: ")
                    print("Post updated successfully!")
                    break
            else:
                print("Post not found!")

        elif choice == "6":
            if blog.posts:
                print(blog.posts[-1])
            else:
                print("No posts available.")
        
        elif choice == "7":
            print("Exiting")
            break

        else:
            print("Incorrect choice, Please try again.")

if __name__ == "__main__":
    main() 
