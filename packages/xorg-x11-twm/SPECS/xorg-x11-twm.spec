Summary:    X.Org X11 twm window manager
Name:       xorg-x11-twm
# NOTE: Remove Epoch line if package gets renamed to something like "twm"
Epoch:      1
Version:    1.0.9
Release:    10%{?dist}
License:    MIT
URL:        http://www.x.org

Source0:    ftp://ftp.x.org/pub/individual/app/twm-%{version}.tar.bz2

BuildRequires:  bison
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xproto) >= 7.0.17
BuildRequires:  pkgconfig(xt)

Requires:       xterm
Provides:       twm = %{epoch}:%{version}

%description
X.Org X11 Tab Window Manager.

%prep
%setup -q -n twm-%{version}

%build
autoreconf -v --install
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# FIXME: Upstream sources do not create the system wide twm config dir, nor
# install the default config file currently.  We'll work around it here for now.
{
   echo "FIXME: Upstream doesn't install systemwide config by default"
   mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/twm
   install -p -m 0644 src/system.twmrc $RPM_BUILD_ROOT%{_sysconfdir}/X11/twm/
   rm -fr $RPM_BUILD_ROOT%{_datadir}/X11
}

%files
%doc COPYING ChangeLog
%{_bindir}/twm
%{_mandir}/man1/twm.1*
%dir %{_sysconfdir}/X11/twm
%config %{_sysconfdir}/X11/twm/system.twmrc

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 22 2015 Hans de Goede <hdegoede@redhat.com> 1:1.0.9-1
- twm 1.0.9 (rhbz#1006028)

* Thu Oct 23 2014 Simone Caronni <negativo17@gmail.com> - 1:1.0.8-2
- Clean up SPEC file, fix rpmlint warnings.
- Configuration file installed by upstream scripts.
- Rework build requirements.

* Wed Oct 01 2014 Adam Jackson <ajax@redhat.com> 1:1.0.8-1
- twm 1.0.8

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Sep 17 2011 Matěj Cepl <mcepl@redhat.com> - 1:1.0.7-1
- New upstream release.

* Sat Jul 16 2011 Matěj Cepl <mcepl@redhat.com> - 1:1.0.6-1
- New upstream release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
