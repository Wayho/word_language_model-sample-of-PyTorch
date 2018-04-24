# coding: utf-8
from leancloud import Engine
from leancloud import LeanEngineError

import subprocess
import select
import requests
import time
import random
import os
import codecs
import psutil

engine = Engine()

ENGNIE_RESTARTED = True
APP_ROOT = os.environ.get('LEANCLOUD_APP_REPO_PATH')
APP_DOMAIN = os.environ.get('LEANCLOUD_APP_DOMAIN') 

print 'APP_ROOT:',APP_ROOT
print 'APP_DOMAIN:',APP_DOMAIN

########## Base Functions ##################
def Save_To_File(filename,text):
	ffile = codecs.open( filename, 'w', 'utf-8')
	ffile.write(text)
	ffile.close()

def Load_From_File(filename):
	ffile = codecs.open( filename, 'r', 'utf-8')
	text = ffile.read()
	ffile.close()
	return text

###############################################
@engine.define( 'ls' )
def cmd_ls():
	OutputShell('ls -l')
	return True

@engine.define( 'top' )
def cmd_top():
	OutputShell('top -b -n 1 -H')
	return True

@engine.define( 'ps' )
def cmd_ps():
	OutputShell('ps -eLf')
	return True

@engine.define( 'cpuinfo' )
def cmd_cpuinfo():
	OutputShell('cat /etc/issue && cat /proc/cpuinfo')
	return True

@engine.define( 'shell' )
# 调试 {'cmd':'ls -l' }
def OutputShell( cmd, **params ):
	print 'shell:',cmd
	result = subprocess.Popen(
		#[ "ping 127.0.0.1" ],
		#[ "find /usr" ],
		[ cmd ],
		shell=True,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE
	)
	# read date from pipe
	select_rfds = [ result.stdout, result.stderr ]
	while len( select_rfds ) > 0:
		(rfds, wfds, efds) = select.select( select_rfds, [ ], [ ] ) #select函数阻塞进程，直到select_rfds中的套接字被触发
		if result.stdout in rfds:
			readbuf_msg = result.stdout.readline()      #行缓冲
			if len( readbuf_msg ) == 0:
				select_rfds.remove( result.stdout )     #result.stdout需要remove，否则进程不会结束
			else:
				print readbuf_msg,

		if result.stderr in rfds:
			readbuf_errmsg = result.stderr.readline()
			if len( readbuf_errmsg ) == 0:
				select_rfds.remove( result.stderr )     #result.stderr，否则进程不会结束
			else:
				print readbuf_errmsg,
	result.wait() # 等待字进程结束( 等待shell命令结束 )
	#print result.returncode
	##(stdoutMsg,stderrMsg) = result .communicate()#非阻塞时读法.
	return result.returncode


################################################

################################################
#{'cmd':'top -b -n 1'}
#  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND


#{'cmd':'top -b -n 1 -H -i'}


#{'cmd':' cat /proc/version '}
#Linux version 3.13.0-123-generic (buildd@lcy01-10) (gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.3) ) #172-Ubuntu SMP Mon Jun 26 18:04:35 UTC 2017

#{'cmd':'grep "model name" /proc/cpuinfo'}
#model name : Common KVM CPU            #共7行
#model name	: Intel(R) Core(TM) i5 CPU         650  @ 3.20GHz

#{'cmd':'uname -a'}
#Linux 0ee7d925a033 3.13.0-123-generic #172-Ubuntu SMP Mon Jun 26 18:04:35 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
#Linux xxx 4.13.0-36-generic #40~16.04.1-Ubuntu SMP Fri Feb 16 23:25:58 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

#{'cmd':'cat /proc/meminfo |grep -i hugepages'}
#AnonHugePages:    192512 kB
#HugePages_Total:       0
#HugePages_Free:        0
#HugePages_Rsvd:        0
#HugePages_Surp:        0
#Hugepagesize:       2048 kB

#{'cmd':' cat /proc/cpuinfo '}
#cpu MHz : 2593.748
#flags : fpu de pse tsc msr pae mce cx8 apic mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx lm constant_tsc nopl pni cx16 sse4_1 sse4_2 x2apic popcnt aes avx hypervisor lahf_lm

#{'cmd':'cat /proc/cgroups'}
#subsys_name	hierarchy	num_cgroups	enabled
#cpuset	5	195	1
#cpu	12	722	1
#cpuacct	12	722	1
#memory	10	1968	1
#devices	2	721	1
#freezer	3	195	1
#net_cls	7	195	1
#perf_event	4	195	1
#net_prio	7	195	1
#hugetlb	11	195	1
#pids	6	722	1
#rdma	9	1	1

#{'cmd':'cat /proc/interrupts'}

#{'cmd':'cat /proc/softirqs'}
#{'cmd':'cat /proc/stat'}

#{'cmd':' cat /proc/cmdline '}
#BOOT_IMAGE=/boot/vmlinuz-4.4.0-72-generic root=/dev/vda1 ro video=800x600 cgroup_enable=memory swapaccount=1 console=ttyS0,115200n8
#BOOT_IMAGE=/boot/vmlinuz-4.13.0-36-generic root=UUID=a60681aa-fed1-496a-a211-fc83a4ce3fe0 ro quiet splash vt.handoff=7

#{'cmd':'cat /proc/interrupts'}

#{'cmd':'cat /proc/modules'}

#{'cmd':'cat /proc/thread-self/limits'}

#{'cmd':'ls /proc/23477/cwd'}

#{'cmd':'ps -eLf'}
#include thread
#UID        PID  PPID   LWP  C NLWP STIME TTY          TIME CMD


#{'cmd':'ps -eLf | grep cpum'}
