# natas25

I tried hard and long at the url to get to where the password was but no luck. I was able to get the traversal down but I could not get through the `natas_webpass` filter.

`....//....//....//....//....//etc/natas_webpass/natas26`

Getting to `natas_webpass` was obviously not the way to go. So I had to look somewhere else. Well, there was another file we could potentially exploit, and that's the file that the server is writing to when there's a traversal attempt. They're also using writing our `User-Agent` to the file which is something we can change.

It took me quite a bit of time to get this part down because I didn't know to use `global` on the variable but I eventually got it.

<details>
  <summary>Password</summary>
    oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T
</details>
