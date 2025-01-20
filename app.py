class Author:
    def __init__(self, name):
        self.name = name

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []

class Article:
    def __init__(self, title, author, magazine):
        self.title = title
        self.author = author
        self.magazine = magazine
        magazine.articles.append(self) 
        author.articles.append(self) 

# Create instances
author1 = Author("John Davi")
author2 = Author("Jane Sue")

magazine1 = Magazine("Science Weekly", "Science")
magazine2 = Magazine("Tech Trends", "Technology")

article1 = Article("Machinelearning Revolution", author1, magazine1)
article2 = Article("Quantum Computing", author2, magazine1)
article3 = Article("Blockchain Explained", author1, magazine2)

# Access and print information
print(f"Magazine: {magazine1.name}, Category: {magazine1.category}")
print("Articles in Science Weekly:")
for article in magazine1.articles:
    print(f"  - {article.title} by {article.author.name}")

print(f"Magazine: {magazine2.name}, Category: {magazine2.category}")
print("Articles in Tech Trends:")
for article in magazine2.articles:
    print(f"  - {article.title} by {article.author.name}")

print(f"Author: {author1.name}")
print("Articles by John Doe:")
for article in author1.articles:
    print(f"  - {article.title} in {article.magazine.name}")

print(f"Author: {author2.name}")
print("Articles by Jane Smith:")
for article in author2.articles:
    print(f"  - {article.title} in {article.magazine.name}")