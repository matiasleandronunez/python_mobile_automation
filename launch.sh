#!/bin/bash

echo "Running docker-compose"
docker-compose up </dev/null &>/dev/null &

status=""

while [[ "`docker inspect -f {{.State.Health.Status}} samsung_galaxy`" != "healthy" ]] || true; status=`docker inspect -f {{.State.Health.Status}} samsung_galaxy`; echo "samsung_galaxy is $status"; if [[ $status == "healthy" ]]; then
    break
  fi; do sleep 5; done;

docker exec -u 0 samsung_galaxy chmod +x /root/tmp/installation_bash_script.sh
docker exec -u 0 samsung_galaxy bash /root/tmp/installation_bash_script.sh
