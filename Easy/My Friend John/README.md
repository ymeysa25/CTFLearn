# My Friend John

**Category:** miscellaneous

## Problem

Have you met my friend John?

He's not so scary, even though they call him "The Ripper".

[MyFriendJohn.zip](https://ctflearn.com/challenge/download/1135)


## Hints
Use cracking tools such as fcrackzip or jtr "Jack The Ripper"

### fcrackzip Solution
- unzip MyFriendJohn.zip
- We want to unzip use-rockyou.zip but zip file is protected by password, so we will crack it, first download [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
)
- (Optional) U can download it using
  ```
  curl -L -o rockyou.txt https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt
  ```

- ```fcrackzip -v -u -D -p rockyou.txt use-rockyou.zip``` after we got the pass, we can use ```unzip use-rockyou.zip```
- inside use-rockyou.zip we have protected zip custom-list.zip, we will use custom-list.txt as dictionary pass to crack it ```fcrackzip -v -u -D -p custom-list.txt custom-list.zip```
- the last zip we want to crack is brute-force-pin.zip, A pin is usually between 4 and 6 numeric digits. ```fcrackzip -b -c "1" -l 4-6 -v -u brute-force-pin.zip```. The -c "1" means only use numeric digits when bruteforcing.
- Finally we get a flag.txt, and use ```cat flag.txt``` to see the flag.



