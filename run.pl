use Proc::Background;
use File::Slurper qw/write_text read_text/;

# This should be run as pi in the /home/pi directory.
if (-e '/home/pi/lock.txt'){
  exit(0);
} else {
  write_text('/home/pi/lock.txt',1);
}
print "Taking photos!\n";
if (!(-e '/home/pi/last.txt')){
  write_text('/home/pi/last.txt',0);
}
my $num = read_text( '/home/pi/last.txt' ) ;
$num = $num + 1;
print "Image # $num\n";
my $pb = Proc::Background->new('python camera.py > out.txt ');
$pb->wait();
write_text( '/home/pi/last.txt', $num ) ;
my $pb2 = Proc::Background->new("mv /home/pi/image.jpg /home/pi/photos/image_" . $num . ".jpg");
$pb2->wait();
my $pb3 = Proc::Background->new("mv /home/pi/out.txt /home/pi/photos/image_" . $num . ".txt");
unlink '/home/pi/lock.txt';
