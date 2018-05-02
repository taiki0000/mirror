<?php

$cityCode = '#INPUT_YOUR_CITY_CODE';
$apiKey = '#INPUT_YOUR_API_KEY';
$base_url = "http://api.openweathermap.org/data/2.5/weather?id=$cityCode&appid=$apiKey&units=metric";
$json = file_get_contents($base_url);
$json = mb_convert_encoding($json, 'UTF-8');
print $json;
