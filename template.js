async function main(){
    let clisd = await init_clisd();
    runPython(clisd, "/main.py")
}

main();