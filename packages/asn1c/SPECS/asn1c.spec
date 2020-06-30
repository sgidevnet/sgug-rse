Name:           asn1c
Version:        0.9.28
Release:        9%{?dist}
Summary:        An ASN.1 Compiler

License:        BSD
URL:            http://lionet.info/asn1c
Source0:        http://lionet.info/soft/%{name}-%{version}.tar.gz

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  perl-interpreter

%description
Compiles ASN.1 data structures into C source structures that can be
simply marshalled to/unmarshalled from: BER, DER, CER, BASIC-XER,
CXER, EXTENDED-XER, PER.

%prep
%autosetup -S git

%build
%configure --docdir=%{_pkgdocdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc %{_pkgdocdir}
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Robbie Harwood <rharwood@redhat.com> - 0.9.28-5
- Add gcc and git to build-deps

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Nathaniel McCallum <npmccallum@redhat.com> - 0.9.28-1
- New upstream release
- Minor spec fixes for new release

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 0.9.27-5
- Add BR: perl (Fix F26FTBFS).
- Introduce %%license.
- Rework doc handling.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Apr 07 2015 Nathaniel McCallum <npmccallum@redhat.com> - 0.9.27-1
- New upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Dec 10 2011 Nathaniel McCallum <npmccallum@redhat.com> - 0.9.21-2
- Removed duplicate docs directory

* Fri Oct 28 2011 Nathaniel McCallum <npmccallum@redhat.com> - 0.9.21-1
- Initial package
