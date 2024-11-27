# ハンズオン用資料
# 基礎知識
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

# ①年齢モデルのConda 環境を構築する方法
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
conda install -c defaults -c conda-forge pytorch=1.9.0 torchvision=0.10.0 numpy=1.22.1 pillow=9.0.0 tqdm=4.62.3 ipywidgets=8.0.2 -y
pip install timm==0.5.4 opencv-python
```
### 4. (別手順)当レポジトリ内のymlファイルを使用した場合
```bash
conda env create -f [age_env.ymlへのパス]
conda activate age_env
```

# ②性別モデルのConda 環境を構築する方法
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
```bash
conda install -c defaults -c conda-forge tensorflow=2.4.0 matplotlib pandas scikit-learn jupyter jupyterlab ipywidgets seaborn plotly numpy scipy scikit-image pillow h5py keras
pip install opencv-python=4.3.0.36
```
### 4. (別手順)当レポジトリ内のymlファイルを使用した場合
```bash
conda env create -f [gender_env.ymlへのパス]
conda activate gender_env
```

