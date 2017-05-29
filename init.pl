#!/usr/bin/perl

use File::Path;
use Proc::Background;
use File::Slurper qw/write_text read_text/;

mkpath '/home/pi/photos';
mkpath '/media/usb';
unlink '/home/pi/lock.txt';

if (-e '/dev/sda1'){
  my $pb1 = Proc::Background->new("cp /home/pi/photos/* /media/usb/");
  $pb1->wait();
  my $pb2 = Proc::Background->new("umount /media/usb");
  $pb2->wait();
  my $pb3 = Proc::Background->new("python /home/pi/message.py Files Coppied.");
  $pb3->wait();
  system("halt -p now");
}
my $val = 0;
if (!(-e "/home/pi/last.txt")){
  write_text("/home/pi/last.txt",0);
}

