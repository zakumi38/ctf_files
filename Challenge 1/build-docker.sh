#!/bin/sh
docker rm web_ddllmmaa
docker build -t web_ddllmmaa .
docker run --name=web_ddllmmaa -p 1337:1337 -it web_ddllmmaa
