class User:
    '''
    News class to define News sources Objects
    '''

    def __init__(self, id, content, author):
        self.id = id
        self.content = content
        self.author = author


class Pitch:
    '''
    Headlines to define News articles class
    '''

    def __init__(self, source, author, title, description, publishedAt, url, urlToImage):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.url = url
        self.urlToImage = urlToImage
        