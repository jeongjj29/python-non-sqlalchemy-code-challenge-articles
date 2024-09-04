class Article:

    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of the Magazine class.")
        if not (
            isinstance(title, str)
            and 5 <= len(title) <= 50
            and not hasattr(self, "title")
        ):
            raise Exception("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("Author must be an instance of the Author class.")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
        else:
            raise Exception("Magazine must be an instance of the Magazine class.")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if (
            isinstance(title, str)
            and 5 <= len(title) <= 50
            and not hasattr(self, "title")
        ):
            self._title = title
        else:
            raise Exception("Title cannot be changed.")


class Author:
    def __init__(self, name):
        if not (isinstance(name, str) and len(name) > 0 and not hasattr(self, "name")):
            raise Exception("Name must be a string greater than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0 and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception("Name cannot be changed.")

    def articles(self):
        return [
            article
            for article in Article.all
            if article.author == self and isinstance(article, Article)
        ]

    def magazines(self):
        return list(
            set(
                [
                    article.magazine
                    for article in self.articles()
                    if isinstance(article, Article)
                ]
            )
        )

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([article.magazine.category for article in self.articles()]))


class Magazine:
    def __init__(self, name, category):
        if not (isinstance(name, str) and 2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 charcters.")
        if not (isinstance(category, str) and len(category) > 0):
            raise Exception("Category must be a string longer than 0 charcters.")
        self._name = name
        self._category = category

    @classmethod
    def top_publisher(cls):
        if Article.all == []:
            return None

        articles_published = {}
        magazines = list(set([article.magazine for article in Article.all]))
        for magazine in magazines:
            articles_published[magazine] = len(
                [
                    article.magazine
                    for article in Article.all
                    if article.magazine == magazine
                ]
            )
        return max(articles_published, key=articles_published.get)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise Exception("Name must be a string between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            return
            # raise Exception("Category must be a string greater than 0 characters.")

    def articles(self):
        return [
            article
            for article in Article.all
            if article.magazine == self and isinstance(article, Article)
        ]

    def contributors(self):
        return list(
            set(
                [
                    article.author
                    for article in self.articles()
                    if isinstance(article, Article)
                ]
            )
        )

    def article_titles(self):
        if len(self.articles()) == 0:
            return None
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors_with_more_than_two_articles = []
        for contributor in self.contributors():
            if (
                len(
                    [
                        article
                        for article in contributor.articles()
                        if article.magazine == self
                    ]
                )
                > 2
            ):
                authors_with_more_than_two_articles.append(contributor)
        if authors_with_more_than_two_articles == []:
            return None
        return authors_with_more_than_two_articles
