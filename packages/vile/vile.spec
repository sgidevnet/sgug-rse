Name:		vile
Version:	9.8t
Release:	4%{?dist}
Summary:	VI Like Emacs
License:	GPLv2
URL:		http://invisible-island.net/vile/
Source0:	https://invisible-mirror.net/archives/vile/current/%{name}-%{version}.tgz
Source1:	xvile.desktop
BuildRequires:	ncurses-devel
BuildRequires:	flex
BuildRequires:	gcc
BuildRequires:	desktop-file-utils
Requires:	%{name}-common = %{version}-%{release}

%package	common
Summary:	The common files needed by any version of the vile editor

%package -n	xvile
Summary:	VI Like Emacs
BuildRequires:	libXpm-devel
BuildRequires:	libXt-devel
BuildRequires:	perl-generators
Requires:	xorg-x11-fonts-misc
Requires:	%{name}-common = %{version}-%{release}


%description	common
vile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.
vile-common provides the files needed for all versions of vile.

%description -n xvile
xvile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.

%description
vile is a text editor which is extremely compatible with vi in terms of "finger
feel".  In addition, it has extended capabilities in many areas, notably
multi-file editing and viewing, syntax highlighting, and key rebinding.

%prep
%setup -q

%build
%configure --with-loadable-filters \
           --disable-rpath-hack \
           --disable-stripping

make %{?_smp_mflags} vile

%configure --with-loadable-filters \
           --disable-rpath-hack \
           --disable-stripping \
           --with-app-defaults=%{_datadir}/X11/app-defaults \
           --with-screen=x11 \
	   --with-icon-theme \
           --with-icondir=%{_datadir}/icons/ \
	   --with-pixmapdir=%{_datadir}/pixmaps/ \
           --with-xpm

make %{?_smp_mflags} xvile
touch vile

%install
make install DESTDIR=%{buildroot} INSTALL='install -p' TARGET='xvile'
make install DESTDIR=%{buildroot} INSTALL='install -p' TARGET='vile'
desktop-file-install --vendor='' --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

ln -s %{_mandir}/man1/xvile.1 %{buildroot}%{_mandir}/man1/uxvile.1
ln -s %{_mandir}/man1/xvile.1 %{buildroot}%{_mandir}/man1/lxvile.1

%files
%{_bindir}/vile
%{_bindir}/vile-pager
%{_bindir}/vile-libdir-path
%{_bindir}/vile-to-html
%{_mandir}/man1/vile*.1.gz

%files common
%doc AUTHORS COPYING CHANGES README doc/*doc
%{_datadir}/vile/
%{_libdir}/vile/

%files -n xvile
%{_bindir}/lxvile
%{_bindir}/lxvile-fonts
%{_bindir}/uxvile
%{_bindir}/xshell.sh
%{_bindir}/xvile
%{_bindir}/xvile-pager
%{_bindir}/xvile-libdir-path
%{_bindir}/xvile-to-html
%{_mandir}/man1/xvile*.1.gz
%{_mandir}/man1/lxvile.1*
%{_mandir}/man1/uxvile.1*
%{_datadir}/pixmaps/vile.xpm
%{_datadir}/icons/hicolor/*/apps/vile.*
%{_datadir}/X11/app-defaults/XVile
%{_datadir}/X11/app-defaults/UXVile
%{_datadir}/applications/xvile.desktop


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.8t-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9.8t-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 9.8t-2
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Dec 07 2018 Filipe Rosset <rosset.filipe@gmail.com> - 9.8t-1
- update to latest upstream 9.8t
- changelog http://invisible-island.net/vile/CHANGES.html#v9_8t

* Thu Sep 13 2018 Filipe Rosset <rosset.filipe@gmail.com> - 9.8s-1
- rebuilt to latest upstream 9.8s

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 9.8r-9
- Rebuild with fixed binutils

* Sat Jul 28 2018 Mark McKinstry <mmckinst@umich.edu> - 9.8r-8
- add BuildRequires for gcc (RHBZ#1606646)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9.8r-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Filipe Rosset <rosset.filipe@gmail.com> - 9.8r-6
- Remove obsolete scriptlets + spec modernization

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 9.8r-5
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.8r-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.8r-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9.8r-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Mark McKinstry <mmckinst@umich.edu> - 9.8r-1
- upgrade to 9.8r (RHBZ#1361436)

* Mon Feb 29 2016 Mark McKinstry <mmckinst@umich.edu> - 9.8q-3
- fix package summary (RHBZ#1311501)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9.8q-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Sep 23 2015 Mark McKinstry <mmckinst@umich.edu> - 9.8q-1
- upgrade to 9.8q (RHBZ#1260817)

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.8p-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Mar 15 2015 Mark McKinstry <mmckinst@nexcess.net> - 9.8p-1
- upgrade to 9.8p (RHBZ#1188844)

* Fri Oct 31 2014 Mark McKinstry <mmckinst@example.com> - 9.8o-1
- upgrade to 9.8o

* Fri Sep 12 2014 Mark McKinstry <mmckinst@example.com> - 9.8n-1
- upgrade to 9.8n

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.8m-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Mark McKinstry <mmckinst@example.com> - 9.8m-4
- re-add buildroot for el5

* Sun Jun 22 2014 Mark McKinstry <mmckinst@nexcess.net> - 9.8m-3
- don't strip executables during build (RHBZ#1106365)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9.8m-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 04 2014 Filipe Rosset <rosset.filipe@gmail.com> - 9.8m-1
- Rebuilt for new upstream release, spec cleanup, fixes rhbz #1060488

* Wed Sep 11 2013 Mark McKinstry <mmckinst@nexcess.net> - 9.8k-1
- upgrade to 9.8k (BZ#983023)

* Fri May 10 2013 Mark Mckinstry <mmckinst@nexcess.net> - 9.8j-1
- upgrade to 9.8j

* Sun Dec  2 2012 Mark McKinstry <mmckinst@nexcess.net> - 9.8i-1
- upgrade to 9.8i
- use better icons

* Wed May 11 2011 Mark McKinstry <mmckinst@nexcess.net> 9.8e-1
- upgrade to 9.8e
- fix dependency

* Sun Jan 30 2011 Mark McKinstry <mmckinst@nexcess.net> 9.8d-3
- symlink lxvile and uxvile to xvile manpage
- add emtpy vendor tag to desktop-file-install to make EPEL happy
- add some conditionals so it will build on EPEL 4

* Wed Jan 26 2011 Mark McKinstry <mmckinst@nexcess.net> 9.8d-2
- include xvile.desktop
- include verison for vile-common requirements
- replace icon with xpm version

* Sun Jan 23 2011 Mark McKinstry <mmckinst@nexcess.net> 9.8d-1
- upgrade to 9.8d
- create vile-common package

* Mon Nov 22 2010 Mark McKinstry <mmckinst@nexcess.net> 9.8b-1
- upgrade to 9.8b
- add xvile

* Mon Aug 16 2010 Mark McKinstry <mmckinst@nexcess.net> 9.8-1
- upgrade to 9.8
- include more documentation

* Sat May 8 2010 Mark McKinstry <mmckinst@nexcess.net> 9.7zc-1
- initial build
