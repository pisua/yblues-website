#!/bin/bash
echo $#
if [ "$#" -ge 3 ]
then
        DIRECTORY=$1
        DOCKER_REPOSITORY=$2
        DOCKER_TAG=$3
        DOCKER_FILE=$4

        DOCKER_FULL_NAME="$DOCKER_REPOSITORY:$DOCKER_TAG"
        DOCKER_FULL_NAME_LATEST="$DOCKER_REPOSITORY:latest"

        cd $DIRECTORY
        echo -e "\x1B[1;32m---- Building docker image \x1B[1;33m[$DOCKER_LOCAL_TAG]\x1B[1;32m...\x1B[0m"


        echo "Building RELEASE version .."
        echo "Tag=$DOCKER_FULL_NAME"
        echo "Tag=$DOCKER_FULL_NAME_LATEST"
        echo "docker buildx build --force-rm=true --pull=true --tag=\"$DOCKER_FULL_NAME\"  -f $DOCKER_FILE \"$(pwd)\""
        docker buildx build --force-rm=true --pull=true --tag="$DOCKER_FULL_NAME"  -f $DOCKER_FILE "$(pwd)"


        if [ "$?" -eq 0 ]
        then
                echo -e "\x1B[1;32m---- Build finished.\x1B[0m"

                #echo -e "\x1B[1;32m---- Push finished.\x1B[0m"
                echo -e "\x1B[1;32mAll finished locally.\x1B[0m"

                # push to docker hub
                if [ "$#" -ge 5 ]
                then
                        echo -e "\x1B[1;32mPushing to Docker Hub...\x1B[0m"
                        docker login -u $4 -p $5
                        echo "docker push $DOCKER_FULL_NAME"
                        docker push $DOCKER_FULL_NAME
                        docker push $DOCKER_FULL_NAME_LATEST


                else
                        echo -e "\x1B[1;32m[WARN] You have not provided your Docker Hub user/pass. Images are not pushed to the Hub!\x1B[0m"
                fi

                echo -e "\x1B[1;32mAll finished.\x1B[0m"
        else
                echo -e "\x1B[1;32m[ERROR] Build error!\x1B[0m"
        fi
        cd ..
else
        echo -e "\x1B[1;32m[ERROR] Invalid parameters! Usage: build_image.sh <directory> <image_repo> <image_tag>\x1B[0m"
fi