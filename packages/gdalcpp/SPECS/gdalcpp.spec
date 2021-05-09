%global commit 4df5ca1fa44b2be1d58e166a5399f179eaf15caa
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global debug_package %{nil}

Name:           gdalcpp
Version:        1.2.0
Release:        3.20180829git%{shortcommit}%{?dist}
Summary:        C++11 wrapper classes for GDAL/OGR

License:        Boost
URL:            https://github.com/joto/gdalcpp
Source0:        https://github.com/joto/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz

%description
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
These are some small wrapper classes for GDAL offering:

* classes with RAII instead of the arcane cleanup functions in stock GDAL
* works with GDAL 1 and 2
* allows you to write less boilerplate code

The classes are not very complete, they just have the code I needed for
various programs.


%prep
%setup -q -n %{name}-%{commit}


%build


%install
mkdir -p %{buildroot}%{_includedir}
cp -p *.hpp  %{buildroot}%{_includedir}


%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/*.hpp


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2.20180829git4df5ca1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec  8 2018 Tom Hughes <tom@compton.nu> - 1.2.0-1.20180829git4df5ca1
- Update to 1.2.0 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-6.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4.20160601git225b97c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun  1 2016 Tom Hughes <tom@compton.nu> - 1.1.1-3.20160601git225b97c
- Update to upstream snapshot

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec  4 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Update to 1.1.1 upstream release

* Tue Dec  1 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Restore dist tag

* Mon Nov 23 2015 Tom Hughes <tom@compton.nu> - 1.1.0-1
- Update to 1.1.0 upstream release

* Tue Aug 25 2015 Tom Hughes <tom@compton.nu> - 0-0.1.20150825git75c0ac4
- Initial build
