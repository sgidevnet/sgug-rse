# Inhibit python compilation
%global __python %{nil}

Name:           perl-v6
Version:        0.047
Release:        12%{?dist}
Summary:        Perl 6 implementation
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/v6
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/v6-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Encode)
BuildRequires:  perl(Filter::Util::Call)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(utf8)
# YAML::Syck not used at tests
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
Requires:       perl(YAML::Syck)
Provides:       perl(Perlito6::AST) = %{version}
Provides:       perl(Perlito6::Emitter::Token) = %{version}
Provides:       perl(Perlito6::Grammar::Control) = %{version}
Provides:       perl(Perlito6::Go::Emitter) = %{version}
Provides:       perl(Perlito6::Java::Emitter) = %{version}
Provides:       perl(Perlito6::JavaScript::Emitter) = %{version}
Provides:       perl(Perlito6::Lisp::Emitter) = %{version}
Provides:       perl(Perlito6::Macro) = %{version}
Provides:       perl(Perlito6::Parrot::Emitter) = %{version}
Provides:       perl(Perlito6::Perl5::Emitter) = %{version}
Provides:       perl(Perlito6::Perl5::Prelude) = %{version}
Provides:       perl(Perlito6::Perl5::Runtime) = %{version}
Provides:       perl(Perlito6::Python::Emitter) = %{version}
Provides:       perl(Perlito6::Ruby::Emitter) = %{version}
Provides:       perl(Perlito6::Runtime) = %{version}

# Do not export private modules
%global __provides_exclude %{!?__provides_exclude:^$}
%global __provides_exclude %__provides_exclude|^perl\\(Apply\\)
%global __provides_exclude %__provides_exclude|^perl\\(ARRAY\\)
%global __provides_exclude %__provides_exclude|^perl\\(Bind\\)
%global __provides_exclude %__provides_exclude|^perl\\(Call\\)
%global __provides_exclude %__provides_exclude|^perl\\(CompUnit\\)
%global __provides_exclude %__provides_exclude|^perl\\(Decl\\)
%global __provides_exclude %__provides_exclude|^perl\\(Do\\)
%global __provides_exclude %__provides_exclude|^perl\\(For\\)
%global __provides_exclude %__provides_exclude|^perl\\(GLOBAL\\)
%global __provides_exclude %__provides_exclude|^perl\\(HASH\\)
%global __provides_exclude %__provides_exclude|^perl\\(If\\)
%global __provides_exclude %__provides_exclude|^perl\\(Index\\)
%global __provides_exclude %__provides_exclude|^perl\\(IO\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Array\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Block\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lit::Hash\\)
%global __provides_exclude %__provides_exclude|^perl\\(Lookup\\)
%global __provides_exclude %__provides_exclude|^perl\\(Main\\)
%global __provides_exclude %__provides_exclude|^perl\\(Method\\)
%global __provides_exclude %__provides_exclude|^perl\\(Pair\\)
%global __provides_exclude %__provides_exclude|^perl\\(Perl5\\)
%global __provides_exclude %__provides_exclude|^perl\\(Proto\\)
%global __provides_exclude %__provides_exclude|^perl\\(Python\\)
%global __provides_exclude %__provides_exclude|^perl\\(Return\\)
%global __provides_exclude %__provides_exclude|^perl\\(Ruby\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::After\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Before\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Block\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Capture\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::CaptureResult\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::CharClass\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Concat\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Constant\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Dot\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::InterpolateVar\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NamedCapture\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NegateCharClass\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::NotBefore\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Or\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Quantifier\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::SpecialChar\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Subrule\\)
%global __provides_exclude %__provides_exclude|^perl\\(Rul::Var\\)
%global __provides_exclude %__provides_exclude|^perl\\(Sig\\)
%global __provides_exclude %__provides_exclude|^perl\\(Sub\\)
%global __provides_exclude %__provides_exclude|^perl\\(Use\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Bit\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Buf\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Int\\)
%global __provides_exclude %__provides_exclude|^perl\\(Val::Num\\)
%global __provides_exclude %__provides_exclude|^perl\\(Var\\)
%global __provides_exclude %__provides_exclude|^perl\\(When\\)
%global __provides_exclude %__provides_exclude|^perl\\(While\\)

# Do not generate requires from Perlito/Python/Prelude.pm, because it
# contains "use v6" and generators process it as Perl version 6.0 instead
# of a Perl module
%global __requires_exclude_from %{?__requires_exclude_from:__requires_exclude_from|}^$
%global __requires_exclude_from %__requires_exclude_from|^%{perl_vendorlib}/Perlito6/Python/Prelude.pm

%description
The v6 module is a front-end to the "Perlito" compiler.

%prep
%setup -q -n v6-%{version}
%fix_shbang_line scripts/perlito6
find -type f -exec chmod -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{_bindir}/*
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-12
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-9
- Perl 5.30 rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-6
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.047-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.047-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 29 2016 Petr Pisar <ppisar@redhat.com> - 0.047-1
- 0.047 bump

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.046-3
- Perl 5.24 rebuild

* Tue May 10 2016 Petr Pisar <ppisar@redhat.com> - 0.046-2
- Provide file name based RPM symbols

* Mon May 09 2016 Petr Pisar <ppisar@redhat.com> - 0.046-1
- 0.046 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.045-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 16 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-11
- Filter requirements from file Perlito/Python/Prelude.pm

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.045-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-9
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.045-8
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.045-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.045-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0.045-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.045-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.045-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Petr Pisar <ppisar@redhat.com> - 0.045-2
- Perl 5.16 rebuild

* Wed May 09 2012 Petr Pisar <ppisar@redhat.com> - 0.045-1
- 0.045 bump

* Tue Apr 17 2012 Petr Pisar <ppisar@redhat.com> 0.044-1
- Specfile autogenerated by cpanspec 1.78.
