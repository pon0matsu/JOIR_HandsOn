# ハンズオン資料
## Anaconda環境構築
https://www.anaconda.com/download/ <br>
・Eメールアドレスを登録し、受信したEmailからダウンロードページヘ移動してください。<br>
・OSに合わせたインストーラーをダウンロードします。<br>
・インストーラーを使用して、Anacondaをインストールしてください。<br>

## 基本的な仮想環境構築コード
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

# ①年齢モデルのConda 環境を構築する方法　<br>
この手順では、ターミナルから直接コマンドを実行して`age_env`という名前のConda環境を構築します。<br>
http://www.joir.jp/data/<br>
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
pip install torch==1.9.0 torchvision==0.10.0 numpy==1.22.1 pillow==9.0.0 tqdm==4.62.3 ipywidgets==8.0.2 timm==0.5.4
```

# ②性別モデルのConda 環境を構築する方法<br>
この手順では、ターミナルから直接コマンドを実行して`gender_env`という名前のConda環境を構築します。<br>
http://www.joir.jp/data/<br>
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
### 3. 必要なパッケージをインストール (Apple Silicon以外)
pip installが可能であるopencv-python==4.3.0.38に変更しています。（本来はopencv-python==4.3.0.36）<br>
```bash
pip install tensorflow==2.4.0 opencv-python==4.3.0.38
```
### 3. 必要なパッケージをインストール (Apple Siliconのみ)
Apple Silicon(M1以降のCPU)では、指定のバージョンでは動作しないため、バージョンの指定はなし<br>
動作確認：tensorflow=2.13.0、opencv-python==4.10.0<br>
```bash
pip install tensorflow opencv-python
```


