# BASH-Book & Cheat-sheet

----------

### Print Only Matched Text with Regex (grep)

Command:

```
grep -Po 'value="\K.*?(?=")'
```

Example:

```
bash:~$ curl -s "http://example.com/" | grep -Po 'href="\K.*?(?=")'
http://example.com/contact
http://example.com/about
```

----------

### Remove Newline Output (sed)

Command:

```
sed ':a;N;$!ba;s/\n/ /g'
```

Example:

```
bash:~$ cat somefile
one
two
three
four
bash:~$ cat somefile | sed ':a;N;$!ba;s/\n/ /g'
one two three four
```
