Name:           httptunnel
Version:        3.3
Release:        24%{?dist}
Summary:        Tunnels a data stream in HTTP requests

License:        GPLv2
URL:            http://www.nocrew.org/software/httptunnel.html
#use debian repackage tarball, it doesn't include non-free documentation files
Source0:        http://ftp.de.debian.org/debian/pool/main/h/httptunnel/httptunnel_%{version}+dfsg.orig.tar.gz
BuildRequires:  gcc

%description
HTTPTunnel creates a bidirectional virtual data stream tunnelled in
HTTP requests. The requests can be sent via a HTTP proxy if so desired.


%prep
%setup -q

recode()
{
        iconv -f "$2" -t utf-8 < "$1" > "${1}_"
        mv -f "${1}_" "$1"
}
recode AUTHORS iso-8859-15
recode ChangeLog iso-8859-15

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT




%files
%doc AUTHORS ChangeLog COPYING DISCLAIMER FAQ HACKING NEWS README TODO
%{_bindir}/*
%{_mandir}/man?/*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 3.3-23
- Add gcc BR

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.3-5
- Autorebuild for GCC 4.3

* Tue Dec 11 2007 Sindre Pedersen Bjørdal <foolish@guezz.net> 3.3-4
- move recode bits to %%prep
- Use debian tarball as upstream tarball, solves non-free docs issue
- add doc files
* Sun Nov 11 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.3-3
- Update License tag to GPLv2
- Make sure all files are encoded with UTF-8
* Wed Jun 06 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.3-2
- Fix incoherent version in changelog
* Mon May 07 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 3.3-1
- Initial build
