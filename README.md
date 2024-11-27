# ハンズオン用資料
## 基礎知識
## Anaconda環境構築
https://www.anaconda.com/download/ <br>
・Eメールアドレスを登録し、ダウンロードページヘ。<br>
・OSに合わせたインストーラーをダウンロード。<br>
・インストーラーを使用して、インストール。<br>

## 仮想環境構築
WindowsならAnaconda prompt, MacOSならterminalを起動する。<br>
### Windows (Anaconda prompt)<br>
```bash
conda create -n [環境名] python=[version]
```
### Mac (terminal)<br>
```bash
conda create -n [環境名] python=[version]
```
### 環境を起動する際には　conda activate [環境名]　を実行<br>

## ライブラリをインストール
### Windows (Anaconda prompt)<br>
```bash
conda install [ライブラリ名]
```
### Mac (terminal)<br>
```bash
conda install [ライブラリ名]
```

# ①年齢モデルのConda 環境を構築する方法<br>
この手順では、ターミナルから直接コマンドを実行して`age_env`という名前のConda環境を構築します。<br>
---
## 手順
### 1. 新しい環境を作成
以下のコマンドで、Python 3.8を使用する新しい環境を作成します。<br>
```bash
conda create -n age_env python=3.8 -y
```
### 2. 環境を有効化
```bash
conda activate age_env
```
### 3. 必要なパッケージをインストール
```bash
pip install pytorch=1.9.0 torchvision=0.10.0 numpy=1.22.1 pillow=9.0.0 tqdm=4.62.3 ipywidgets=8.0.2 timm==0.5.4 opencv-python
```

# ②性別モデルのConda 環境を構築する方法<br>
この手順では、ターミナルから直接コマンドを実行して`gender_env`という名前のConda環境を構築します。<br>
---
## 手順
### 1. 新しい環境を作成
以下のコマンドで、Python 3.8を使用する新しい環境を作成します。<br>
```bash
conda create -n gender_env python=3.8
```
### 2. 環境を有効化
```bash
conda activate gender_env
```
### 3. 必要なパッケージをインストール
pip installが可能であるopencv-python==4.3.0.38に変更しています。（本来はopencv-python==4.3.0.36）<br>
```bash
pip install tensorflow=2.4.0 opencv-python==4.3.0.38
```

# Apple Silicon等Localでの実施が困難な場合
Google Colabを使用<br>
Google ColabのセルはPythonコードを記述して実行するために使われることが多いのですが、セルの先頭に%%shellと書くことで、PythonではなくLinuxコマンド（Shellコマンド）を実行するためのセルに切り替えることができるため、それを利用した形になります。<br>
## 年齢モデル
https://colab.research.google.com/drive/1NPL-hKVARE5jmI6de4gopxNJGPS3yixd?usp=sharing　<br>
Google Colabのノートブックを自身のGoogle Driveにコピーし、使用開始　<br>
①モデルデータ、age_colab.py(本来のコードを一部修正)、眼底写真が画像を一時的にアップロードする。<br>
②Minicondaを使用して、環境構築をしており、最終的にage_colab.pyの内容を実行<br>

## 性別モデル
https://colab.research.google.com/drive/1Y0SDYc7883lM8XpokjIFfJusRTeluP5A?usp=sharing　<br>
Google Colabのノートブックを自身のGoogle Driveにコピーし、使用開始　<br>
①モデルデータ、gender_colab.py(本来のコードを一部修正)、眼底写真が画像を一時的にアップロードする。<br>
②Minicondaを使用して、環境構築をしており、最終的にage_colab.pyの内容を実行<br>
