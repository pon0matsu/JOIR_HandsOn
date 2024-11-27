# ハンズオン用資料
# 概要
## Anaconda環境構築
https://www.anaconda.com/download/ <br>
・Eメールアドレスを登録し、ダウンロードページヘ。<br>
・OSに合わせたインストーラーをダウンロード。<br>
・インストーラーを使用して、インストール。<br>

## 仮想環境構築
WindowsならAnaconda prompt, MacOSならterminalを起動する。<br>
### Windows (Anaconda prompt)<br>
conda create -n [環境名] python=[version] <br>
### Mac (terminal)<br>
conda create -n [環境名] python=[version] <br>
### 環境を起動する際には　conda activate [環境名]　を実行<br>

## ライブラリをインストール
### Windows (Anaconda prompt)<br>
(環境名) > conda install [ライブラリ名]<br>
### Mac (terminal)<br>
$ conda install [ライブラリ名]<br>

# <span style="color:blue;">Conda 環境をYAMLファイルなしで構築する方法</span>
この手順では、ターミナルから直接コマンドを実行して`gender_env`という名前のConda環境を構築します。
---
## 手順
### 1. 新しい環境を作成
以下のコマンドで、Python 3.8を使用する新しい環境を作成します。
```bash
conda create -n gender_env python=3.8
