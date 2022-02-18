function loadFile(filePath) {
    let request = new Request(filePath);

   return fetch(request) 
   .then(resp => { 
        return resp.text()
    });
}

async function runPython(pyodide, name) {
    let code = loadFile(name)
    code.then(
        function(val) {pyodide.runPython(val)}
    )
}

async function main(){
    let pyodide = await loadPyodide({
        indexURL : "https://cdn.jsdelivr.net/pyodide/v0.19.0/full/"
    });
    
    await runPython(pyodide, "/framework.py");
    await runPython(pyodide, "/main.py");
}

main();