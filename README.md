# iface_tools_pl_cgi

## 概要

ネットワークインターフェイス関連ツール (Perl) (CGIインターフェイス)

このパッケージは、
クライアントホストからWeb サーバのCGI にアクセスすることによって、
Web サーバにログインすることなく
[iface_tools_pl](https://github.com/yuksiy/iface_tools_pl)
が提供しているツールと同様の機能を利用できるようにします。

例えば、自ネットワーク内に稼働中のLinux ルータがあり、
そのルータが外部のISP にPPPoE で接続し、さらに
そのルータがLAN 側からのみアクセス可能な管理用のWeb サーバを提供している場合、
LAN 側に在籍しているネットワーク管理者が
そのルータにログインすることなく、
ISP からルータのWAN 側に付与されたIPアドレスを知るために
本パッケージのCGI を使用する、
といった利用方法を想定しています。

そのため、現状では
[iface_tools_pl/README.md](https://github.com/yuksiy/iface_tools_pl/blob/master/README.md)
の中の「iface_addr.pl get」相当の機能のみを提供しています。

## 使用方法

### iface_addr.cgi

「ppp0」インターフェイスに割り当てられたIPv4アドレスを取得する場合、以下のURLにアクセスします。

    http://Webサーバのホスト名/local-cgi/iface_addr.cgi?action=get&l=ppp&f=inet&a=local&iface=ppp0

### その他

* 上記の「http\://Webサーバのホスト名/local-cgi」の部分は、それぞれの環境に応じて読み替えてください。

* 上記で紹介したツールの詳細については、「*.cgi」ファイルのヘッダー部分を参照してください。

## 動作環境

OS:

* Linux (Debian)

依存パッケージ または 依存コマンド:

* make (インストール目的のみ)
* perl
* [iface_tools_pl](https://github.com/yuksiy/iface_tools_pl)

## インストール

ソースからインストールする場合:

    (Debian の場合)
    # make install

fil_pkg.plを使用してインストールする場合:

[fil_pkg.pl](https://github.com/yuksiy/fil_tools_pl/blob/master/README.md#fil_pkgpl) を参照してください。

## インストール後の設定

本パッケージが提供するCGIスクリプトが有効になるように、
Web サーバ側にて適切な設定を行ってください。

## 最新版の入手先

<https://github.com/yuksiy/iface_tools_pl_cgi>

## License

MIT License. See [LICENSE](https://github.com/yuksiy/iface_tools_pl_cgi/blob/master/LICENSE) file.

## Copyright

Copyright (c) 2011-2017 Yukio Shiiya
