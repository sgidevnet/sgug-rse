Summary: OpenBSD SNDIO audio daemon ported to IRix by TruHobbyist
Name: sndio
Version: 1.8.1
Release: 1
License: BSD
Group: System
Source0: https://sndio.org/sndio-1.8.1.tar.gz
# put that in $rpmbuild/SOURCES and smoke it
# First patch applies TruHobbyist's changes, second makes it compile with GCC
Patch0: sndio.th.patchdiff
Patch1: sndio-sgug-fix.patch

%description
Audio daemon from the BSD folks, modified to be compatible with SGI/Irix systems.

%prep
%setup -q
%autopatch -p1

%build
# Not using Macro as it passes flags that get rejected, these are otherwise the same as defaults
./configure --prefix=/usr/sgug --libdir=/usr/sgug/lib32 --pkgconfdir=/usr/sgug/lib32/pkgconfig
make

%install
rm -rf %{buildroot}
%make_install prefix=${RPM_BUILD_ROOT}%{_prefix}
## TODO
## ADD SERVICES here
## contrib/init.d.sndiod.sgi
## ADD sndiod USER during %pre

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/aucat
%{_bindir}/midicat
%{_bindir}/sndioctl
%{_bindir}/sndiod
%{_includedir}/sndio.h
%{_libdir}/pkgconfig/sndio.pc
%{_libdir}/libsndio.so
%{_libdir}/libsndio.so.7.2
%doc /usr/sgug/share/man/man1/aucat.1.gz
%doc /usr/sgug/share/man/man1/midicat.1.gz
%doc /usr/sgug/share/man/man1/sndioctl.1.gz
%doc /usr/sgug/share/man/man3/mio_*.3.gz
%doc /usr/sgug/share/man/man3/sio*.3.gz
%doc /usr/sgug/share/man/man7/sndio.7.gz
%doc /usr/sgug/share/man/man8/sndiod.8.gz


# No devel package, this thing's like two megabytes and I'm lazy, you get all of it

%changelog
* Wed Sep 7 2022 Jenna16bit jenna16bit@github
Add initial version by TruHobbyist, modified slightly for the SGUG compiler environment by Jenna16bit
