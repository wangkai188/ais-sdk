<?php
/**
 * 文本检测服务的aksk请求方式的示例
 */
require "./ais_sdk/moderation_text.php";
require "./ais_sdk/utils.php";

$app_key = "*************";
$app_secret = "*************";

$categories = array(
    array(
        "text" => "666666luo聊请+110亚砷酸钾六位qq，fuck666666666666666",
        "type" => "content"
    )
);

$items = array("ad", "politics", "politics", "politics", "contraband", "contraband");

$result = moderation_text_aksk($app_key, $app_secret, $categories, $items);
echo $result;
