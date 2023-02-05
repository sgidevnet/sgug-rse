Name:           stbi
%global soname  lib%{name}
%global srcname stb_image
Version:        1.33
Release:        13%{?dist}
Summary:        JPEG/PNG reader
License:        Public Domain
URL:            http://nothings.org/%{srcname}.c
Source0:        %{url}
BuildRequires:  gcc
BuildRequires:  dos2unix

%description
Public Domain JPEG/PNG reader. Primarily of interest to game developers and
other people who can avoid problematic images and only need the trivial
interface.

%package devel
Summary: JPEG/PNG reader development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -Tc
head -62 %{SOURCE0} > README
head -184 %{SOURCE0} | tail -112 >> README
 
head -65 %{SOURCE0} | tail -2 > %{srcname}.h
head -332 %{SOURCE0} | tail -146 >> %{srcname}.h

echo '#include "stb_image.h"' > %{srcname}.c
head -4586 %{SOURCE0} | tail -4254 >> %{srcname}.c

tail -86 %{SOURCE0} > CHANGES

dos2unix *

%build
gcc -O2 -g -pipe -Wall -I. -fPIC -c %{srcname}.c
gcc -O2 -g -pipe -Wall -I. -shared -Wl,-soname,%{soname}.so.1 %{srcname}.o -o %{soname}.so.1.0.0


%install
install -Dpm0755 %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1.0.0
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so.1
ln -s %{soname}.so.1.0.0 %{buildroot}%{_libdir}/%{soname}.so
install -Dpm0644 %{srcname}.h %{buildroot}%{_includedir}/%{srcname}.h


%files
%doc README CHANGES
%{_libdir}/%{soname}.so.*

%files devel
%{_libdir}/%{soname}.so
%{_includedir}/*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 02 2013 Miro Hrončok <mhroncok@redhat.com> - 1.33-1
- Started

