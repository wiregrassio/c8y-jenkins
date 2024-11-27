clear
docker container run \
-it \
--rm \
-e CUMULOCITY_USERNAME='Elliot' \
-e CUMULOCITY_PASSWORD='-7rEr-*2NHEAKQ.D' \
-e CUMULOCITY_URL='https://elliotwillis.us.cumulocity.com' \
-v $(pwd)/step_1.py:/home/step_1.py \
-v $(pwd)/mappings:/home/mappings \
wiregrass:jenkins_scripts
