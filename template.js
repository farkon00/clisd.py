async function main(){
    let clisd = await init_clisd();
    clisd.then(async function() {
        await runPython(clisd, "/main.py");
    });
}

main();