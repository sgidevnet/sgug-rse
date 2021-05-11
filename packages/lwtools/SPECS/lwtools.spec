Name:           lwtools
Version:        4.17
Release:        2%{?dist}
Summary:        Cross-development tool chain for Motorola 6809 and Hitachi 6309

License:        GPLv3
URL:            http://www.lwtools.ca/
Source0:        http://www.lwtools.ca/releases/lwtools/lwtools-%{version}.tar.gz

%description
LWTOOLS is a set of cross-development tools for the Motorola 6809 and
Hitachi 6309 microprocessors. It supports assembling to raw binaries,
CoCo LOADM binaries, and a proprietary object file format for later
linking. It also supports macros and file inclusion among other things.

%package doc
Summary:        Documentation for the LWTOOLS cross-development tool chain
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

BuildRequires:  gcc

%description doc
The complete documentation for the LWTOOLS cross-development tool chain.


%prep
%setup -q


%build
export LDFLAGS=${LDFLAGS:-%__global_ldflags}
make %{?_smp_mflags} CFLAGS="%{optflags}"


%install
make install INSTALLDIR=%{buildroot}%{_bindir}/

mkdir -p %{buildroot}%{_docdir}/%{name}
mv docs/*.txt %{buildroot}%{_docdir}/%{name}
mv docs/manual %{buildroot}%{_docdir}/%{name}
cp -a 00README.txt %{buildroot}%{_docdir}/%{name}


%files
%{_bindir}/*
%dir %{_docdir}/%{name}
%license COPYING GPL3

%files doc
%{_docdir}/%{name}/*.txt
%{_docdir}/%{name}/manual


%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 John W. Linville <linville@tuxdriver.com> 4.17-1
- Update for version 4.17 from upstream

* Mon Feb 11 2019 John W. Linville <linville@tuxdriver.com> 4.16-1
- Update for version 4.16 from upstream
- Update URLs

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 John W. Linville <linville@redhat.com> - 4.15-4
- Add previously unnecessary BuildRequires for gcc

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 John W. Linville <linville@tuxdriver.com> 4.15-1
- Update for version 4.15 from upstream

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 10 2017 John W. Linville <linville@tuxdriver.com> 4.14-1
- Update for version 4.14 from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Apr 18 2016 John W. Linville <linville@tuxdriver.com> 4.13-1
- Update for version 4.13 from upstream

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 4.12-1
- Update to 4.12 (#1270624)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 14 2015 John W. Linville <linville@tuxdriver.com> 4.11-1
- Update for version 4.11 from upstream

* Wed Feb  4 2015 John W. Linville <linville@tuxdriver.com> 4.10-3
- Use license macro for files containing license information

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 13 2014 John W. Linville <linville@tuxdriver.com> 4.10-1
- Initial import
