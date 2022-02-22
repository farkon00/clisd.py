async function main(){
    let clisd = await init_clisd();
    await runPython(clisd, "/main.py")
}

main();