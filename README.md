# e-mail-sending
Pythonでメール送信を実装しました

用いたライブラリは以下の二つです．
- email
- smtplib

両方とも標準ライブラリのため，pip installする必要はないです．

このスクリプトをwindows10のタスクスケジューラーに登録し，自動送信を実現しました．

# タスクスケジューラーへのPythonスクリプトの登録方法
- ctrl + Rを押す
- 出てきたボックスに，Taskschd.msc，を入力する(タスクスケジューラーの起動される)
- フォルダをタスクスケジューラーライブラリに変える
- 基本タスクの生成
- 名前と説明をわかるように入力
- 次へ
- いつタスクを開始するか指定(毎日，毎週，毎週，1回限り，コンピューターの起動時，ログオン時，特定のイベントへのログの記録時)
- 次へ
- 具体的ないつやるかの指定
- 次へ
- プログラムの開始
- 次へ
- プログラム/スクリプトの欄へ，python.exeを指定する
- 引数の追加の欄へ，pythonスクリプトのファイル名を指定する
- 開始(オプション)の欄へ，pythonスクリプトのある場所(パス)を指定する
- 次へ
- 完了
