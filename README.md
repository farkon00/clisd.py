# clisd.py
Clisd is UI framework with client side rendering for python. It uses WASM and [Pyodide framework](https://github.com/pyodide/pyodide) to run python code in clients browser.

In plans this framework will be able to compete with React, Vue.js, Angular etc.

Roadmap : 
* Develop good base for framework.
* Add abillity for server side rendering.
* Add more control of the page and interactive pages to framework.
* Add integration with Django for easy development for front and back end.
* Start development of new full-stack framework. Which will use this framework for front-end.
---
# Getting Started
1. Download template.html and framework.py(in future this will be on CDN).
2. Set up your local server(author uses Live Server for VS Code).
3. Create main.py or other .py file.
4. Put your file name into 31 line of template.
5. Write code in your file.

Done!

## Example
```
style = [] # Style is used to add css from components

def cute_component(): # Component 
    style.append(
    """
    #react_p {
        font-size : 60px;
    }
    """
    )

    return div(
        p("Component example : ", id="react_p"),
        img(width="20%", height="20%", src="https://bit.ly/3gXBe1f") # Image of cat
    )

def main():
    tag = div(
            p("Nice start for the framework!", _class="content"),
            cute_component()
        , _class="container flex nav", id="nav"
    )

    render_body(tag, styles=style) # Renders Tag objects as html

main()
```
