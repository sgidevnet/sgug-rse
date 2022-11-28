Name:           unibilium
Version:        2.0.0
Release:        5%{?dist}
Summary:        Terminfo parsing library

License:        LGPLv3+
URL:            https://github.com/mauke/unibilium

Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         0001-Relax-checks-for-extended-capability-to-support-new-.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
# For docs
BuildRequires:  %{_bindir}/pod2man
# For tests
BuildRequires:  %{_bindir}/prove

%description
Unibilium is a very basic terminfo library. It doesn't depend on curses or any
other library. It also doesn't use global variables, so it should be
thread-safe.

%package devel
Summary:        Development files needed for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%autosetup -p1
echo '#!/bin/sh' > ./configure
chmod +x ./configure

%build
%configure
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir}

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%check
make test

%ldconfig_scriptlets

%files
%license LGPLv3
%doc Changes
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_mandir}/man3/unibi_*.3*
%{_mandir}/man3/%{name}.h.3*

%changelog
* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 14 2018 Andreas Schneider <asn@redhat.com> - 2.0.0-3
- Add support for parsing new terminfo format

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 25 2018 Andreas Schneider <asn@redhat.com> - 2.0.0-1
- Update to version 2.0.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-2
- Switch to %%ldconfig_scriptlets

* Sat Sep 09 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.2.0-1
- Initial package
