u="$1"; f=pages/$(echo "$u" | md5sum | cut -c1-12).html
curl -sL -m 20 -A "Mozilla/5.0 (compatible; dortus-onderzoek)" "$u" -o "$f"; sleep 0.3
