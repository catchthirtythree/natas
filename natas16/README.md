# natas16

Because we're between quotes, I know we can do some funky stuff with $() but I'm not exactly sure what. One thing that came to mind was to do something like this:

`$(cat /etc/natas_webpass/natas17 >> ./dictionary.txt)`

It bypasses the regex check but it should append the password file to `dictionary.txt` before displaying the whole thing because we leave the string empty but it doesn't seem to work. I feel like I'm on the right track, or at least better than when I first looked at this and had no idea what to do.

I thought about trying to bruteforce with a boolean check like the last challenge but I was having a hard time coming up with a way to do it because I've not touched bash in a while. I ended up with a crazy idea where I would `cat` the password file into a variable, and then `grep` specified indices of that file and if I got something, it meant that I found a letter. Something like this:

`aprils$(a=$(cat /etc/natas_webpass/natas17))$(grep <letter> <<< ${a:<index>:1})`

but it would not work at all when I put it into practice. It seemed to work in my terminal with some test files though.

I'll admit that I ended up having enough of this one and looked it up and damn was I decently close (at least with the grep part...). I think I need to take a step back at some point or take a break because I could have had it but I got a little too impatient.

<details>
  <summary>Password</summary>
    8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
</details>
