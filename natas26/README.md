# natas26

PHP Object Injection? Answer a few days later: Yes.

This one was difficult for me. I wrote Logger off as some sort of red herring but I really, absolutely could not find a vulnerability anywhere else.

Then I learned about PHP Object Injection, and it blew my mind, but I still couldn't figure out how the hell I was meant to get around doing this so I didn't look at it for a few days. After a good 2 hour session it finally clicked with me what I could do here but it required playing around with PHP Object Injection to really understand what I could do.

For some reason I had it in my mind that the constructor would run when unserializing but that was completely false. Once I got around that and saw that I could use the `img/` path, it was pretty straightforward what I had to do.

I have to admit, this has been one of the most rewarding ones for me so far.

<details>
  <summary>Password</summary>
    55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ
</details>
