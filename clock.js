// 時計のメインとなる関数
function clock()
{
    // 曜日を表す各文字列の配列
    var weeks = new Array("日","月","火","水","木","金","土");
    // 現在日時を表すインスタンスを取得
    var now = new Date();
    // 年
    var y = now.getFullYear();
    // 月 0~11で取得されるので実際の月は+1したものとなる
    var mo = now.getMonth() + 1;
    // 日
    var d = now.getDate();
    // 曜日 0~6で日曜始まりで取得されるのでweeks配列のインデックスとして指定する
    var w = weeks[now.getDay()];
    // 時
    var h = now.getHours();
    // 分
    var mi = now.getMinutes();
    // 秒
    var s = now.getSeconds();

    // 日付時刻文字列のなかで常に2ケタにしておきたい部分はここで処理
    if (mo < 10) mo = "0" + mo;
    if (d < 10) d = "0" + d;
    if (mi < 10) mi = "0" + mi;
    if (s < 10) s = "0" + s;

    //　HTML: <span id="clock_date">(ココの日付文字列を書き換え)</span>
    document.getElementById("clock_date").innerHTML =  y + "/" + mo + "/" + d + " (" + w + ")";
    //　HTML: <span id="clock_time">(ココの時刻文字列を書き換え)</span>
    document.getElementById("clock_time").innerHTML = h + ":" + mi;
    //　HTML: <div id="clock_frame"> の内部要素のフォントサイズをウインドウサイズの10分の1ピクセルに設定
    document.getElementById("clock_frame").style.fontSize =  window.innerWidth / 10 + "px";

    document.getElementById("clock_time2").innerHTML = mi;
    document.getElementById("clock_time1").innerHTML = h;
}

function wether()
{
  var http = require('http');
  var url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=130010';

http.get(url, function(res) {
    var body = '';
    res.setEncoding('utf8');
    res.on('data', function(data) {
        body += data;
    });
    res.on('end', function(data) {
        console.log(JSON.parse(body).forecasts[0].telop);
    })
});
}

function anime(){

    var timestamp1 = new Date().getTime();
    $('#animation').attr('src', 'brown.gif' + '?' + timestamp1);

}

// 上記のclock関数を1000ミリ秒ごと(毎秒)に実行する
setInterval(clock, 1000);
setInterval(anime, 2000);
setInterval("text1.style.opacity^=1",1000)
