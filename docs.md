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
        * [Event.apply](#eventaplly)
    * [Functions](#functions)
      * [relative](#relative)
      * [anchor](#anchor)
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

  Methods :
  ---
  ### Event.aplly
  `def apply (target)`
  
  Applies an event for `target`.
  
  Arguments :
  ---
  * target : JS EventTarget - target, which will be used for addEventListener
  
# Functions
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
  `def route (route : dict, filter=lambda x : x)`
  
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
 * clisd : pyodide module - pyodide module returned bi init_clisd
 * name : String - link to .py file