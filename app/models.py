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

    def __init__(self, id, title, description, url, urlToImage, publishedAt):
        self.id = id
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt