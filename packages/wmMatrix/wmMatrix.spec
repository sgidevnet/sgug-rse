%global snapdate 20120814
%global treeish	97216606

Name:		wmMatrix
Version:	0.2
Release:	14.%{snapdate}git%{treeish}%{?dist}
Summary:	DockApp version of Jamie Zawinski's xmatrix screensaver hack

# The entire source code is GPLv2+ except for matrix.* and yarandom.* which is BSD
License:	GPLv2+ and BSD

# wmMatrix is long since abandoned by its' original author and now
# maintained by wmaker-dev@lists.windowmaker.org subscribers.
URL:		http://repo.or.cz/w/dockapps.git

# "snapshot" link from http://repo.or.cz/w/dockapps.git/tree/HEAD:/wmMatrix
# Tree-ish hash reduced to 8 chars, name and version parts are correctly
# parsed by gitweb.  However, you will get different results each time you
# try to download this file, because git-archive(1) stamps each file with
# current time.  This is how git-archive(1) works...
Source:		%{url}/snapshot/%{name}-%{version}-g%{treeish}.tar.gz

BuildRequires:  gcc
BuildRequires:	libXext-devel libXpm-devel

%description
wmMatrix displays The Matrix (from the film of the same name) in
a Window Maker dock application. Based on the xscreensaver module
created by Jamie Zawinski.

Although it works best with Window Maker, wmMatrix also works fine
with other window managers.

%prep
%setup -q -c

%build
cd dockapps
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
install -p -m755 dockapps/wmMatrix %{buildroot}%{_bindir}/wmMatrix
install -p -m644 dockapps/wmMatrix.1 %{buildroot}%{_mandir}/man1/wmMatrix.1

%files
%doc dockapps/COPYING dockapps/COPYING.BSD
%{_bindir}/wmMatrix
%{_mandir}/man1/wmMatrix.1*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-6.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2.20120814git97216606
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Aug 14 2012 Alexey I. Froloff <raorn@raorn.name> - 0.2-1.20120814git97216606
- Initial build for Fedora
