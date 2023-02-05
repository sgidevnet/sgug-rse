%global gitsnap 20140818gitdf0ddc3

Name:           bind-to-tinydns
Version:        0.4.3
Release:        25.%{gitsnap}%{?dist}
Summary:        Convert DNS zone files in BIND format to tinydns format

License:        BSD
URL:            http://www.erat.org/
Source0:        bind-to-tinydns-%{version}-%{gitsnap}.tar.bz2
Patch0:         bind-to-tinydns-0.4.3-cflags.patch

BuildRequires: gcc

%description
This is a program that parses zone files used by the BIND DNS server and
converts them to the native format of the tinydns component of Dan Bernstein's
djbdns DNS server.

%prep
%setup -q -n %{name}
%patch0 -p1


%build
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 755 bind-to-tinydns $RPM_BUILD_ROOT%{_bindir}/bind-to-tinydns


%files
%doc README COPYING
%{_bindir}/bind-to-tinydns


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-25.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-24.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-23.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.4.3-22.20140818gitdf0ddc3
- add gcc into buildrequires

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-21.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-20.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-19.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-18.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-17.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-16.20140818gitdf0ddc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Tim Jackson <rpm@timj.co.uk> - 0.4.3-15.20140818gitdf0ddc3
- Updated to latest upstream snapshot; fixes SRV record support

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-14.20140205git32dc9263
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-13.20140205git32dc9263
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Feb 05 2014 Tim Jackson <rpm@timj.co.uk>
- Updated to latest upstream snapshot; supports AAAA records
- License is now BSD

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 Tim Jackson <rpm@timj.co.uk> 0.4.3-4
- Compile stage now uses standard compiler flags

* Tue Jan 27 2009 Tim Jackson <rpm@timj.co.uk> 0.4.3-3
- Correct License tag to GPL+

* Tue Jan 27 2009 Tim Jackson <rpm@timj.co.uk> 0.4.3-2
- Add missing source URL

* Sat Sep 06 2008 Tim Jackson <rpm@timj.co.uk> 0.4.3-1
- Initial RPM build
