use Proc::Background;
use File::Slurp;

if (-e '/dev/sda1'){
  print "USB Detected.\n";
  if (-e '/tmp/write.lock'){
    print "Exiting!\n";
  } else {
    system('touch /tmp/write.lock');
    system('mount /dev/sda1 /media/data');
    system ("cp -R /home/pi/data/* /media/data/");
    system('rm /tmp/write.lock');
    system('sudo shutdown -h -P now');
  }
}
else {
  print "Taking photos!\n";
  if (!(-e '/home/pi/last.txt')){
    write_file('/home/pi/last.txt',0);
  }
  my $num = read_file( '/home/pi/last.txt' ) ;
  $num = $num + 1;
  print "Image # $num\n";
  my $pb = Proc::Background->new('raspistill -o /home/pi/data/image.' . $num . '.jpg');
  $pb->wait();
  write_file( '/home/pi/last.txt', $num ) ;
}

