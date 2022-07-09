# clisd.py
Clisd is UI framework with client side rendering and SPA for python. It uses WASM and [Pyodide framework](https://github.com/pyodide/pyodide) to run python code in clients browser.

**This project isnt developed currently.**
<!--In plans this framework will be able to compete with React, Vue.js, Angular etc.-->

Roadmap : 
* [x] Develop good base for framework.
* [x] Add more control of the page and interactive pages to framework.

May be :
* [ ] Integration with Django for easy development for front and back end.
* [ ] Development of new full-stack framework. Which will use this framework as front-end part.
---
# Getting Started
1. Create html file and load script from CDN https://cdn.jsdelivr.net/gh/farkon00/clisd.py/clisd.js
2. Set up your local server(author uses [Live Server for VS Code](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer)).
3. Create main.py or other .py file.
4. Create code as showed in template.js.
5. Write code in your .py file.

Done!


# Documentation

# Table of content
  * [Python](#python)
    * [Components](#components)
      * [Functional components](#functional-components)
      * [Class components](#class-components)
    * [Variables and costants](#variables-and-costants)
      * [LOREM](#lorem)
      * [styles](#styles)
      * [_style_elem](#_style_elem)
    * [Types](#types)
      * [Tag](#tag)
        * [Tag.render](#tagrender)
      * [Component](#component) 
        * [Component.render](#componentrender)
      * [State](#state)
        * [State.set](#stateset)
      * [Event](#event)
        * [Event.apply](#eventaplly)
    * [Functions](#functions)
      * [Tag fucntions](#tag-fucntions)
      * [relative](#relative)
      * [anchor](#anchor)
      * [render_page](#render_page)
      * [route](#route)
    
  * [JS](#js)
    * [init_clisd](#init_clisd)
    * [runPython](#runpython)
 
# Python 
# Components
In clisd.py pages splited into components, and pages are component also. There is 2 types of components: fucntions and classes.

## Functional components
  Functional components are functions that return string of html code or Tag object. Compoentns can accept arguments or make requests to back-end themselves. Also functional components can`t use states, only way for using states is making functional components included in class component, so they will be rerendered every time state changes.

  Simple example of components :
  ```
  def nav_link(name, link):
    return li(a(name, href=link))

  def nav():
    styles.append(nav_styles) # Styles are big, so they are not included.

    return div(
      ul(
        li(h1(a("Example page", href="#"), _class="logo")),
        nav_link("About", "#about"),
        nav_link("Test", "#about/test"),
        _class="nav-list"
      ),
          _class="nav"
      )
  ```

## Class components
  Class components are classes, which are inherieted from [Component](#component) class and have _render private method. Main difference between fucntional and class components is states.

  States created by using [State](#state) class. Example of state : `self.state = State(self, 0)`, so first argument is component itself and second is initial value. State value can be anything.

  When state changes component automatically rerenderes itself. But if you don`t want that add auto_render argument to initialization of state.

  Example of class component : 
  ```
  class ClassComp(Component):
    def __init__(self):
      self.state = State(self, 0)
    
    def _render(self):
      return div(
        Tag("button", "CLICK", events=(Event("click", lambda x : self.state.set(self.state.value + 1)),)),
        p(self.state.value)
      )
  ```

# Variables and costants
  ## LOREM
  Type : str

  Constant of old text lorem ipsum. Used by web developers as placeholder.

  ## styles
  Type : list\[str\]

  Array of styles from components. Clears every time when page rendered.

  ## _style_elem
  Type : JS HTMLElement(None before first render)

  JS object for style element, that was added from [styles](#styles) list.


# Types
  ## Tag
  HTML tag type. 
  
  Constructor args :
  ---
  * name : str - name of html tag
  * *content - tags or text inside of tag
  * envents : tuple[Event] - events for this tag
  * \_class : str - classes of tag
  * \*\*atrs - attributes of tag
  
  Methods :
  ---
  ### Tag.render
  `def render (tag=None)`
  
  Renders [Tag](#tag) obejct to JS HTMLElement.
  
  Argument tag created for DRY and inheritance.
  
  
  ## Component
  Component type. Used for inheritance for custom class components. Inherited from [Tag](#tag).

  Details :
  ---
  
  Components must have private method \_render, which returns string or [Tag](#tag).
  
  Methods :
  ---
  ### Component.render
  `def render ()`
  
  Renders component to screen.
  
  ## State
  Dynamic state for class components type.
  
  Constructor arguments :
  ---
  * component : [Component](#component) - component to which this state belongs
  * value : object - initial value of state
  * auto_render=True - bool coresponding to auto rerendering component after state value changing

  Properties :
  ---
  value : object - value of state, on change calls [set](#stateset)
  
  Methods :
  ---
  ### State.set
  `def set (self, value : object)`
  
  Sets value of state to `value`. Also can be used by setting State.value manually(`self.my_state.value = 1`).
  
  ## Event
  Data class, which stores all data about event.
  
  Constructor arguments :
  ---
  * event : str - name of event. [More about events](https://developer.mozilla.org/en-US/docs/Web/Events)
  * action : function = lambda e: None - function that will be called on event

  Methods :
  ---
  ### Event.aplly
  `def apply (target)`
  
  Applies an event for `target`.
  
  Arguments :
  ---
  * target : JS EventTarget - target, which will be used for addEventListener
  
# Functions
  ## Tag fucntions
  `def <tag>(*args, **kwargs)`

  For easier and more beatiful code there are shortcut functions for the most used tags. This functions returns [Tag](#tag) obejct. For first argument goes tag name and then unpacked args and kwargs.

  Tags that have shortcuts : div, p, pre, span, img, input, button, textarea, table, tbody, th, tr, td, a, h1, h2, h3, h4, h5, h6, strong, em, i, br, ul, ol, li

  Example : `a("About", href="#about")`

  ## relative
  `def relative (link : str)`
  
  Converts relative link `link` to absolute link.
  
  Arguments :
  ---
  * link : str - relative link to be converted

  ## anchor
  `def anchor (id : str)`
  
  Converts id name to anchor link.
  
  Arguments :
  ---
  * id : str - id of element to which link will point

  ## render_page
  `def render_page(dom : Tag)`
  
  Renders `dom` to screen, displays CSS.
  
  Arguments :
  ---
  * dom : Tag - tag that will be displayed to screen

  ## route
  `def route (route : dict[str : FunctionType], filter : FunctionType=lambda x : x)`
  
  Routes link in `route` dictionary. Automatically calls [render_page](#render_page), when link changes. 
  
  Route looks that way :
  ```
  {
    '' : main,
    'test' : {
      '' : test,
      'about' : about
    }
  }
  ```
  Where main, test and about is function components, that return Tag object. 
  
  Links will look like that :
  ```
  website.com : main,
  website.com#/test : test,
  website.com#/test/about : about
  ```

  Filter fucntion example :
  ```
  def filter_(code):
    return div(
        nav(),
        code
    )
  ```
  
  Details :
  ---
  Clisd.py uses hashes for routing. This is needed for creation of SPA. So in html anchor links must be used to work.
  
  Arguments :
  ---
  * route : dict - dictionary of links and function components for that. **Carefully read description of function for structure of dictionary**
  * filter : function - function, that adds template code to page, like navigation or footer.
  
  
# JS
# Functions
 ## init_clisd
 `async function init_clisd ()`
 
 Initialize clisd framework and pyodide. Returns pyodide module. Check [pyodide docs](https://pyodide.org/en/stable/usage/api/js-api.html#js-api-pyodide) for more details.
 
 ## runPython
 `async function runPython (clisd, name)`
 
 Runs python file via pyodide framework.
 
 Arguments :
 ---
 * clisd : pyodide module - pyodide module returned by init_clisd
 * name : String - link to .py file
