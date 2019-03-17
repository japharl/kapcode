sudo perl /home/pi/kapcode/init.pl

if [ -f /home/pi/kapcode/exit ]
then
  echo "Exit requested";
  rm /home/pi/kapcode/exit;
  exit 0 ;
fi

sudo chown -R pi:pi /home/pi/kapcode/*
sudo chmod -R 777 /home/pi/kapcode/*
python /home/pi/kapcode/camera.py
shutdown -P now
