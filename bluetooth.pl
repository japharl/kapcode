#!/usr/bin/perl

print "ENSURE THIS SCRIPT IS RUN AS ROOT.\n";
print "Please enter the bluetooth address of your headphones: ";
my $x = <STDIN>;
$x =~ chomp($x);

print "Writing configs...\n";

my $OUT;

open($OUT,">","/home/pi/kapcode/bluetooth.txt");
print $OUT $x ;
close $OUT;

open($OUT,">","/etc/rc.local");
print $OUT "#!/bin/bash\n";
print $OUT "echo 'connect $x \n quit' | bluetoothctl \n";
close $OUT;
