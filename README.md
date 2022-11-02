Vampire Survivorsのカスタムスキン作成支援ツールです。

## 動作環境
Python3とOpenCVが必要です。
Windowsの場合Python3はMicrosoft Storeからでも入手できます。
Macならデフォルトでインストールされているはずです。

OpenCVは以下のコマンドをコマンドプロンプトやPowerShell、ターミナルで実行することでインストールできます。

```
pip install opencv-python
```


# split.py
characters.jsonに基づきcharacters.pngの各画像を分割します。

## 必要なもの
- 分割したい characters.png
- ↑と同じバージョンの characters.json

## 使い方
1. characters.jsonとcharacters.pngをsplit.pyと同じディレクトリに配置してsplit.pyを実行します。
2.  splitディレクトリ下に分割された画像が保存されます。
  (※ 同名のファイルは上書きされるので注意してください)


# apply.py
characters.pngにカスタムスキンを適用します。

## 必要なもの
- カスタムスキン画像
  - 必要なキャラのみで良いです
  - split.pyで分割される画像と同じ名前、大きさである必要があります
- カスタムスキンを適用したいcharacters.png
- ↑と同じバージョンのcharacters.json

## 使い方
1. apply.pyと同じディレクトリにcustomディレクトリを作成し、その配下にスキン画像を配置します。
2. characters.jsonとcharacters.pngをsplit.pyと同じディレクトリに配置してapply.pyを実行します。
3. characters.pngにカスタムスキンが反映され、元のcharacters.pngのバックアップファイルcharacters.bk.pngが生成されます。
