# natas14

This one looks like some simple sql injection. We should be able to do a nested select state in the password field. But the more I look at it, the more I'm thinking that it might not be possible with the double quotes around the password variable.

Once I realized it wasn't possible, I tried thinking about other ways we could add to the query and then I ended up spending way too long because I thought the username was `natas14` instead of `natas15` even though I had the right thing...

Just think of how you could make one side of an if statement `true` if the other side is doomed to be `false`.

<details>
  <summary>Password Field</summary>
    " or username="natas15
</details>

<details>
  <summary>Password</summary>
    AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J
</details>
