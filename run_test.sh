clear
docker container run \
-it \
--rm \
-v $(pwd)/step_1.py:/home/step_1.py \
wiregrass:jenkins_scripts