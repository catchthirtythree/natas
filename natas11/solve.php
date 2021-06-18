<?php

function xor_encrypt($in) {
    $key = 'qw8J';
    $text = $in;
    $outText = '';

    for ($i=0; $i<strlen($text); $i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$data = array(
    "showpassword" => "yes",
    "bgcolor" => "#ffffff"
);

$json_data = json_encode($data);
$encrypted_data = xor_encrypt($json_data);
$based_data = base64_encode($encrypted_data);

print($based_data);
