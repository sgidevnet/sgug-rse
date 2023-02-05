# TODO: BR: perl(File::Spec::Link) when available

Name:		perl-Cwd-Guard
Version:	0.05
Release:	11%{?dist}
Summary:	Temporarily change the current directory
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Cwd-Guard
Source0:	https://cpan.metacpan.org/authors/id/K/KA/KAZEBURO/Cwd-Guard-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Copy)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(utf8)
# Module Runtime
BuildRequires:	perl(constant)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(if)
BuildRequires:	perl(parent)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Test::More) >= 0.88
BuildRequires:	perl(Test::Requires)
# Runtime
Requires:	perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description
Cwd::Guard can change the current directory (chdir) using a limited scope.

  use Cwd::Guard qw/cwd_guard/;
  use Cwd;
 
  my $dir = getcwd;
  MYBLOCK: {
    my $guard = cwd_guard('/tmp/xxxxx') or die
      "failed chdir: $Cwd::Guard::Error";
    ... # chdir to /tmp/xxxxx
  }
  ... # back to $dir

%prep
%setup -q -n Cwd-Guard-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Cwd/
%{_mandir}/man3/Cwd::Guard.3*

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-4
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.05-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.05-2
- Perl 5.24 rebuild

* Thu Apr 14 2016 Paul Howarth <paul@city-fan.org> - 0.05-1
- Update to 0.05
  - Add a new test

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-3
- Perl 5.22 rebuild

* Tue Oct  7 2014 Paul Howarth <paul@city-fan.org> - 0.04-2
- Sanitize for Fedora submission

* Sat Oct  4 2014 Paul Howarth <paul@city-fan.org> - 0.04-1
- Initial RPM version
