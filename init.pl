use File::Path;
use Proc::Background;

mkpath '/home/pi/photos';
mkpath '/media/usb';
unlink '/home/pi/lock.txt';

if (-e '/dev/sda1'){
  print "USB Attached!";
  my $pb0 = Proc::Background->new("mount -t vfat /dev/sda1 /media/usb");
  $pb0->wait();
  my $pb1 = Proc::Background->new("cp /home/pi/photos/* /media/usb/");
  $pb1->wait();
  my $pb2 = Proc::Background->new("umount /media/usb");
  $pb2->wait();
}
