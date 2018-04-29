use File::Path;
use Proc::Background;
use File::Slurper qw/write_text read_text/;

mkpath '/home/pi/kapcode/photos';
mkpath '/media/usb';
my $flag = 0;

if (-e '/dev/sda1'){
  my $pb0 = Proc::Background->new("mount -t vfat /dev/sda1 /media/usb");
  $pb0->wait();
  my $pb1 = Proc::Background->new("cp /home/pi/kapcode/photos/* /media/usb/");
  $pb1->wait();
   my $pb2x = Proc::Background->new("/bin/rm -rf /home/pi/kapcode/photos/*");
   $pb2x->wait();
   write_text("/home/pi/kapcode/last.txt",0);
  # If the file exit exists on the root of the usb device, the script will exit, not shutdown the pc, and will not start the camera script.
  if (-e "/media/usb/exit"){
    my $pbe = Proc::Background->new("touch /home/pi/kapcode/exit");
    $pbe->wait();
    $flag = 1;
  }
  my $pb2 = Proc::Background->new("umount /media/usb");
  $pb2->wait();
  my $pb3 = Proc::Background->new("python /home/pi/kapcode/message.py Files Coppied.");
  $pb3->wait();
  if ($flag == 0){
    system("halt -p");
  }
}
my $val = 0;
if (!(-e "/home/pi/kapcode/last.txt")){
  write_text("/home/pi/kapcode/last.txt",0);
}
