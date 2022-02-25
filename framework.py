from js import document, window
from types import FunctionType
import pyodide

global _style_elem
_style_elem = None

styles = []

# Lorem ipsum text
LOREM = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta labore vel aperiam sapiente iste eligendi molestiae\
     incidunt perferendis in minima dolorum, asperiores libero adipisci dolor quam ut ipsum ab est architecto at pariatur. Modi\
     architecto consectetur harum rerum nesciunt suscipit ex temporibus aperiam dignissimos, alias repellendus facilis libero\
     tempore fuga esse repudiandae cumque quidem nam! Dicta in, natus ipsam, magnam vel quam reiciendis ipsa culpa quibusdam nobis\
     laudantium quis. Aspernatur suscipit esse deleniti repudiandae molestias provident amet animi magni quam soluta, dicta\
     reprehenderit aut magnam vero nihil similique, quia obcaecati dolores consequuntur quidem quis error. Perferendis itaque, \
    adipisci dolorum quis voluptate illum quam rerum molestiae, atque excepturi consectetur autem. Repudiandae quas ullam saepe \
    fuga vitae at esse quibusdam tempore laboriosam expedita a magnam veritatis, ea quod repellendus corrupti maxime perspiciatis \
    quo incidunt, placeat adipisci minus. Facere doloremque hic in. Corporis optio maiores tempore aut molestias provident \
    voluptatum non, pariatur voluptatem eveniet dolore, et, blanditiis iure neque ducimus nam possimus minima magnam ipsum \
    exercitationem itaque cum. Voluptatem, iure fugiat sunt odio quidem quod iusto fugit natus dolor praesentium ea dolorum aut \
    corporis laboriosam ad quae sed blanditiis molestiae facere enim. Facere, porro assumenda perspiciatis maxime pariatur \
    molestias impedit? Non, consequuntur blanditiis saepe quisquam fugit maxime? Incidunt velit maiores dolore impedit ab totam \
    at perferendis, id, ad fugiat suscipit explicabo numquam atque animi natus doloremque repudiandae tenetur et repellat \
    voluptas. Quis tempora iure deleniti aliquid incidunt sed, quos nulla eum sequi ratione, nobis ducimus labore ut libero \
    dicta! Dolorem vero corporis illum officia et soluta rerum reiciendis optio explicabo obcaecati, nisi, cupiditate excepturi \
    perspiciatis deleniti quam doloribus eaque? Suscipit quos dolores iure debitis ullam, mollitia, esse veniam amet odio, harum \
    aliquam eveniet eligendi eaque maxime sapiente aut quasi. Natus quas quos dicta, dolorem nihil ex eveniet, odio laboriosam \
    repellendus neque rerum temporibus laudantium autem voluptatum maxime aspernatur sunt, itaque labore illo suscipit nam. \
    Accusantium explicabo odit, vel soluta dolore unde ipsa eius adipisci tempore iure dicta officia aspernatur ullam saepe \
    eligendi neque, minus maiores consequatur debitis, esse numquam est delectus necessitatibus! Magnam quasi tempora consectetur \
    suscipit voluptate ullam nulla quis ut facilis optio. Eos voluptates sit facere fuga maiores deleniti? Minus iusto ea \
    accusantium officiis error, sit quia impedit ratione asperiores soluta harum adipisci libero temporibus molestias consectetur \
    deserunt eos obcaecati nulla dignissimos, tempore excepturi? Eius totam, earum qui id culpa aperiam exercitationem laborum \
    quidem aspernatur facere quasi, dignissimos, nemo quibusdam? Dignissimos qui et ex exercitationem pariatur officiis laborum \
    ipsam cum natus dolorum nemo, doloremque porro consequatur rerum. Itaque officiis, labore ipsam facere repellendus praesentium \
    earum voluptate reprehenderit commodi numquam, recusandae perferendis quam accusamus quia magnam corrupti quae qui sit \
    dolores tempora! Dolore libero, exercitationem obcaecati rerum earum suscipit enim minus maiores debitis facere adipisci \
    temporibus tempore quod nesciunt? Molestias reiciendis quae commodi ut praesentium. Numquam nesciunt magni et vero quaerat \
    recusandae debitis blanditiis, incidunt obcaecati enim eaque laudantium perferendis delectus nobis itaque provident non \
    excepturi odio expedita quia corporis impedit. Quod velit amet vitae rerum maxime tenetur fugiat neque, sit ea."

class Tag:
    """HTML tag clisd.py object"""
    def __init__(self, name : str, *content, _class : str="", events=None, **attrs):
        self.name = name
        self.content = content

        self.events = events if events else []

        self.attrs = attrs
        if _class: self.attrs["class"] = _class

    def render(self, tag=None):
        """Renders tag to html"""
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
        """Renders component to html"""
        return super().render(tag=self._render())

class State:
    """Dynamic state for clisd.py components"""
    def __init__(self, component : Component, value : object, auto_render : bool=True):
        self.component = component
        self._value = value
        self.auto_render = auto_render

    def set(self, value : object):
        """Sets value for state and renders component, if auto_render"""
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


class Event:
    """Clisd.py event object"""
    def __init__(self, event : str, action : FunctionType = lambda e: None):
        self.event = event
        self.action = action

    def apply(self, target):
        """Apllies event on target"""
        target.addEventListener(self.event, pyodide.create_proxy(self.action))

# Shortcuts for tags
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

    if "render" in dir(dom):
        body = dom.render()
        document.body.innerHTML = ""
        document.body.appendChild(body)
    else:
        document.body.innerHTML = dom
    

    if not _style_elem:
        _style_elem = document.createElement("style")

    _style_elem.innerHTML = "\n".join(styles)
    styles[0:] = []

    document.head.appendChild(_style_elem)
    

def route(route : dict[str : FunctionType], filter : FunctionType=lambda x : x):
    """Routes links in clisd.py"""
    def route_link(e=None, page : str=None, _route : dict[str : FunctionType]=route):
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
            route_link(page="/".join(url_parts[1:] if url_parts[1:] else "/"), _route=lvl)
        else:
            render_page(filter(lvl()))

    window.addEventListener("hashchange", pyodide.create_proxy(route_link))
    route_link(None)