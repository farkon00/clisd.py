from js import document

class Tag:
    """HTML tag object"""
    def __init__(self, name : str, *content, _class : str="", **attrs):
        self.name = name
        self.content = content
        self.attrs = attrs
        if _class: self.attrs["class"] = _class

    def render(self):
        return \
f"""
<{self.name}
    {' '.join([f'{i}="{j}"' for i, j in self.attrs.items()])}>{''.join([i.render() if isinstance(i, Tag) else i for i in self.content])}
</{self.name}>
""".replace("\\n", "")

def div(*args, **kwargs): return Tag("div", *args, **kwargs)
def p(*args, **kwargs): return Tag("p", *args, **kwargs)
def span(*args, **kwargs): return Tag("span", *args, **kwargs)
def img(**kwargs): return Tag("img", "", **kwargs)
def a(*args, **kwargs): return Tag("a", *args, **kwargs)
def br(**kwargs): return Tag("br", "", **kwargs)
def ul(*args, **kwargs): return Tag("ul", *args, **kwargs)
def ol(*args, **kwargs): return Tag("ol", *args, **kwargs)
def li(*args, **kwargs): return Tag("li", *args, **kwargs)

def render_body(dom : Tag, styles=[]):
    document.body.innerHTML = dom.render()
    style = "<style>" + "\n".join(styles) + "</style>"
    document.head.innerHTML += style