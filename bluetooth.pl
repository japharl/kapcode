#!/usr/bin/perl

print "Please enter the bluetooth address of your headphones: ";
my $x = <STDIN>;
$x =~ chomp($x);

print "Writing configs...\n";

my $OUT;
open($OUT,">","/home/pi/.asoundrc");
print $OUT "defaults.bluealsa.interface \"hci0\"\n";
print $OUT "defaults.bluealsa.device \"$x\"\n";
print $OUT "defaults.bluealsa.profile \"a2dp\"\n";
print $OUT "defaults.bluealsa.delay \"10000\"\n";
close $OUT;
