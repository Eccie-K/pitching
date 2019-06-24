class Source:
    '''
    News class to define News sources Objects
    '''

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


class Articles:
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
        