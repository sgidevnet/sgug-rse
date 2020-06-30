Summary:        Converter between the rpm, dpkg, stampede slp, and Slackware tgz file formats
Name:           alien
Version:        8.95
Release:        13%{?dist}

License:        GPLv2+
URL:            https://sourceforge.net/projects/alien-pkg-convert/
Source:         http://downloads.sourceforge.net/alien-pkg-convert/%{name}_%{version}.tar.xz

Requires:       dpkg, debhelper, rpm-build
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

BuildArch:      noarch



%description
Alien is a program that converts between the rpm, dpkg, stampede 
slp, and Slackware tgz file formats. If you want to use a package 
from another distribution than the one you have installed on your 
system, you can use alien to convert it to your preferred package 
format and install it.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor VARPREFIX=%{buildroot}

make

%install
make pure_install DESTDIR=%{buildroot} \
        VARPREFIX=%{buildroot} \
        PREFIX=%{buildroot}%{_prefix}

%{__rm} -rf %{buildroot}%{perl_vendorarch}/auto/Alien

chmod 755 %{buildroot}%{_bindir}/alien

%files
%license GPL
%doc README debian/changelog
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man?/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 8.95-13
- Perl 5.32 rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 8.95-10
- Perl 5.30 rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 8.95-7
- Perl 5.28 rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 8.95-4
- Perl 5.26 rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Dmitrij S. Kryzhevich <krege@land.ru> - 8.95-2
- Update URL and Source tags.

* Wed Aug 03 2016 Dmitrij S. Kryzhevich <krege@land.ru> - 8.95-1
- Update to 8.95.

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 8.90-7
- Perl 5.24 rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.90-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.90-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 8.90-4
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 8.90-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 03 2014 Dmitrij S. Kryzhevich <krege@land.ru> - 8.90-1
- Update 8.90.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.88-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 8.88-3
- Perl 5.18 rebuild

* Wed May 22 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 8.88-2
- No need for "defattr" in files section.

* Tue May 21 2013 Dmitrij S. Kryzhevich <krege@land.ru> - 8.88-1
- Update to 8.88.

* Tue Nov 23 2010 Dmitrij S. Kryzhevich <krege@land.ru> - 8.83-1
- First try.
