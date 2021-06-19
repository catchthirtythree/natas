# natas15

First, notice that the page will show you what query is being executed if you add `debug` to the GET request / query string. I'm thinking that might be key to figuring this one out since it doesn't look like there's any other place for the server to emit something to us.

I was wondering if I could take advantage of `echo` and run some `php` commands but I wasn't able to get anything going. Then I found a post on stackoverflow that mentinoed there that I might not be able to do any code injection with `php` but with echo there was a risk of XSS attacks.

So I tried to play with putting an `iframe` in the window and it worked, but it wasn't showing what I wanted it to show. I'm actually not sure if I'm able to make it show what I want to show because what it would be showing belongs to me and not the server.

It seemed like the echo wasn't the key to this challenge anymore and I went back to looking at the `mysql` query. I started looking up different types of `sql injection` and I eventually landed on `blind sql injection` and it reminded me of some HackTheBox videos I'd watched. I realized that since we're getting a message back from the server telling us whether the user exists or not, we could exploit that testing for the password and bruteforcing it.

Also, remember that LIKE is case INsensitive. I didn't know that the first time I ran my script.

<details>
  <summary>Password</summary>
    WaIHEacj63wnNIBROHeqi3p9t0m5nhmh
</details>
