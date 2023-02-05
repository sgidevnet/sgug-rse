Name:           bcm43xx-fwcutter
Version:        006
Release:        22%{?dist}
Summary:        Firmware extraction tool for Broadcom wireless driver

License:        GPLv2+
URL:            http://bcm43xx.berlios.de/
Source0:        http://download.berlios.de/bcm43xx/%{name}-%{version}.tar.bz2
Source1:	README.Fedora

BuildRequires:  gcc
%description
This package contains the 'bcm43xx-fwcutter' tool which is used to
extract firmware for the Broadcom network devices, from the official
Windows, MacOS or Linux drivers.

See the README.Fedora file shipped in the package's documentation for
instructions on using this tool.

%prep
%setup -q
sed -i -e 's/-O2/$(RPM_OPT_FLAGS)/' Makefile


%build
make
cp %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 bcm43xx-fwcutter $RPM_BUILD_ROOT%{_bindir}/bcm43xx-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 bcm43xx-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1


%files
%{_bindir}/bcm43xx-fwcutter
%{_mandir}/man1/*
%doc README README.Fedora COPYING

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 006-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 006-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 006-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 006-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 006-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 006-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 006-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 006-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 006-4
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> 006-3
- Update licence

* Wed Aug 22 2007 David Woodhouse <dwmw2@infradead.org> 006-2
- Rebuild

* Thu Mar 22 2007 David Woodhouse <dwmw2@infradead.org> 006-1
- Update to 006
- Remove obsolete modprobe.bcm43xx

* Sat Oct 14 2006 David Woodhouse <dwmw2@infradead.org> 005-1
- Update to 005

* Mon Sep 11 2006 David Woodhouse <dwmw2@infradead.org> 004-2
- Rebuild

* Fri Mar 31 2006 David Woodhouse <dwmw2@infradead.org> 004-1
- Update to 004

* Thu Mar 23 2006 David Woodhouse <dwmw2@infradead.org> 003-2
- Package review. Use $RPM_OPT_FLAGS, ship man page, etc.
- Complete documentation, add sample bcm43xx.modprobe file

* Wed Mar 22 2006 David Woodhouse <dwmw2@infradead.org> 003-1
- Initial build.

