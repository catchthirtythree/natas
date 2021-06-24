# natas20

This took way longer than I wanted it to. I looked through the code, pointed out some potential vulnerabilities and then saw the line `$_SESSION["name"] = $_REQUEST["name"];` and knew it had something to do with it but I couldn't figure out what. I started to pick apart how saving and loading happened when I noticed the `explode("\n", $data)` as well as the `$data .= "$key $value\n";`. The hardest part was figuring out how to pass that new line to the server...

<details>
  <summary>Password</summary>
    IFekPyrQXftziDEsUr3x21sYuahypdgJ
</details>
