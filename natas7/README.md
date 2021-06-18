# natas7

Notice that whenever the query string `page` changes, you will change page. If you attempt to change that string to anything, you will get a php error saying that the file does not exist in the current directory and it will display the directory.

If you inspect the page, you will also notice this comment:

```html
<!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
```

You can do directory traversal here and read the webpass file by entering `../../../../etc/natas_webpass/natas8` as the `page` query string.

<details>
  <summary>Password</summary>
  ```
  DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
  ```
</details>