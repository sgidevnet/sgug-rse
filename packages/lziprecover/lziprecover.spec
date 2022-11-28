Name:           lziprecover
Version:        1.20
Release:        5%{?dist}
Summary:        Data recovery tool and decompressor for files in the lzip compressed format

License:        GPLv3+
URL:            http://www.nongnu.org/lzip/lziprecover.html
Source0:        http://download.savannah.gnu.org/releases/lzip/lziprecover/lziprecover-%{version}.tar.lz
Source1:        http://download.savannah.gnu.org/releases/lzip/lziprecover/lziprecover-%{version}.tar.lz.sig
BuildRequires:  lzip gcc-c++

%description
Lziprecover is a data recovery tool and decompressor for files in the lzip 
compressed data format (.lz) able to repair slightly damaged files, recover 
badly damaged files from two or more copies, extract undamaged members 
from multi-member files, decompress files and test integrity of files.

Lziprecover is able to recover or decompress files produced by any of the 
compressors in the lzip family; lzip, plzip, minilzip/lzlib, clzip and 
pdlzip. This recovery capability contributes to make the lzip format one 
of the best options for long-term data archiving. 


%prep
%setup -q
# file needs to be copied, because it is used in "make check"
cp -a COPYING{,.txt}
# convert CRLF to LF
sed -i 's/\r//' COPYING.txt 


%build
%configure CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}


%install
make install install-man DESTDIR=$RPM_BUILD_ROOT

# if install-info is present, this is created by upstream's makefile
rm -Rf $RPM_BUILD_ROOT%{_infodir}/dir


%check
make check

%files
# TODO is currently empty
%license COPYING.txt
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/lziprecover
%{_infodir}/lziprecover.info*
%{_mandir}/man1/lziprecover.1*


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 01 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.20-3
- BR fix.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 12 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.20-1
- 1.20

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Apr 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 1.19-1
- 1.19, BZ 1442896.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 19 2016 Jon Ciesla <limburgher@gmail.com> - 1.18-1
- 1.18, BZ 1337729.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 09 2015 Jon Ciesla <limburgher@gmail.com> - 1.17-1
- 1.17, BZ 1228902.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.15-4
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Jon Ciesla <limburgher@gmail.com> - 1.15-1
- 1.15, BZ 1010894.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 10 2013 Jon Ciesla <limburgher@gmail.com> - 1.14-1
- 1.14, BZ 972489.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Jon Ciesla <limburgher@gmail.com> - 1.13-1
- Initial spec for Fedora
