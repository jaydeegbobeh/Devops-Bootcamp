## Linux commands

- Who am I `uname` or `uname -a`
- Where am I `pwd` 
- List files (inc hidden files) `ls -a`
- Delete file `rm filename` or `rm -rf filename` forces deletion
- Create a file `touch filename` or `nano filename` `vi filename`
- Edit text - `vi filename` or `nano filename`
- Create a dir `mkdir dir_name`
- Navigate inside dir `cd dir_name`
- List all processes running `ps aux` or `top`
- Kill a process `kill process_id`
- Wildcard matches any characters `*` e.g `ls *.py` will list all the files with .py extension
- File permissions `+x ececutanle`
- `read (r) write (w)`
- `ll` checks all permissions
- change permissions
    - `chomd 700` allows r,w,e
    - `chomd 600` read and write access
    - `chmod 400` read permission only
- Read last 2 lines of a file `tail -2 file name`
- Copy file/ folder `cp filename destination`
- Move a file (cut/paste) `mv filename ./location`
- You can also use mv to rename a file `mv filename new_filename`
- How to use piping | `ls | head -2`

** Variable and Environment Variable**
- How to check env var? `env`
- Print particular env `printenv name`
- Creating env var `export key=value` `export name=Jaydee`, `printenv name` will return 'Jaydee'
- Environment variables are stored in current session unless they are persistent
- **Persistent env**
1. sudo nano ~/.bashrc
2. Write a line for each variable you wish to add:
    - export DB_HOST = localhost
3. source ~/.bashrc : applies changes during current session

