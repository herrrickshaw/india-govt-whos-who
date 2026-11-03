#!/bin/bash
# usage: fetch.sh url outfile
UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
curl -sS -L -A "$UA" --max-time 40 -o "$2" -w "%{http_code} %{size_download} %{url_effective}\n" "$1"; sleep 1
