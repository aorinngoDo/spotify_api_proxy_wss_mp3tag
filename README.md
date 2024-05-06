# Spotify API Proxy + Mp3Tag Web Source Script

Spotify APIは利用に認証が必要であるため、Mp3TagのWeb Source Script単体では利用できない。

簡素なプロキシをローカルサーバーに立てることで、Spotify APIの情報を利用できるようにしている。

## Usage

1. `.src` ファイルを `%APPDATA%\Mp3tag\data\sources` フォルダにコピーする

2. [spotify_api_proxy_config_example.py](spotify_api_proxy_config_example.py) を `spotify_api_proxy_config_example.py` にリネームして、`CLIENT_ID`, `CLIENT_SECRET` を自分で発行したものに変更する

3. `python spotify_api_proxy.py` でプロキシサーバーを立ち上げる
   - `requests` モジュールが必要
   - 1時間でトークンが切れるので、必要に応じて再起動する

4. Mp3TagでWeb Source Scriptを利用する
