import subprocess

cmd = "ifconfig | grep en0"

p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
    print (str(line))
retval = p.wait()