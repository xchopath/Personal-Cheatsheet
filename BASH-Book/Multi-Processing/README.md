# Sample Script for BASH Multi Processing

Just add background process operator (&) in some functions or commands for doing multi-process but it will be bloated.

For resource management, this script might help you:

```
#!/usr/bin/env bash

function anyfunc() {
  # put your activity here
  DELAY=`shuf -i 1-10 | head -1`
  sleep ${DELAY}s
  echo "PROCESS ${1} - delay ${DELAY}"
}

# this variable setted up to limit maximum simultaneous process
PROCMAX=5 

(
  for thing in {1..20}; do 
    ((PROCNUM=PROCNUM%PROCMAX)); ((PROCNUM++==0)) && wait
    anyfunc "${thing}" & 
  done
  wait
)
```
