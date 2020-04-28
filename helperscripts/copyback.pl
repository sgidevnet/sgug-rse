#!/usr/sgug/bin/perl

use File::Find;
use File::Copy;
use File::HomeDir;

# YOU MUST RUN THIS AT THE REPO ROOT

# Basic idea
# Look for each .spec under the current dir.
# Get the parent directory and for all files under there,
# See if there exists anything in ~/rpmbuild/SUBPATH
# If it does - copy it to local version.

my @gitrepomatches;
find( { wanted => sub { push @gitrepomatches, $_ }, no_chdir => 1}, "packages");

my @packagedirs;

for $localspecfile (@gitrepomatches)
{
    $_ = $localspecfile;
    if( m|packages/(.*)/SPECS/(.*)\.spec$| ) {
	
	my $packagedir = $1;
	my $specname = $2;
	print "Found: $localspecfile\n";
	print "Found: $packagedir\n";
	print "Found: $specname\n";
	push(@packagedirs,$packagedir);
	if( $packagedir ne $specname ) {
	    print "Warning! Mismatch on $localspecfile\n";
	}
    }
}

# Now for each package dir, find each file under it
# If we can find such a file under ~/rpmbuild, copy it over
for $packagedir (@packagedirs) {
    my @FOUNDFILES = glob "packages/$packagedir/*/*";


    for $foundfile (@FOUNDFILES) {
	$_ = $foundfile;
	if( m|packages/[^\/]+/.*\.spec\.orig.*| ) { print("Skipping $foundfile\n"); next; };
#	print("Found $foundfile\n");
	m|packages/([^\/]+)/(.*)|;
	my $packageName = $1;
	my $sourceFile = $2;
#	print "Package is $packageName\n";
#	print "SourceFile is $sourceFile\n";

	my $rpmbuildFile = File::HomeDir->my_home."/rpmbuild/$sourceFile";
	my $targetFile = "./packages/$packageName/$sourceFile";

	if( -e $rpmbuildFile) {
	    my $cmd = "cp $rpmbuildFile $targetFile";
	    print "Command is '$cmd'\n";

	    copy($rpmbuildFile, $targetFile) or die "Copy failed: $!";
	}
    }
}

