Name:          xdesktopwaves
Version:       1.4
Release:       2%{?dist}

Summary:       Simulation of water waves on the X Window System desktop
License:       GPLv2+
URL:           http://xdesktopwaves.sf.net/
Source:        https://downloads.sourceforge.net/project/xdesktopwaves/xdesktopwaves/xdesktopwaves-%{version}.tar.gz
BuildRequires: libX11-devel, desktop-file-utils, libXext-devel
BuildRequires: gcc

%description
xdesktopwaves is a cellular automata setting the background of your X
Window System desktop under water. Windows and mouse are like ships on
the sea. Each movement of these ends up in moving water waves. You can
even have rain and/or storm stirring up the water.

%prep
%setup -q
%{__sed} -i -e "s,-s,," Makefile

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LFLAGS="-L/usr/%{_lib}" %{?_smp_mflags}

%install
%{__mkdir_p} $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
%{__mkdir_p} $RPM_BUILD_ROOT{%{_datadir}/applications,%{_datadir}/pixmaps}
%{__make} install BINDIR=$RPM_BUILD_ROOT%{_bindir} MAN1DIR=$RPM_BUILD_ROOT%{_mandir}/man1
%{__cp} -p %{name}.xpm $RPM_BUILD_ROOT%{_datadir}/pixmaps

cat > %{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=xdesktopwaves
Type=Application
Comment=Simulation of water waves on the X Window System desktop
Exec=xdesktopwaves
Icon=xdesktopwaves.xpm
Terminal=false
EOF

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications           \
  --add-category X-Fedora                              \
  --add-category Application                           \
  --add-category Graphics                              \
  %{name}.desktop


%files
%doc COPYING README
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Adrian Reber <adrian@lisas.de> -1.4-1
- Updated to 1.4

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 18 2018 Adrian Reber <adrian@lisas.de> -1.3-27
- Added BR: gcc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Feb 10 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.3-16
- Remove vendor tag from desktop file as per https://fedorahosted.org/fesco/ticket/1077
- Cleanup spec as per recently changed packaging guidelines

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3-10
- Autorebuild for GCC 4.3

* Thu Oct 11 2007 Adrian Reber <adrian@lisas.de> - 1.3-9
- rebuilt for BuildID
- updated license tag
- fixed sourceforge URL

* Wed Apr 19 2006 Adrian Reber <adrian@lisas.de> - 1.3-8
- rebuilt

* Wed Apr 19 2006 Adrian Reber <adrian@lisas.de> - 1.3-7
- fixed BR

* Tue Apr 11 2006 Adrian Reber <adrian@lisas.de> - 1.3-6
- trying to fix build on x86_64

* Tue Apr 11 2006 Adrian Reber <adrian@lisas.de> - 1.3-5
- rebuilt for modular X

* Tue May 10 2005 Adrian Reber <adrian@lisas.de> - 1.3-4
- remove stripping from Makefile so that the
  debuginfo subpackage gets build

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Feb 14 2005 Adrian Reber <adrian@lisas.de> - 1.3-1
- updated to 1.3

* Wed Jan  5 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.2-1
- Make with proper LFLAGS to support /usr/X11R6/lib64 location
  (fix confirmed as necessary via Matthias Saou's package).

* Tue Dec 07 2004 Adrian Reber <adrian@lisas.de> - 0:1.2-0.fdr.1
- updated to 1.2

* Mon Nov 22 2004 Adrian Reber <adrian@lisas.de> - 0:1.0-0.fdr.1
- initial package
