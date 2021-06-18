# natas4

The page states that authorized users must come from `http://natas5.natas.labs.overthewire.org/`. You can do this by sending a GET request to `http://natas4.natas.labs.overthewire.org/` and setting the `Referer` to `http://natas5.natas.labs.overthewire.org/`. Note that you will have to set `Authorization` as well in which if you inspect a GET request to the initial page in the browser will look something like this: `Basic <token>`.

Run the `solve.py` script and read the contents for the password.

<details>
  <summary>Password</summary>
  ```
  iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
  ```
</details>