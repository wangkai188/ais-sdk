/**
 * 图像内容批量检测服务ak,sk请求方式的使用示例
 */
var content = require("./ais_sdk/image_content_batch");
var utils = require("./ais_sdk/utils");

var app_key = "*************";
var app_secret = "*************";

var filepath = "./data/moderation-terrorism.jpg";
var data = utils.changeFileToBase64(filepath);

url1 = "https://ais-sample-data.obs.cn-north-1.myhwclouds.com/terrorism.jpg";
url2 = "https://ais-sample-data.obs.cn-north-1.myhwclouds.com/antiporn.jpg";

content.image_content_batch_aksk(app_key, app_secret, [url1, url2], ["politics", "terrorism", "porn"], 0, function (result) {
    console.log(result);
});