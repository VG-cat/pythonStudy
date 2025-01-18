#! /bin/bash
echo "开始更新软件源......"
sudo apt update
until [[ $? == 0 ]]; do
	echo "update 失败，重新安装"
	sudo apt update
done
echo "开始安装mysql......"
echo "注意 安装过程中会提示设置mysql密码"
sleep 3
sudo apt install mysql-server mysql-client
until [[ $? == 0 ]]; do
	#statements
	echo " mysql安装失败，重新安装"
	sudo apt install mysql-server mysql-client
done
echo "开始安装常用软件......"
sudo apt install build-essential cmake python-dev ctags silversearcher-ag libncurses5-dev libgnome2-dev libgnomeui-dev  libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git vim gcc g++ mono-xbuild python-pip python3-pip virtualenv virtualenvwrapper redis-server mongodb sl
until [[ $? == 0 ]]; do
	echo " install 失败，重新安装"
	sudo apt install build-essential cmake python-dev ctags silversearcher-ag libncurses5-dev libgnome2-dev libgnomeui-dev  libgtk2.0-dev libatk1.0-dev libbonoboui2-dev libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git vim gcc g++ mono-xbuild python-pip python3-pip virtualenv virtualenvwrapper redis-server mongodb sl
done

echo "开始安装python软件......"
pip3 install ipython tree
until [[ $? == 0 ]]; do
	echo "pip 失败，重新安装"
	pip3 install ipython tree
done

echo "开始vim安装配置......"
tar xf ./vim.tar.gz -C ~/
echo "vim配置完成"
echo "开始创建python3虚拟环境......"
echo "创建爬虫虚拟环境spider......"
sleep 3
cd ~
cd ./.virtualenvs
if [ $? != 0 ]
	then
	mkdir ~/.virtualenvs
	cd ./.virtualenvs
fi
virtualenv spider -p python3
until [[ $? == 0 ]]; do
	#statements
	echo "虚拟环境创建失败，重新创建"
	virtualenv spider -p python3
done
echo "spider虚拟环境创建"
source ./spider/bin/activate
until [[ $? == 0 ]]; do
	#
	echo " 进入虚拟环境失败，重新进入"
	source ./spider/bin/activate
done
echo "安装爬虫依赖包"
pip install requests scrapy redis pymongo pymysql scrapy-redis
until [[ $? == 0 ]]; do
	#
	echo "爬虫依赖包安装失败，重新安装"
	pip install requests scrapy redis pymongo pymysql scrapy-redis
done
deactivate
echo "创建dajngo虚拟环境......"
virtualenv django -p python3
until [[ $? == 0 ]]; do
	#statements
	echo "虚拟环境创建失败，重现创建"
	virtualenv django -p python3
done
source ./django/bin/activate
until [[ $? == 0 ]]; do
	#
	echo " 进入虚拟环境失败，重新进入"
	source ./django/bin/activate
done
pip install django redis pymongo pymysql 
deactivate
cd ~
user=$(whoami)
echo "虚拟环境配置完成"
clear
echo "  "
echo "666666666666666666666666666666666666666666666666666666666666666666666"
echo "配置完成,${user},开始你的代码旅程......"
sleep 5
sl -F
sleep 3
echo "  "
echo "  "
echo "接下来还没完"
echo "还有彩蛋哦！"
IFSbak=$IFS
IFS="\n"
while read -r line 
do
    #statements
    echo ${line}
    sleep 0.2
done < .hide 
IFS=$IFSbakZZ
echo "安装完成"
echo "重启计算机"
sleep 10
init 6
