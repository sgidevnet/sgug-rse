Name:           sigrok-firmware
Version:        0.1.0
%global         checkout 20151211gitb2daf81
Release:        14.%{checkout}%{?dist}
Summary:        Firmware for some hardware supported by sigrok
License:        GPLv2 and Redistributable, no modification permitted
URL:            http://www.sigrok.org/
# $ git clone git://sigrok.org/sigrok-firmware
# $ cd sigrok-firmware
# $ git checkout b2daf81ca2e892b5b80ce4bc35ff5a846853b50b
# $ sh autogen.sh
# $ mkdir build
# $ cd build
# $ ../configure
# $ make dist
# $ mv %%{name}-%%{version}.tar.gz %%{name}-%%{version}-%%{checkout}.tar.gz
Source0:        %{name}-%{version}-%{checkout}.tar.gz
BuildArch:      noarch

%description
%{name} is a collection of firmware files required for some of the
devices libsigrok supports (logic analyzers, oscilloscopes, or others).

%{name} only contains firmware files which have an explicit
permission/license that allows at _least_ redistribution of the firmware.

%package        nonfree
Summary:        Components of %{name} with non-free licenses
License:        Redistributable, no modification permitted
Requires:       %{name}-filesystem = %{version}-%{release}

%description    nonfree
The %{name}-nonfree package contains firmwares available under non-free
licenses which permit redistribution.

%package        filesystem
Summary:        Directory structure for %{name}

%description    filesystem
This package provides directories required by packages containing sigrok
binary firmware.


%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files filesystem
%doc README NEWS COPYING
%dir %{_datadir}/%{name}

%files nonfree
%doc asix-sigma/LICENSE.Sigma
%{_datadir}/%{name}/asix-sigma-*.fw
%doc sysclk-lwla/LICENSE.LWLA
%{_datadir}/%{name}/sysclk-lwla1016-*.rbf
%{_datadir}/%{name}/sysclk-lwla1034-*.rbf

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-9.20151211gitb2daf81
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Feb 06 2016 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-8.20151211gitb2daf81
- Update to newer upstream revision to pull in sysclk-lwla firmware.
- Drop "free" subpackage, as nexus osciprime files have been removed upstream

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-7.20130426git83e0802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6.20130426git83e0802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5.20130426git83e0802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-4.20130426git83e0802
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 06 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-3.20130426git83e0802
- Cap remaining description lines at 80 characters
- Version the dependency on sigrok-firmware-filesystem

* Mon May 06 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-2.20130426git83e0802
- Don't use macros in comments
- Cap description lines at 80 characters
- Use proper license descriptors.
- Add OsciPrime sources in the SRPM

* Sun May 05 2013 Alexandru Gagniuc <mr.nuke.me@gmail.com> - 0.1.0-1
- Initial RPM release