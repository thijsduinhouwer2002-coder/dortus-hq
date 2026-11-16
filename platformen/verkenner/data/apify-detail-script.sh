#!/bin/bash
f="det/$1.json"; [ -s "$f" ] && exit 0
curl -s -m 30 "https://api.apify.com/v2/acts/$1" -o "$f"
