from js import document, window
import pyodide

global _style_elem
_style_elem = None

styles = []

class Tag:
    """HTML tag clisd.py object"""
    def __init__(self, name : str, *content, _class : str="", events=None, **attrs):
        self.name = name
        self.content = content

        self.events = events if events else []

        self.attrs = attrs
        if _class: self.attrs["class"] = _class

    def render(self, tag=None):
        if not tag:
            tag = self

        self.element = document.createElement(tag.name)

        for i, j in tag.attrs.items():
            self.element.setAttribute(str(i), str(j))

        for i in tag.events:
            i.apply(self.element)

        for i in tag.content:
            if isinstance(i, Tag):
                self.element.appendChild(i.render())
            else:
                self.element.innerHTML += str(i)

        return self.element

class Component(Tag):
    """Clisd.py component object"""

    def __init__(self): pass

    def render(self):
        return super().render(tag=self._render())

class State:
    """Dynamic state for clisd.py components"""
    def __init__(self, component, value, auto_render=True):
        self.component = component
        self._value = value
        self.auto_render = auto_render

    def set(self, value):
        self._value = value
        if self.auto_render:
            elem = self.component.element
            elem.parentNode.replaceChild(self.component.render(), elem)
            styles[0:] = []

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        self.set(value)


def div(*args, **kwargs): return Tag("div", *args, **kwargs)
def p(*args, **kwargs): return Tag("p", *args, **kwargs)
def pre(*args, **kwargs): return Tag("pre", *args, **kwargs)
def span(*args, **kwargs): return Tag("span", *args, **kwargs)
def img(**kwargs): return Tag("img", "", **kwargs)
def input(**kwargs): return Tag("input", "", **kwargs)
def button(*args, **kwargs): return Tag("button", *args, **kwargs)
def textarea(*args, **kwargs): return Tag("textarea", *args, **kwargs)
def table(*args, **kwargs): return Tag("table", *args, **kwargs)
def tbody(*args, **kwargs): return Tag("tbody", *args, **kwargs)
def th(*args, **kwargs): return Tag("th", *args, **kwargs)
def tr(*args, **kwargs): return Tag("tr", *args, **kwargs)
def td(*args, **kwargs): return Tag("td", *args, **kwargs)
def a(*args, **kwargs): return Tag("a", *args, **kwargs)
def h1(*args, **kwargs): return Tag("h1", *args, **kwargs)
def h2(*args, **kwargs): return Tag("h2", *args, **kwargs)
def h3(*args, **kwargs): return Tag("h3", *args, **kwargs)
def h4(*args, **kwargs): return Tag("h4", *args, **kwargs)
def h5(*args, **kwargs): return Tag("h5", *args, **kwargs)
def h6(*args, **kwargs): return Tag("h6", *args, **kwargs)
def strong (*args, **kwargs): return Tag("strong", *args, **kwargs)
def em(*args, **kwargs): return Tag("em", *args, **kwargs)
def i(*args, **kwargs): return Tag("i", *args, **kwargs)
def br(**kwargs): return Tag("br", "", **kwargs)
def ul(*args, **kwargs): return Tag("ul", *args, **kwargs)
def ol(*args, **kwargs): return Tag("ol", *args, **kwargs)
def li(*args, **kwargs): return Tag("li", *args, **kwargs)


class Event:
    """Clisd.py event object"""
    def __init__(self, event, action = lambda e: None):
        self.event = event
        self.action = action

    def apply(self, target):
        target.addEventListener(self.event, pyodide.create_proxy(self.action))

def relative(link : str):
    """Convert relative link to absolute"""

    return f"#{document.URL.split('#')[1]}/{link}"

def anchor(id : str):
    if id[0] == "#":
        id = id[1:]

    return f"#{document.URL.split('#')[1]}#{id}"

def render_page(dom : Tag):
    """Renders dom to screen, change styles"""
    global _style_elem

    document.body.innerHTML = ""
    document.body.appendChild(dom.render())

    if not _style_elem:
        _style_elem = document.createElement("style")

    _style_elem.innerHTML = "\n".join(styles)
    styles[0:] = []

    document.head.appendChild(_style_elem)
    

def route(route : dict, filter=lambda x : x):
    """Routes links in clisd.py"""
    def route_link(e, page=None, _route=route):
        route =_route
        if page:
            url = page
        else:
            try:
                url = document.URL.split("#")[1]
            except IndexError:
                url = "/"

        if url:
            if url[0] == "/" or url[0] == "\\":
                url = url[1:]
        if url:
            if url[-1] == "/" or url[-1] == "\\":
                url = url[:-1]

        url_parts = []
        for i in url.split("/"):
            if "\\" not in i:
                url_parts.append(i)
            else:
                for j in i.split("\\"):
                    url_parts.append(j)

        url_parts = url_parts if url_parts else [""]

        lvl = route.get(url_parts[0], None)

        if not lvl and None not in route:
            return render_page(p("Error 404 : Page not found"))

        if isinstance(lvl, dict):
            route_link(None, page="/".join(url_parts[1:] if url_parts[1:] else "/"), _route=lvl)
        else:
            render_page(filter(lvl()))

    window.addEventListener("hashchange", pyodide.create_proxy(route_link))
    route_link(None)