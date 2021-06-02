Name:		perl-Carp-Fix-1_25
Version:	1.000001
Release:	19%{?dist}
Summary:	Smooth over incompatible changes in Carp 1.25
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Carp-Fix-1_25
Source0:	http://cpan.metacpan.org/authors/id/M/MS/MSCHWERN/Carp-Fix-1_25-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(Module::Build)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::More) >= 0.88
# Dependencies
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Carp 1.25 made a change to its formatting, adding a period at the end of the
message. This can mess up tests and code that are looking for error messages.
Carp::Fix::1_25 makes the message consistent, regardless of what version of
Carp you're using.

Carp::Fix::1_25 exports its own carp functions, which change the Carp message
to match the 1.25 version. Carp::Fix::1_25 otherwise acts exactly like Carp and
it will honor Carp global variables such as @CARP_NOT and %%Carp::Internal.

Why do this instead of just upgrading Carp? Upgrading Carp would affect all
installed code all at once. You might not be ready for that, or you might not
want your module to foist that on its users. This lets you fix things one
namespace at a time.

%prep
%setup -q -n Carp-Fix-1_25-%{version}

# Unbundle Test-Simple and use the system one (#998410)
rm -rf t/lib/Test
sed -i -e '/^t\/lib\/Test\//d' MANIFEST

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} %{buildroot}

%check
./Build test

%files
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendorlib}/Carp/
%{_mandir}/man3/Carp::Fix::1_25.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-18
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-15
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-12
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Aug  8 2016 Paul Howarth <paul@city-fan.org> - 1.000001-10
- Classify buildreqs by usage
- Use %%license where possible

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-9
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.000001-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000001-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-6
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.000001-5
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.000001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 22 2013 Paul Howarth <paul@city-fan.org> - 1.000001-3
- Unbundle Test-Simple and use the system one (#998410)
- Since we now require Test::More ≥ 0.88, drop EPEL-5 compatibility

* Mon Aug 19 2013 Paul Howarth <paul@city-fan.org> - 1.000001-2
- Sanitize for Fedora submission

* Thu Aug 15 2013 Paul Howarth <paul@city-fan.org> - 1.000001-1
- Initial RPM version
