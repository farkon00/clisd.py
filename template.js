async function main(){
    let clisd = init_clisd();
    clisd.then(function(val) {runPython(val, "/main.py")});
}

main();