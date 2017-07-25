#!/usr/bin/perl

# ==============================================================================
#   機能
#     インターフェイスのアドレス処理
#   構文
#     USAGE 参照
#
#   Copyright (c) 2011-2017 Yukio Shiiya
#
#   This software is released under the MIT License.
#   https://opensource.org/licenses/MIT
# ==============================================================================

######################################################################
# 基本設定
######################################################################
use strict;
use warnings;

use CGI qw(:standard);

######################################################################
# 変数定義
######################################################################
# ユーザ変数

# システム環境 依存変数

# プログラム内部変数
my $action;

my $IFACE;

my $LINK = "ether";
my $FAMILY = "inet";
my $ADDRESS = "local";
my $SCOPE = "global";

my $param;
my @IFACE_ADDR_GET_OPTIONS;
my @addr;
my $addr;

######################################################################
# 関数定義
######################################################################
sub USAGE {
	print <<EOF;
Usage:
  iface_addr.cgi?action=get& [OPTIONS ...] &iface=IFACE

IFACE_ADDR_OPTIONS:
  l=LINK    : {ether|ppp}
  f=FAMILY  : {link|inet|inet6}
  a=ADDRESS : {local|broadcast|peer}
  s=SCOPE   : {global|site|link|host}
EOF
}

use Iface_tools::Iface_addr;

sub HTTP_ERR_EN {
	print
		header(-type => "text/html", -charset => "UTF-8", -status => 500),
		start_html(-title => "500 Internal error",
		           -declare_xml => "1", -lang => "en-US", -encoding => "UTF-8"),
		@_,
		end_html;
	return;
}

######################################################################
# メインルーチン
######################################################################

# 変数の取得
foreach $param (param()) {
	if ( $param eq "action" ) {
		$action = param($param);
	} elsif ( $param eq "iface" ) {
		$IFACE = param($param);
	} elsif ( $param eq "l" ) {
		$LINK = param($param);
	} elsif ( $param eq "f" ) {
		$FAMILY = param($param);
	} elsif ( $param eq "a" ) {
		$ADDRESS = param($param);
	} elsif ( $param eq "s" ) {
		$SCOPE = param($param);
	} else {
		HTTP_ERR_EN(h2("-E Invalid parameter -- \"$param\""));
		exit 1;
	}
}

# ACTIONのチェック
if ( not defined($action) ) {
	HTTP_ERR_EN(h2("-E Missing ACTION"));
	exit 1;
} else {
	if ( $action !~ m#^(?:get)$# ) {
		HTTP_ERR_EN(h2("-E Invalid ACTION -- \"$action\""));
		exit 1;
	}
}

# 引数のチェック
if ( $action =~ m#^(?:get)$# ) {
	# 第1引数のチェック
	if ( not defined($IFACE) ) {
		HTTP_ERR_EN(h2("-E Missing IFACE argument"));
		exit 1;
	}
}

# 変数定義(引数のチェック後)
@IFACE_ADDR_GET_OPTIONS = ("-l", "$LINK", "-f", "$FAMILY", "-a", "$ADDRESS", "-s", "$SCOPE");

if ( $action eq "get" ) {
	# HTTPヘッダの出力
	print header(-type => "text/plain", -charset => "");

	# インターフェイスのアドレスの取得
	@addr = IFACE_ADDR_GET(@IFACE_ADDR_GET_OPTIONS, $IFACE);
	if ( scalar(@addr) > 0 ) {
		foreach $addr (@addr) {
			print "$addr\n";
		}
		exit 0;
	} else {
		exit 1;
	}
}

