Name:       pdd
Version:    1.4
Release:    2%{?dist}
Summary:    Tiny date, time diff calculator

License:    GPLv3+
URL:        https://github.com/jarun/pdd
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  make
Requires: python3-dateutil


%description
There are times you want to check how old you are (in years, months, days) or
how long you need to wait for the next flash sale... pdd (python3 date diff)
is a small cmdline utility to calculate date and time difference. If no
program arguments are specified it shows the current date, time and timezone.


%prep
%autosetup -p1 -n %{name}-%{version}
sed -i '1s/env //' pdd


%build
# Nothing to do


%install
%make_install PREFIX=%{_prefix}


%files
%doc CHANGELOG README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 15:02:29 CET 2019 Robert-André Mauchin <zebob.m@gmail.com>- 1.4-1
- Release 1.4 (#1696243)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3.1-1
- Release 1.3.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.3-1
- Release 1.3

* Sun May 20 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2-1
- Release 1.2

* Sat Feb 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.1-1
- First RPM release
