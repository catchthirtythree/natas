# natas18

I'm having trouble with this one. It seems like there's no way to get into the `print_credentials()` with the right flags off the bat. There are two things that I've noticed that I'm starting to think might be part of the solution though:

* I notice that there are some areas where failed sessions are handled.
* I also noticed the usage of `&&` and `and` in a few `if` statements.

But these still don't seem exploitable really. I think the first one is just some regular error handling and the second one is something that can only be exploited situationally. I will say that I looked into ways to exploit sessions and to make sessions fail and it sort of sent me on the right track.

I thought that maybe if I tried to send a lot of requests at the same time, I could make the `session_start()` fail. So I started trying to hammer the server with 20-60 requests but nothing seemed to work very well. I had made the mistake of a using a single session id so I switched to randomizing them, but I still wasn't getting much out of it.

I'm sure I found the password at this point somewhere accidentally but didn't realize because I was printing the whole page and expecting to see something big happen. I started filtering for certain terms in the content and printing out smaller versions until I eventually tried 700 requests and got it. Only then did I realize that I was looking for the admin's session id.

Oh well. ¯\_(ツ)_/¯

<details>
  <summary>Password</summary>
    4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs
</details>
