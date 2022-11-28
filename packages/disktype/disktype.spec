Name:           disktype
Version:        9
Release:        29%{?dist}
Summary:        Detect the content format of a disk or disk image

License:        MIT
URL:            http://disktype.sourceforge.net/
Source0:        http://downloads.sourceforge.net/disktype/disktype-9.tar.gz

BuildRequires:  gcc

%description
The purpose of disktype is to detect the content format of a disk or disk
image. It knows about common file systems, partition tables, and boot codes.

%prep
%setup -q

%build
sed -i '/CFLAGS   =/d' Makefile
sed -i '/LDFLAGS  =/d' Makefile
make %{?_smp_mflags} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 755 disktype %{buildroot}%{_bindir}
install -p -m 644 disktype.1 %{buildroot}%{_mandir}/man1

%files
%doc HISTORY LICENSE TODO
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 9-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Richard Fearn <richardfearn@gmail.com> - 9-27
- Don't remove buildroot in %%install section

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Richard Fearn <richardfearn@gmail.com> - 9-25
- Add BuildRequires: gcc
  (see https://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 9-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 16 2017 Richard Fearn <richardfearn@gmail.com> - 9-23
- Remove unnecessary Group: tag, BuildRoot: tag, and %%clean section

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 9-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 9-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Richard Fearn <richardfearn@gmail.com> - 9-18
- Remove unnecessary %%defattr

* Wed Sep 23 2015 Richard Fearn <richardfearn@gmail.com> - 9-17
- Enable hardened build

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 9-12
- Drop libewf support

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Apr 02 2010 Richard Fearn <richardfearn@gmail.com> - 9-6
- Bump for rebuild against libewf 20100226

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May  1 2008 Richard Fearn <richardfearn@gmail.com> - 9-3
- update EWF patch so that it doesn't modify CFLAGS/LDFLAGS
- mention EWF in man page

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 9-2
- build using $(RPM_OPT_FLAGS)
- install man page with -p to preserve timestamp
- add patch to support EWF images

* Sat Mar  8 2008 Richard Fearn <richardfearn@gmail.com> - 9-1
- initial package for Fedora

