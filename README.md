# clisd.py
Clisd is UI framework with client side rendering and SPA for python. It uses WASM and [Pyodide framework](https://github.com/pyodide/pyodide) to run python code in clients browser.

In plans this framework will be able to compete with React, Vue.js, Angular etc.

Roadmap : 
* [x] Develop good base for framework.
* [ ] Add more control of the page and interactive pages to framework.(WIP)
* [ ] integration with Django for easy development for front and back end.
* [ ] development of new full-stack framework. Which will use this framework for front-end.
---
# Getting Started
1. Create html file and load script from CDN https://cdn.jsdelivr.net/gh/farkon00/clisd.py/clisd.js
2. Set up your local server(author uses Live Server for VS Code).
3. Create main.py or other .py file.
4. Create code as showed in template.js.
5. Write code in your .py file.

Done!


# Documentation

# Table of content
  * [Python](#python)
    * [Types](#types)
      * [Tag](#tag)
        * [Tag.render](#tagrender)
      * [Component](#component) 
        * [Component.render](#componentrender)
      * [State](#state)
        * [State.set](#stateset)
      * [Event](#event)
    * [Functions](#functions)
      * [render_page](#render_page)
      * [route](#route)
    
  * [JS](#js)
    * [init_clisd](#init_clisd)
    * [runPython](#runpython)
 
# Python 
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
  `def set (value)`
  
  Sets value of state to `value`. Also can be used by setting State.value manually(`self.my_state.value = 1`).
  
  ## Event
  Data class, which stores all data about event.
  
  Constructor arguments :
  ---
  * event : str - name of event. [More about events](https://developer.mozilla.org/en-US/docs/Web/Events)
  * action : function = lambda e: None - function that will be called on event
  
# Functions
  ## render_page
  `def render_page(dom : Tag)`
  
  Renders `dom` to screen, displays CSS.
  
  Arguments :
  ---
  * dom : Tag - tag that will be displayed to screen

  ## route
  `def route(route : dict)`
  
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
  
  Details :
  ---
  Clisd.py uses hashes for routing. This is needed for creation of SPA. So in html anchor links must be used to work.
  
  Arguments :
  ---
  * route : dict - dictionary of links and function components for that. **Carefully read description of function for structure of dictionary**
  
  
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
 * clisd : pyodide module - pyodide module returned bi init_clisd
 * name : Strign - link to .py file

# Example
```
def cute_component():
    styles.append(
    """
    #comp_p {
        font-size : 60px;
    }
    """
    )

    return div(
        p("Component example : ", id="comp_p"),
        img(width="20%", height="20%", src="https://bit.ly/3gXBe1f") # Image of cat
    )

def main_page():
    return div(
            p("Nice start for the framework!", _class="content"),
            cute_component(),
            a("About", href="#about")
    )

class ClassComp(Component):
    def __init__(self):
        self.state = State(self, 0)
    
    def _render(self):
        return div(
            Tag("button", "CLICK", events=(Event("click", lambda x : self.state.set(self.state.value + 1)),)),
            p(self.state.value)
        )

def about_page():
    return div(
        a("Main", href="#"),
        p("We don`t know who we are"),
        ClassComp()
    )

def main():
    route({
        "about" : about_page,
        "" : main_page
    })

main()
```
