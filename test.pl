use Proc::Background;
use File::Slurp;

# This should be run as root in the /home/pi directory.
# called via cronjob.

if (!(-e "/media/data")){
   my $pb = Proc::Background->new("mkdir /media/data");
   $pb->wait();
}

if (-e '/dev/sda1'){
  print "USB Detected.\n";
  if (-e '/tmp/write.lock'){
    print "Exiting!\n";
  } else {
    system('touch /tmp/write.lock');
    system('mount /dev/sda1 /media/data');
    if (-e "/media/data/rm.txt"){
      system ("rm /home/pi/data/*");
      system ("rm /home/pi/last.txt");
      system ("rm /tmp/write.lock");
      system ("sudo shutdown -h -P now");
    }
    system ("cp -R /home/pi/data/* /media/data/");
    system('rm /tmp/write.lock');
    system('sudo shutdown -h -P now');
  }
}
else {
# Fill in here.
}

