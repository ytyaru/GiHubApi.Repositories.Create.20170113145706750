# このソフトウェアについて

GitHubのリポジトリ作成APIを実行する。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
* [WinAuth](https://winauth.com/download/)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* [GitHubアカウント](https://github.com/join?source=header-home)を作成する
* [AccessToken](https://github.com/settings/tokens)を1つ以上作成する
* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)でGitHubアカウントDBを作成する
* Main.pyで以下の変数を設定する

```python
db_path = 'C:/GitHub.Accounts.sqlite3'
username = 'github_username'
repo_name = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
repo_description = 'repo desc.'
repo_homepage = 'http://repo'
```

TwoFactor認証アカウントを使う場合、WinAuthで取得できるようにしておく。

* [Two-Factor認証を有効にする設定](https://github.com/settings/two_factor_authentication/intro)を行う
* [WinAuth](https://winauth.com/download/)などでOTP(One-Time-Password)を取得する

# 実行

```dosbatch
python Main.py
```

TwoFactor認証アカウントを使う場合、WinAuthで取得してから実行すると、クリップボードからOTPを取得してAPIを実行する。

WinAuthでOTPを取得してから変更されるまでの間(30秒間)に、`Main.py`を実行すること。

# 結果

リモートリポジトリが生成される。
[Create a new Repository API](https://developer.github.com/v3/repos/#create)の結果が`GiHubApi.Repositories.Create.{id}.json`ファイルに出力される。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
