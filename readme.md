# 기능
음원 스트리밍 사이트 [멜론][melon_index]의 [TOP100][top100] / [최신음악][newsong] / [장르음악][genre] 곡 정보를 크롤링하여 CSV 파일로 저장하는 프로그램입니다.

[melon_index]: https://www.melon.com/index.htm
[top100]: https://www.melon.com/chart/index.htm
[newsong]: https://www.melon.com/new/index.htm
[genre]: https://www.melon.com/genre/song_list.htm?gnrCode=GN0100

# 사용법
   1. 버전에 맞는 크롬 드라이버를 다운로드
   2. 크롤링 코드가 있는 디렉터리에 드라이버를 두기
   3. 원하는 정보가 있는 페이지의 URL을 복사하여 코드 내의 `url` 변수에 할당
   4. 크롤링!

CSV 파일의 변수명 별 저장하는 정보입니다.

|변수명|내용|
|-----|-----|
|`num`|크롤링 순서|
|`songname`|노래 이름|
|`artist`|가수 이름|
|`album`|앨범명|
|`date`|발매일|
|`genre`|장르|
|`lyric`|가사|

# 개선사항
신곡 정보를 자주 수집하게 될 경우를 염두에 두어 파일 이름에 자동으로 수집 일시 정보를 추가하도록 수정하였습니다.

파일명 예시 - songdata_2024.01.01.csv