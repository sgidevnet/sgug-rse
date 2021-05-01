# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}

Summary: A lightweight multi-tabbed terminal emulator for X
Name: mrxvt
Version: 0.5.4
Release: 28%{?dist}
URL: http://materm.sourceforge.net/wiki/Main/HomePage
License: GPLv2+
BuildRequires:  gcc
#BuildRequires: imake pkgconfig ncurses-devel libXft-devel libXaw-devel libXext-devel desktop-file-utils
BuildRequires: pkgconfig ncurses-devel libXft-devel libXaw-devel libXext-devel desktop-file-utils
#BuildRequires: libpng-devel libjpeg-devel libutempter-devel
BuildRequires: libpng-devel libjpeg-devel

Source0: http://downloads.sourceforge.net/materm/%{name}-%{version}.tar.gz
Source1: http://littlehat.homelinux.org:8000/FEDORA/mrxvt/current/0.5.3/%{name}.desktop

#Patch1: http://downloads.sourceforge.net/materm/no-scroll-with-buffer-mrxvt-0.5.3.patch
Patch2: mrxvt.sgifixes.patch

%description
Mrxvt (previously materm) is based on 2.7.11 CVS of rxvt and aterm.

%prep

%setup -q
#%patch1 -p0 -b .no-scroll-with-buffer-mrxvt-0.5.3
%patch2 -p1
sed -i 's|\r||' share/scripts/mrxvt.vbs

%build

#configure \
#           --enable-everything \
#           --disable-debug
# mrxvt & the config cache aren't happy together
unset CONFIG_SITE
%configure \
           --enable-sgi-scroll \
           --with-tab-radius=0

make %{?_smp_mflags}

%install

rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT INSTALL="%{__install} -p" install 

desktop-file-install \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        %{SOURCE1}

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc

%files 
%doc doc/README* doc/*.txt*
%doc share/scripts/
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/mrxvt
%{_mandir}/man1/mrxvt.1*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/mrxvt/default.menu
%config(noreplace) %{_sysconfdir}/mrxvt/mrxvtrc
%config(noreplace) %{_sysconfdir}/mrxvt/mrxvtrc.sample
%config(noreplace) %{_sysconfdir}/mrxvt/submenus.menu
%{_datadir}/applications/mrxvt.desktop
%{_datadir}/pixmaps/%{name}*

%changelog
* Fri Dec 18 2020 Daniel Hams <daniel.hams@gmail.com> - 0.5.4-28
- Include desktop file

* Tue Oct 27 2020 Daniel Hams <daniel.hams@gmail.com> - 0.5.4-27
- Rebuild for jpegturbo

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.5.4-26
- Remove hard coded shell paths, avoid use of config.cache

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
