#!/usr/bin/perl

use File::Path;
use Proc::Background;
use File::Slurper qw/write_text read_text/;

mkpath '/home/pi/kapcode/photos';
mkpath '/media/usb';

if (-e '/dev/sda1'){
  my $pb1 = Proc::Background->new("cp /home/pi/kapcode/photos/* /media/usb/");
  $pb1->wait();
  my $pb2 = Proc::Background->new("umount /media/usb");
  $pb2->wait();
  my $pb3 = Proc::Background->new("python /home/pi/kapcode/message.py Files Coppied.");
  $pb3->wait();
  system("halt -p now");
}
my $val = 0;
if (!(-e "/home/pi/kapcode/last.txt")){
  write_text("/home/pi/kapcode/last.txt",0);
}

