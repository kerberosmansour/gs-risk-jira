echo "*****************************"
echo "*** Building docker image ***"
echo "*****************************"

cd bin/Docker

docker build --no-cache -t gs-risk-jira .      || exit 1


#docker run -it -p 5000:5000 gs-risk-jira bash
