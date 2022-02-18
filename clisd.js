function loadFile(filePath) {
    let request = new Request(filePath);

   return fetch(request) 
   .then(resp => { 
        return resp.text()
    });
}

async function runPython(clisd, name) {
    let code = loadFile(name);
    code.then(
        function(val) {clisd.runPython(val)}
    );
}

async function init_clisd() {
    let pyodide = await loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.19.0/full/"
    });
    
    await runPython(pyodide, "https://cdn.jsdelivr.net/gh/farkon00/clisd.py/framework.py");

    return pyodide;
}