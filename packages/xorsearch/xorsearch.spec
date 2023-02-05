Name:           xorsearch
Version:        1.11.2
Release:        1%{?dist}
Summary:        Search for a given string in an XOR, ROL, ROT or SHIFT encoded binary file

License:        Public Domain
URL:            http://blog.didierstevens.com/programs/xorsearch/

%global pkgver %(echo %{version} | sed 's/\\./_/g')
Source0:        http://didierstevens.com/files/software/XORSearch_V%{pkgver}.zip
Patch0:         %{name}-cosmetics.patch

BuildRequires:  gcc

%description
XORSearch is a program to search for a given string in an XOR, ROL, ROT or SHIFT
encoded binary file. An XOR encoded binary file is a file where some (or all)
bytes have been XORed with a constant value (the key). A ROL (or ROR) encoded
file has its bytes rotated by a certain number of bits (the key). A ROT encoded
file has its alphabetic characters (A-Z and a-z) rotated by a certain number
of positions. A SHIFT encoded file has its bytes shifted left by a certain
number of bits (the key): all bits of the first byte shift left, the MSB
of the second byte becomes the LSB of the first byte, all bits of the second
byte shift left, … XOR and ROL/ROR encoding is used by malware programmers
to obfuscate strings like URLs.


%prep
%setup -q -c
%patch0 -p 1 -b .cosmetics
#remove binaries
rm -rf OSX Linux XORSearch.exe

%build
# gcc %{optflags} -Wno-trigraphs XORSearch.c -o %{name}
gcc %{optflags} -Wno-trigraphs -D __APPLE__=1 XORSearch.c -o %{name}


%install
#Targetting EPEL as well
rm -rf "%{buildroot}"
install -m 755 -D %{name} "%{buildroot}/%{_bindir}/%{name}"


%files
%{_bindir}/%{name}

%changelog
* Mon Aug 12 2019 Michal Ambroz <rebus at, seznam.cz> 1.11.2-1
- bump to 1.11.2
- patch the off_t -> size_t, string formatting of size_t, using the fread return code

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug 01 2016 Michal Ambroz <rebus at, seznam.cz> 1.11.1-3
- fix EPEL5 build

* Mon Aug 01 2016 Michal Ambroz <rebus at, seznam.cz> 1.11.1-2
- changes based on package review by  Filip Szymański

* Mon Apr 25 2016 Michal Ambroz <rebus at, seznam.cz> 1.11.1-1
- bump version

* Sat Feb 16 2013 Michal Ambroz <rebus at, seznam.cz> 1.0-1
- initial build for Fedora
