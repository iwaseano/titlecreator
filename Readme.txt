Readme.txt
Internal TitleCreator
Created by Yosuke Iino

-------------------
◆ .exe ファイルの場所
===================
右上にある [Clone or Download] から git clone するか .zip で入手してください。

dist/TitleCreator/TitleCreator.exe
[TitleCreator.exe] をショートカットにするなりピン止めするなりして使ってください。

-------------------
◆ 使用する前に
===================
Edge のバージョンが "17763" である必要があります。
「オプション機能の管理」-->「機能の追加」から、"Microsoft WebDriver" をインストールする必要があります。

-------------------
◆ 以前との変更点
===================
・[Status]に"MR"を追加しました。
・[Service Level] のデフォルト値を "Proffesional" へと変更しました。
・Scrape ボタンを押すことで、自動的に [Severity]、[Product]、[Title] が入力されるようになりました。

基本今までの Title Creator と同じように使えるはず。

-------------------
◆ Scrape 機能について
===================

SR 番号を入力し、【Scrape】ボタンを押すと、自動的に [Severity]、[Product]、[Title] が入力されます。

また、取得時には、Edge が起動していない必要があります。
【Scrape】ボタンを押す前に Edge を終了させる必要があります。

-------------------
◆ Update 案
===================

・自由編集欄を追加する
・取得に失敗した際に、エラーメッセージを表示させる

-------------------
◆ Release Note
===================

2020/02/19 v1.00: 作成
2020/02/21 v1.01: レイアウトの修正
2020/02/21 v1.02: [Service Level] のデフォルト値を "Proffesional" へ変更
2020/03/02 v1.03: Scrape 機能を追加
