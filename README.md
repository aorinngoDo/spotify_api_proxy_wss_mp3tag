# Spotify API Proxy + Mp3Tag Web Source Script

Spotify APIは利用にヘッダ認証が必要であるため、Mp3TagのWeb Source Script単体では利用できない。

簡素なプロキシをローカルサーバーに立てることで、Spotify APIの情報を利用できるようにしている。

Spotify API requests require header authentication, so it is not possible to use it with Mp3Tag's Web Source Script alone.

By setting up a simple proxy on a local server, you can use Spotify API information.

## 利用方法

- Python3が動作する環境が必要
  - [Python Windows embeddable package](https://www.python.org/downloads/windows/) (Windows専用), [indygreg/python-build-standalone](https://github.com/indygreg/python-build-standalone) などを利用すると簡単

1. `.src` ファイルを `%APPDATA%\Mp3tag\data\sources` フォルダにコピーする

2. [spotify_api_proxy_config_example.py](spotify_api_proxy_config_example.py) を `spotify_api_proxy_config_example.py` にリネームして、`CLIENT_ID`, `CLIENT_SECRET` を自分で発行したものに変更する (参照: [Getting started with Web API | Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started))

3. `python spotify_api_proxy.py` でプロキシサーバーを立ち上げる
   - 1時間でトークンが切れるので、必要に応じて再起動する
   - ファイアウォールで許可の設定が必要な場合がある

4. Mp3TagでWeb Source Scriptを利用する

## Usage

- Requires an environment where Python3 can run
  - [Python Windows embeddable package](https://www.python.org/downloads/windows/) (Windows only), [indygreg/python-build-standalone](https://github.com/indygreg/python-build-standalone) etc. make it easy

1. Copy the `.src` file to the `%APPDATA%\Mp3tag\data\sources` folder

2. Rename [spotify_api_proxy_config_example.py](spotify_api_proxy_config_example.py) to `spotify_api_proxy_config.py` and change `CLIENT_ID`, `CLIENT_SECRET` to the ones you issued (see: [Getting started with Web API | Spotify for Developers](https://developer.spotify.com/documentation/web-api/tutorials/getting-started))

3. Start the proxy server with `python spotify_api_proxy.py`
   - The token expires in 1 hour, so restart as needed
   - You may need to set up permissions in the firewall

4. Use the Web Source Script in Mp3Tag

## Notes

- **For users outside Japan, it is recommended to change `market=JP` in the `.src` file to the appropriate country code.**
- **The proxy server is buggy and not secure. Use at your own risk.  プロキシササーバは不安定で、セキュリティが保証されていません。自己責任で使用してください。**
