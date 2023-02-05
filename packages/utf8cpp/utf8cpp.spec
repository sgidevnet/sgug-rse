# This package only contains header files.
%global debug_package %{nil}

Name:       utf8cpp
Version:    2.3.4
Release:    13%{?dist}
Summary:    A simple, portable and lightweight library for handling UTF-8 encoded strings

License:    Boost
URL:        http://utfcpp.sourceforge.net/
Source0:    http://downloads.sourceforge.net/utfcpp/utf8_v2_3_4.zip
BuildArch:  noarch

%description
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package    devel
Summary:    Header files for %{name}
BuildArch:  noarch
Provides:   %{name}-static = %{version}-%{release}

%description devel
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.


%prep
%setup -q -c %{name}-%{version}


%build
# nothing to do


%install
mkdir -p %{buildroot}%{_includedir}
install -p -m0644 source/utf8.h %{buildroot}%{_includedir}/utf8.h
mkdir -p %{buildroot}%{_includedir}/utf8
for i in checked.h core.h unchecked.h; do
    install -p -m0644 source/utf8/${i} %{buildroot}%{_includedir}/utf8/${i}
done


%files devel
%doc doc/*
%{_includedir}/utf8.h
%dir %{_includedir}/utf8
%{_includedir}/utf8/checked.h
%{_includedir}/utf8/core.h
%{_includedir}/utf8/unchecked.h


%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-4
- fix docs macro

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-3
- drop base package

* Wed Apr 30 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-2
- add Provides: utf8cpp-static
- fix Source0 URL
- add missing BuildArch: noarch

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.3.4-1
- initial package
