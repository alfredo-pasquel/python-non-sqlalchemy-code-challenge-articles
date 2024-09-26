class Article:
    all = []

    def __init__(self, author, magazine, title):
        
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string and between 5 and 50 characters long.")
        
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        
        self._author = author
        self._magazine = magazine
        self._title = title
        
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of the Magazine class.")
        self._magazine = new_magazine
    
    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of the Author class.")
        self._author = new_author

class Author:

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([article.magazine.category for article in self.articles()]))

class Magazine:
    all_magazines = []

    def __init__(self, name, category):

        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        
        Magazine.all_magazines.append(self)
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters long.")
        self._name = new_name
    
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    
    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]
    
    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author in author_counts:
                author_counts[author] += 1
            else:
                author_counts[author] = 1
        
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
