# natas13

This challenge is similar to the last except now we have to trick the server into thinking that our payload is an image.

I picked PNG because it seemed to be the easiest the spoof but you could pick any from the list in the documentation for `exif_imagetype` found here: https://www.php.net/manual/en/function.exif-imagetype.php

According to the documentation for that function, the function only checks the first few bytes of a file to make sure that it is indeed that file and returns the type of file. If you read the PNG specifications, they give you the first 8 bytes of a PNG file here: http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature

Now that you know the starting bytes and you have the payload already since it's the same as before, you just need to create a file with the starting bytes and the payload and do the same steps as last challenge by changing the `filename` and sending the payload and clicking the link. You should see the PNG bytes before the password when you access the file.

<details>
  <summary>Password</summary>
  Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1
</details>
