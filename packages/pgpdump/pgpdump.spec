Name:           pgpdump
Version:        0.33
Release:        5%{?dist}
Summary:        PGP packet visualizer
License:        MIT
URL:            http://www.mew.org/~kazu/proj/pgpdump/
Source0:        http://www.mew.org/~kazu/proj/pgpdump/%{name}-%{version}.tar.gz
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc

%description
pgpdump is a PGP packet visualizer which displays the packet format of
OpenPGP (RFC 4880) and PGP version 2 (RFC 1991).

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc CHANGES README.md
%license COPYRIGHT
%{_bindir}/pgpdump
%{_mandir}/man1/pgpdump.1*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Nick Bebout <nb@fedoraproject.org> - 0.33-3
- Rebuild to fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 9 2018 Nick Bebout <nb@fedoraproject.org> - 0.33-1
- Update to 0.33

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 10 2017 Nick Bebout <nb@fedoraproject.org> - 0.32-1
- Update to 0.32

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon May 09 2016 Nick Bebout <nb@fedoraproject.org> - 0.31-1
- Update to 0.31 - fix buffer overflow

* Wed Apr 27 2016 Nick Bebout <nb@fedoraproject.org> - 0.30-1
- Update to 0.30

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 01 2014 Christopher Meng <rpm@cicku.me> - 0.29-1
- Update to 0.29

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 09 2013 Christopher Meng <rpm@cicku.me> - 0.28-1
- Initial Package.
