# run

```
docker-compose up
```

visit `localhost:30080`

# sources

- https://developer.ibm.com/code/2017/07/13/step-step-guide-running-gitlab-ce-docker/
- https://docs.gitlab.com/omnibus/docker/

# user

- root
- password

# add ssh key

- generate `~/.ssh/yourkey.pub`
- copy `~/.ssh/yourkey.pub`
- add SSH key: `Profile` > `Settings` > `SSH Keys` > paste into `Key` > `Add key`

# push code (should just work with ssh)

```
git remote add local yourprojecturl
git push local master
```

# run flask redis compose

```
cd ~/projects/docker/flask-redis-compose
docker compose up
```

# test post endpoint

```
curl -v localhost:5000/trigger -X POST
```

expected:
```
*   Trying 127.0.0.1...
* Connected to localhost (127.0.0.1) port 5000 (#0)
> POST /trigger HTTP/1.1
> Host: localhost:5000
> User-Agent: curl/7.47.0
> Accept: */*
> 
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 28
< Server: Werkzeug/0.14.1 Python/3.4.9
< Date: Sun, 25 Nov 2018 17:20:17 GMT
< 
triggered the post endpoint
* Closing connection 0
```

# add web hook to gitlab

`project` > `settings` > `integrations` > paste `http://localhost:5000/trigger` > `Add webhook`

# test the web hook

```
gitlab_1_d27547e6f149 | Errno::EADDRNOTAVAIL (Failed to open TCP connection to localhost:5000 (Cannot assign requested address - connect(2) for "localhost" port 5000)):
```
