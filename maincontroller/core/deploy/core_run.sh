#!/bin/sh
sshpass -p $3 scp ~/parsersmaincontroller/ParsersMainController/vkparsers/deploy/vk_project.zip  adminroot@185.177.93.157:~/
sshpass -p $3 scp ~/parsersmaincontroller/ParsersMainController/vkparsers/deploy/vk_deploy.sh  adminroot@185.177.93.157:~/
echo "$1@$2:/home/$1/"
sshpass -p $3 ssh -t -t  $1@$2 <<EOF
	echo "on serve"
	ls
	apt-get install unzip
	bash vkparsers/deploy/vk_deploy.sh $4 &
EOF

