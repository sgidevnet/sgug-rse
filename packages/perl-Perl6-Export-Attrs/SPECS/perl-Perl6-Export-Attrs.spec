Name:           perl-Perl6-Export-Attrs
Summary:        Perl 6 'is export(...)' trait as a Perl 5 attribute
Version:        0.000006
Release:        8%{?dist}
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Perl6-Export-Attrs
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Perl6-Export-Attrs-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))

%{?perl_default_filter}

%description
Implements a Perl 5 native version of what the Perl 6 symbol export
mechanism will look like.


%prep
%setup -q -n Perl6-Export-Attrs-%{version}


%build
%{__perl} Build.PL installdirs=vendor
./Build


%install
./Build install destdir=%{buildroot} create_packlist=0

%{_fixperms} %{buildroot}/*


%check
./Build test


%files
%doc Changes README
%{perl_vendorlib}/Perl6
%{_mandir}/man3/Perl6::Export::Attrs.3pm*


%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.000006-8
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.000006-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000006-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.000006-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.000006-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000006-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.000006-2
- Perl 5.28 rebuild

* Sun Feb 18 2018 Emmanuel Seyman <emmanuel@seyman.fr> - 0.000006-1
- Update to 0.000006

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.000005-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000005-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.000005-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.000005-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.000005-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.000005-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 24 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.000005-1
- Update to 0.000005

* Sun Oct 18 2015 Emmanuel Seyman <emmanuel@seyman.fr> - 0.000004-1
- Update to 0.000004

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.3-8
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.0.3-7
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 0.0.3-4
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.3-2
- Add missing build requirements.

* Mon Jan 07 2013 Mathieu Bridon <bochecha@fedoraproject.org> - 0.0.3-1
- Initial package for Fedora, with help from cpanspec.
