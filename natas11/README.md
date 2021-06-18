# natas11

I think I took the longest possible route on this one but it worked.

The `xor_encrypt` `$key` is `<censored>` in the source code, but you can still work out what it is if you know what you're looking for.

The starting data is: `$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");`
And what you're looking for is: `{"showpassword":"no","bgcolor":"#ffffff"}`

There's a cookie in the browser here with the name `data` whose value is the value of base64 encoded value of the xor'd json.

Warning: The value you get in the browser might be url escaped, ie: you'll see `%3D` at the end of it instead of the base64 padding character `=`.

So if we take the cookie's value, base64 decode it and xor it, we should get valid json. We should be able to reverse this method so that we can pass this json in and get a base64 value that will show us the password.

Hint: the key's value is 4 characters.

<details>
  <summary>Password</summary>
  EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3
</details>