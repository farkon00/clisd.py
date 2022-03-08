
function loadFile(filePath) {
    let request = new Request(filePath);

   return fetch(request) 
   .then(resp => { 
        return resp.text()
    });
}

async function runPython(clisd, name) {
    let code = await loadFile(name);
    await clisd.runPython(code);
}

async function init_clisd() {
    let pyodide = await loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.19.0/full/"
    });

    await runPython(pyodide, "/framework.py");

    return pyodide;
}