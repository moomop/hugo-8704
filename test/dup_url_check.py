#! /usr/bin/env python3
import subprocess

fail_count = 0
pass_count = 0
for i in range(100):
    print(i)
    subprocess.run(['hugo'])
    p = subprocess.run(['grep', '-r', '/http', 'public/'] )
    if p.returncode == 1:
        pass_count += 1
    else:
        fail_count += 1

print('{} pass {} fail'.format(pass_count, fail_count))
