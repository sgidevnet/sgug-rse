Name:           logserial
Version:        0.4.2 
Release:        25%{?dist}
Summary:        Package for logging incoming bytes on asynchronous serial ports

License:        GPL+
URL:            http://www.ibiblio.org/pub/Linux/system/serial/logserial-0.4.2.lsm
Source0:        http://www.ibiblio.org/pub/Linux/system/serial/logserial-0.4.2.tar.gz
Patch0:         logserial-makefile.patch

BuildRequires:  gcc
%description
Package for logging incoming bytes on asynchronous serial ports.
It was written for loging calls on our telephone central, but
you can use it for any devices connected to serial ports. From
version 0.4 it can be used to send data through serial line.

%prep
%setup -q
%patch0 -p0


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -p -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}



%files
%doc CHANGELOG README
%{_bindir}/%{name}




%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-7
- modify the patch to make rpmbuild even happier, fuzz must be 0

* Sat Aug 02 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-6
- make rpmbuild happy, it now has a stricter syntax checking

* Sat Feb 09 2008 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-5.2.1
- previous entry had wrong date

* Wed Aug 22 2007 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-5.2
- rebuilt for gcc-4.3.0

* Wed Aug 22 2007 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-5.1
- rebuilt

* Mon Aug 06 2007 Manuel Wolfshant <wolfy@fedoraproject.org> 0.4.2-5
- License clarification

* Tue Nov 14 2006 lonely wolf <wolfy@pcnet.ro> 0.4.2-4
- remove some debugging lines from the spec. No effect on generated binaries

* Mon Nov 13 2006 lonely wolf <wolfy@pcnet.ro> 0.4.2-3
- corrected the patch to make use of $RPM_OPT_FLAGS

* Sun Nov 12 2006 lonely wolf <wolfy@pcnet.ro> 0.4.2-2
- Modify the Makefile to make use of $RPM_OPT_FLAGS

* Mon Nov 07 2006 lonely wolf <wolfy@pcnet.ro> 0.4.2-1
- Initial Fedora package
