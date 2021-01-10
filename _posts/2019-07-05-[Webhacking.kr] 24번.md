---
layout: post
title: '[Webhacking.kr] 24번'
author: MilkClouds
comments: true
date: 2019-07-05 00:06
tags: [problem-solving]

---

## 문제
[http://webhacking.kr/challenge/bonus/bonus-4/](http://webhacking.kr/challenge/bonus/bonus-4/)  


## 설명  
**문제를 아직 풀지 않았다면 읽지 말자.**  
기본형의 strreplace를 한 번만 사용해서 제대로 된 필터링을 할 수 없음을 보여주는 문제다. 백준에서 문자열 폭발.. 이었나? 같은 문제들도 문자열 대체가 있는데 단순하게 함수 한번 써서는 해결이 안되는 문제가 많던걸로 기억한다.  

`index.phps` 들어가보면 어떤 구조로 작동하는지 알 수 있고, 세 번의 문자열 대체를 거치고도 127.0.0.1이 남아있도록 만들면 된다.  

```php
<?

extract($_SERVER);
extract($_COOKIE);

if(!$REMOTE_ADDR) $REMOTE_ADDR=$_SERVER[REMOTE_ADDR];

$ip=$REMOTE_ADDR;
$agent=$HTTP_USER_AGENT;


if($_COOKIE[REMOTE_ADDR])
{
$ip=str_replace("12","",$ip);
$ip=str_replace("7.","",$ip);
$ip=str_replace("0.","",$ip);
}

echo("<table border=1><tr><td>client ip</td><td>$ip</td></tr><tr><td>agent</td><td>$agent</td></tr></table>");

if($ip=="127.0.0.1")
{
@solve();
}

else
{
echo("<p><hr><center>Wrong IP!</center><hr>");
}
?>
```


쿠키에 `REMOTE_ADDR=17.277..00..00..1` 넣어서 보내주면 풀린다.  