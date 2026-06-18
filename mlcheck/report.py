"""MLReport simple representation."""

class MLReport:
    def __init__(self, title: str = "ML Report"):
        self.title = title
        self.sections = []

    def add_section(self, name: str, content: dict):
        self.sections.append({"name": name, "content": content})

    def to_dict(self):
        return {"title": self.title, "sections": self.sections}
