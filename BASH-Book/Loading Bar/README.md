# BASH Loading Bar

### For Example

Create file `loadingbar.sh`

```
#!/usr/bin/env bash

function _loadingbar {
   let _progress=(${1}*100/${2}*100)/100
   let _done=(${_progress}*4)/10
   let _left=40-$_done
   _fill=$(printf "%${_done}s")
   _empty=$(printf "%${_left}s")
   printf "\r<${_fill// /\#}${_empty// /:}> ${_progress}%%"
}

last=10
for ((i=0;i<=$last;i++))
do
   _loadingbar "$i" "${last}"
   sleep 0.1
done
```

### GIF

![Loading Bar](https://github.com/xchopath/Personal-Cheatsheet/blob/master/BASH-Book/Loading%20Bar/loadingbar.gif)

Asciinema: <https://asciinema.org/a/1qD1KXjPOVIYtF2UexeCjUNN1?autoplay=1>
