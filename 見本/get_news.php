<?php

$base_url = "http://rss2json.com/api.json?rss_url=http%3A%2F%2Fnews.google.com%2Fnews%3Fhl%3Dja%26ned%3Dus%26ie%3DUTF-8%26oe%3DUTF-8%26output%3Drss";
$json = file_get_contents($base_url);
$json = mb_convert_encoding($json, 'UTF-8');
print $json;
