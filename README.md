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

- generate ~/.ssh/yourkey.pub
- copy ~/.ssh/yourkey.pub
- paste into profile settings > ssh keys

# push code (should just work with ssh)

```
git remote add local yourprojecturl
git push local master
```
