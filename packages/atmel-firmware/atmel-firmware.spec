%define usb_version 0.1

Name:           atmel-firmware
Version:        1.3
Release:        21%{?dist}
Summary:        Firmware for Atmel at76c50x wireless network chips

License:        Redistributable, no modification permitted
URL:            http://at76c503a.berlios.de/
Source0:        http://www.thekelleys.org.uk/atmel/atmel-firmware-%{version}.tar.gz
Source1:        http://download.berlios.de/at76c503a/at76_usb-firmware-%{usb_version}.tar.gz
BuildArch:      noarch
    
Obsoletes:      at76_usb-firmware < %{usb_version}
Provides:       at76_usb-firmware = %{usb_version}

%description
The drivers for Atmel at76c50x wireless network chips in the Linux 2.6.x kernel 
but do not include the firmware.
This firmware needs to be loaded by the host on most cards using these chips.


%prep
%setup -q 
%setup -q -D -T -a 1 
install -pm 0644 at76_usb-firmware-%{usb_version}/COPYRIGHT COPYRIGHT-usb
install -pm 0644 at76_usb-firmware-%{usb_version}/README README-usb
for i in COPYING README COPYRIGHT-usb README-usb; do
install -pm 0644 ${i} ${i}.%{name}
rm  ${i}
ln -sf /lib/firmware/${i}.%{name} ${i}
done

%build
# Nothing to build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/lib/firmware

install -pm 0644 images/*.bin $RPM_BUILD_ROOT/lib/firmware
#install -m 0644 images.usb/* $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 at76_usb-firmware-%{usb_version}/*.bin $RPM_BUILD_ROOT/lib/firmware
install -pm 0644 *.%{name} $RPM_BUILD_ROOT/lib/firmware


%files
%doc COPYING README COPYRIGHT-usb README-usb VERSION
/lib/firmware/*


%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan  7 2010 John W. Linville <linville@redhat.com> - 1.3-7
- Add dist tag

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 15 2007 kwizart < kwizart at gmail.com > - 1.3-4
- Prevent timestamps changes.

* Thu Dec 13 2007 Ralf Corsépius <rc040203@freenet.de> - 1.3-3
- Don't ship docs in /lib/firmware (BZ 420921).
- Minor spec cleanups.
- Bump %%release to fix F7 -> F8 EVR breakage.

* Mon Aug 27 2007 kwizart < kwizart at gmail.com > - 1.3-2
- Drop the dist tag for firmware

* Mon Mar 19 2007 kwizart < kwizart at gmail.com > - 1.3-1
- Initial clean package
