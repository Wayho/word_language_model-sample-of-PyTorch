# Description

This is a Shell for LeanCloud, by Python(master branch) and Nodejs(NodeJS branch).

# How it work

It provide some API, in API, it use <procstreams> library to shell the command, and print output of shell command in console.

# API

* ls:   A test API, shell command such as "ls -l".
* top:  top -b -n 1 -H
* ps:   ps -eLf
* cpuinfo:  cat /etc/issue && cat /proc/cpuinfo
* shell:    shell command use procstreams.out() method.
* shellpipe:    shell command use procstreams.pipe() method.

# Features


# Requirements

* psutil>=5.4.3(Python)

* procstreams >= 0.3.0(Nodejs)


# Installation

* just deploy and open https://leancloud.cn/dashboard/apionline/index.html


# Credits



# License



