if [ $EUID -ne 0 ];then
  echo "Please run as root."
  exit 1
fi

echo "Welcome to the pw-volume-gui installer."
echo "If you have not installed pipewire, pw-volume, python3 and tkinter, you will not be able to install this now."
read -p "Install (y/n)? " prompt

if [ "$prompt" != "y" ];then
  echo "Exiting..."
  exit 0
fi

cp main.py /usr/bin/pw-volume-gui
chmod 755 /usr/bin/pw-volume-gui
mkdir /usr/share/pw-volume-gui/
cp COPYING /usr/share/pw-volume-gui/COPYING
cp README.md /usr/share/pw-volume-gui/README.md
echo "Finished! You may now run pw-volume-gui."
