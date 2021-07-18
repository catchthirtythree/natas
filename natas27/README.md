# natas27

There's not a whole lot in the source code that's all that weird. How `mysql_real_escape_string` is used seems pretty decent along with the uses of single quotes. The calls to `html_entities` seems pretty sketchy but not all that interesting. The `dumpData` function looks pretty juicy however. The only way this could be useful is if we could find a way to put multiple `natas28` users in the database. We can do this by exploiting the way the table is created, ie: `varchar(64)`. Pretty neat.

<details>
  <summary>Password</summary>
    JWwR438wkgTsNKBbcJoowyysdM82YjeF
</details>
