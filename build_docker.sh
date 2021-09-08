#!/bin/bash

DIR="`dirname \"$0\"`"

DIRECTORY="$DIR"
DOCKER_REPOSITORY="apisu/yblues"

DOCKER_TAG=2.0.1
DOCKER_USER=$1
DOCKER_PASSWORD=$2

echo -e "\x1B[1;32m[INFO] Building Image [$DOCKER_REPOSITORY:$DOCKER_TAG] located on [$DIRECTORY]\x1B[0m"

DIR="`dirname \"$0\"`"

echo "build and push on nexus user=$DOCKER_USER password=$DOCKER_PASSWORD "
bash $DIR/build_image.sh "$DIRECTORY" "$DOCKER_REPOSITORY" "$DOCKER_TAG" Dockerfile $DOCKER_USER $DOCKER_PASSWORD
