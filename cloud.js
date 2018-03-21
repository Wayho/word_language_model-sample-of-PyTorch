var AV = require('leanengine');
var $PSshell = require('procstreams');

AV.Cloud.define('ls', function(request) {
    cmd = 'ls -l'
    console.log('$'+cmd);
    $PSshell(cmd).out();
    return cmd;
});

//call api in this page:
//https://leancloud.cn/dashboard/apionline/index.html
//{'cmd':'uname -a'}
AV.Cloud.define('shell', function(request) {
    console.log('$'+request.params.cmd);
    $PSshell(request.params.cmd).out();
    return request.params.cmd;
});

//call api in this page:
//https://leancloud.cn/dashboard/apionline/index.html
//{'cmd':'uname -a'}
AV.Cloud.define('shellpipe', function(request) {
    console.log('$'+request.params.cmd);
    $PSshell(request.params.cmd).pipe(process.stdout)
    .data(function(err, stdout, stderr) {
        // handle error
        console.log(stdout); // prints
    });
    return request.params.cmd;
});
