if [ $EUID -ne 0 ];then
  echo "Please run as root."
  exit 1
fi
read -p "Uninstall (y/n)? " prompt

if [ "$prompt" != "y" ];then
  echo "Exiting..."
  exit 0
fi
read -p "Are you sure you want to uninstall (y/n)? " prompt

if [ "$prompt" != "y" ];then
  echo "Exiting..."
  exit 0
fi


rm /usr/bin/pw-volume-gui
rm -rf /usr/share/pw-volume-gui/
