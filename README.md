# clisd.py
Clisd is UI framework with client side rendering and SPA for python. It uses WASM and [Pyodide framework](https://github.com/pyodide/pyodide) to run python code in clients browser.

In plans this framework will be able to compete with React, Vue.js, Angular etc.

Roadmap : 
* Develop good base for framework.
* Add abillity for server side rendering.
* Add more control of the page and interactive pages to framework.
* Add integration with Django for easy development for front and back end.
* Start development of new full-stack framework. Which will use this framework for front-end.
---
# Getting Started
1. Download template.html, template.js and framework.py(in future this will be on CDN).
2. Set up your local server(author uses Live Server for VS Code).
3. Create main.py or other .py file.
4. Run runPython function as showed in template.js.
5. Write code in your file.

Done!

## Example
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
        , _class="container flex nav", id="nav"
    )

def about_page():
    return div(
        a("Main", href="#"),
        p("We don`t know who we are")
    )

def main():
    route({
        "about" : about_page,
        "" : main_page
    })

main()
```
