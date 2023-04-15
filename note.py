class Note:
    def __init__(self, title, content, summary):
        self.title = title
        self.content = content
        self.summary = summary

    def update(self, title=None, content=None, summary=None):
        if title is not None:
            self.title = title
        if content is not None:
            self.content = content
        if summary is not None:
            self.summary = summary

    def to_dict(self):
        return {'title': self.title, 'content': self.content, 'summary': self.summary}