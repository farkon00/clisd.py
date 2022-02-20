from js import document, window
import pyodide

global _style_elem
_style_elem = None

styles = []

class Tag:
    """HTML tag object"""
    def __init__(self, name : str, *content, _class : str="", **attrs):
        self.name = name
        self.content = content
        self.attrs = attrs
        if _class: self.attrs["class"] = _class

    def render(self):
        self.element = document.createElement(self.name)
        for i, j in self.attrs.items():
            self.element.setAttribute(str(i), str(j))

        for i in self.content:
            if isinstance(i, Tag):
                self.element.appendChild(i.render())
            else:
                self.element.innerHTML += str(i)

        return self.element

def div(*args, **kwargs): return Tag("div", *args, **kwargs)
def p(*args, **kwargs): return Tag("p", *args, **kwargs)
def span(*args, **kwargs): return Tag("span", *args, **kwargs)
def img(**kwargs): return Tag("img", "", **kwargs)
def a(*args, **kwargs): return Tag("a", *args, **kwargs)
def br(**kwargs): return Tag("br", "", **kwargs)
def ul(*args, **kwargs): return Tag("ul", *args, **kwargs)
def ol(*args, **kwargs): return Tag("ol", *args, **kwargs)
def li(*args, **kwargs): return Tag("li", *args, **kwargs)

def render_page(dom : Tag):
    global _style_elem

    document.body.innerHTML = ""
    document.body.appendChild(dom.render())

    if not _style_elem:
        _style_elem = document.createElement("style")

    _style_elem.innerHTML = "\n".join(styles)
    styles[0:] = []

    document.head.appendChild(_style_elem)
    

def route(route : dict):
    def route_link(e):
        try:
            url = document.URL.split("#")[1]
        except IndexError:
            url = "/"

        try:
            if url:
                if url[0] == "/":
                    url = url[1:]

            lvl = route[url.split("/")[0]]
        except Exception:
            return render_page(p("Error 404 : Page not found"))

        if isinstance(lvl, dict):
            route("/".join(url.split("/")[1:]))
        else:
            render_page(lvl())

    window.addEventListener("hashchange", pyodide.create_proxy(route_link))
    route_link(None)