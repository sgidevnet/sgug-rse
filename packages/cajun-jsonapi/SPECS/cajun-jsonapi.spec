# cajun only ships headers, so no debuginfo package is needed
BuildArch:      noarch

Summary: A cross-platform C++ header library for JSON
Name: cajun-jsonapi
Version: 2.0.3
Release: 10%{?dist}
URL: https://github.com/cajun-jsonapi/cajun-jsonapi
Source0: https://github.com/cajun-jsonapi/cajun-jsonapi/archive/%{version}.tar.gz
License: BSD

BuildRequires:  gcc-c++
%description
CAJUN is a C++ API for the JSON data interchange format with an emphasis
on an intuitive, concise interface. The library provides JSON types
and operations that mimic standard C++ as closely as possible in concept
and design.

%package devel
Summary: Header files for cajun

%description devel
Header files you can use to develop applications with cajun.

CAJUN is a C++ API for the JSON data interchange format with an emphasis
on an intuitive, concise interface. The library provides JSON types
and operations that mimic standard C++ as closely as possible in concept
and design.

%prep
%setup -q

%build

%install
install -d -m755 $RPM_BUILD_ROOT/%{_includedir}/cajun/json
install -p -m644 json/* $RPM_BUILD_ROOT/%{_includedir}/cajun/json

%check
make %{?_smp_mflags}

%files devel
%doc Readme.txt ReleaseNotes.txt
%dir %{_includedir}/cajun
%dir %{_includedir}/cajun/json
%{_includedir}/cajun/json/*

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Sep 26 2013 Daniel Pocock <daniel@pocock.com.au> - 2.0.3-1
- Initial spec file
