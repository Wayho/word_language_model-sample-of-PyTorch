var $p = require('procstreams');

function shell_ls() {
	$p('ls').out();
}

function shell_ls_l() {
	$p('ls -l').out();
}

function shell_pipe_ls_l() {
	$p('ls -l').pipe(process.stdout)       //相比.out()，不会终止!!!
}

function shell_test() {
    //多命令示例
	$p('ls')
        .out()
        .and('ls -l')
        .out()
        .and('cat app.js')
        .out()
        .on('exit', function() {
            console.log('done');
        });
}

shell_pipe_ls_l()

//$p('ls').out();

//$p('ls').then($p('ls -l'));


/*
$p('ls')
    .out()
    .and('ls -l')
    .out()
    .and('cat app.js')
    .out()
    .on('exit', function() {
      console.log('done');
    });

    /*
    $p('ls').data(function(err, stdout, stderr) {
        // handle error
        console.log(stdout); // prints stdout
    });
    */


