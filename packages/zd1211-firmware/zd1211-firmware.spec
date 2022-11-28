Name:		zd1211-firmware
Version:	1.5
Release:	5%{?dist}
Summary:	Firmware for wireless devices based on zd1211 chipset
License:	GPLv2
URL:		http://zd1211.wiki.sourceforge.net
Source0:	http://downloads.sourceforge.net/zd1211/zd1211-firmware-%{version}.tar.bz2
Patch0:		zd1211-firmware-1.4-build__from_headers.patch
BuildArch:	noarch

BuildRequires:  gcc

%description
This package contains the firmware required to work with the zd1211 chipset.


%prep
%setup -q -n %{name}
%patch0 -p1
sed -i 's/\r//' *.h

%build
make CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
make install FW_DIR=$RPM_BUILD_ROOT/lib/firmware/zd1211 


%files
%doc README
%license COPYING
%dir /lib/firmware/zd1211
/lib/firmware/zd1211/*


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.5-3
- Add missing cc

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 02 2018 John W. Linville <linville@redhat.com> - 1.5-1
- Update to 1.5
- Remove unused definition of snap

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.4-4
- Add dist tag

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Oct 12 2007 kwizart < kwizart at gmail.com > - 1.4-1
- Update to 1.4

* Tue Aug 14 2007 kwizart < kwizart at gmail.com > - 1.3-5
- Drop the dist tag
- Update URL
- Fix directory ownership

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.3-4
- Update to snap 2007-03-19 but still no changes from Dec 26 2006.
- Drop devel is not usefull
- Use patch for sudo and zd1211b install
- Fix description/summary

* Sun Feb 25 2007 kwizart < kwizart at gmail.com > - 1.3-3
- Update to the snapshot source zd1211rw_fw_2007-02-23
 Timestramp didn't changed from 26-12-2006 so don't think date
 will tell anything in that case. I Prefer to wait for release tarball
 to fix any number version is that necessary.
- Uses of $RPM_OPT_FLAGS in place of CFLAGS += -Wall

* Sun Feb 11 2007 kwizart < kwizart at gmail.com > - 1.3-2
- Bundle the original vendor driver used to generate the firmware.

* Sat Jan  6 2007 kwizart < kwizart at gmail.com > - 1.3-1
- Update to 1.3

* Wed Oct 11 2006 kwizart < kwizart at gmail.com > - 1.2-1_FC5
- inital release.
