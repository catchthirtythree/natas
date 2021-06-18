# natas12

I was searching for vulnerabilities with `$_POST[file][tmp_name]` specifically and fell on a stackoverflow post where someone asked if their code was vulnerable and someone mentioned that they would be vulnerable to invalid file upload attacks. I felt like I spoiled myself on this challenge a bit.

I spent a bunch of time with the `filename` that wouldn't have gotten me anywhere anyway but I was certain that I could use `move_uploaded_file` to move a webpass file to a target based on the `filename` except `phpinfo($filename, PHPINFO_EXTENSION)` is very strict about what you give it and it seems like attempting a directory traversal is impossible here.

I could be wrong here but my line of thinking is that ince the the server is a php enabled Apache server (you can see in the Response Headers => Server: Apache/2.4.10 (Debian)) and the server is storing the file you uploaded for you and letting you access it, you can upload a "malicious" `.php` file and have the server host it to you in the `upload` folder. You could make this `.php` file run all sorts of stuff, like echoing the password to the challenge. Before uploading, you would change the `filename` from `<randomstring>.jpg` to `<randomstring>.php` so it gets rendered appropriately.

This will get you your password.

<details>
  <summary>Password</summary>
  jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY
</details>
