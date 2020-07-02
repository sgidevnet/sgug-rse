Name:           perl-Dist-Milla
Version:        1.0.20
Release:        8%{?dist}
Summary:        CPAN distribution builder
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Dist-Milla
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Dist-Milla-v%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# Dist::Zilla::App version from Dist::Zilla in META
# Dist::Zilla::App 6 not used at tests
# Dist::Zilla::Plugin::InlineFiles not used at tests
# Dist::Zilla::Plugin::StaticInstall not used at tests
# Dist::Zilla::Role::AfterMint not used at tests
# Dist::Zilla::Role::MetaProvider not used at tests
# Dist::Zilla::Role::MintingProfile::ShareDir not used at tests
# Dist::Zilla::Role::PluginBundle::Config::Slicer not used at tests
# Dist::Zilla::Role::PluginBundle::Easy not used at tests
# Dist::Zilla::Role::PluginBundle::PluginRemover not used at tests
# Dist::Zilla::Role::TextTemplate not used at tests
# File::pushd not used at tests
# Git::Wrapper not used at tests
# Moose not used at tests
# namespace::autoclean not used at tests
# parent not used at tests
# version not used at tests
# Additional plugins defined in META, this is a plugin bundle:
# Dist::Zilla::Plugin::CheckChangesHasContent not used at tests
# Dist::Zilla::Plugin::ConfirmRelease not used at tests
# Dist::Zilla::Plugin::CopyFilesFromBuild 0.163040 not used at tests
# Dist::Zilla::Plugin::CopyFilesFromRelease not used at tests
# Dist::Zilla::Plugin::ExecDir not used at tests
# Dist::Zilla::Plugin::ExtraTests not used at tests
# Dist::Zilla::Plugin::Git::Contributors 0.009 not used at tests
# Dist::Zilla::Plugin::Git::GatherDir not used at tests
# Dist::Zilla::Plugin::Git::Init 2.012 not used at tests
# Dist::Zilla::Plugin::GithubMeta not used at tests
# Dist::Zilla::Plugin::License not used at tests
# Dist::Zilla::Plugin::LicenseFromModule 0.05 not used at tests
# Dist::Zilla::Plugin::Manifest not used at tests
# Dist::Zilla::Plugin::MetaJSON not used at tests
# Dist::Zilla::Plugin::MetaYAML not used at tests
# Dist::Zilla::Plugin::ModuleBuildTiny not used at tests
# Dist::Zilla::Plugin::NameFromDirectory 0.04 not used at tests
# Dist::Zilla::Plugin::NextRelease not used at tests
# Dist::Zilla::Plugin::PodSyntaxTests not used at tests
# Dist::Zilla::Plugin::Prereqs::FromCPANfile 0.06 not used at tests
# Dist::Zilla::Plugin::ReadmeAnyFromPod not used at tests
# Dist::Zilla::Plugin::ReadmeFromPod not used at tests
# Dist::Zilla::Plugin::ReversionOnRelease 0.04 not used at tests
# Dist::Zilla::Plugin::ShareDir not used at tests
# Dist::Zilla::Plugin::Test::Compile not used at tests
# Dist::Zilla::Plugin::TestRelease not used at tests
# Dist::Zilla::Plugin::UploadToCPAN not used at tests
# Dist::Zilla::Plugin::VersionFromMainModule not used at tests
# Dist::Zilla::PluginBundle::Git not used at tests
# Module::CPANfile 0.9025 not used at tests
# Tests:
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | sed 's,[^0-9^.]*,,g'))
# Dist::Zilla::App version from Dist::Zilla in META
Requires:       perl(Dist::Zilla::App) >= 6
Requires:       perl(Dist::Zilla::Plugin::InlineFiles)
Requires:       perl(Dist::Zilla::Plugin::StaticInstall)
Requires:       perl(Dist::Zilla::Role::AfterMint)
Requires:       perl(Dist::Zilla::Role::MetaProvider)
Requires:       perl(Dist::Zilla::Role::MintingProfile::ShareDir)
Requires:       perl(Dist::Zilla::Role::PluginBundle::Config::Slicer)
Requires:       perl(Dist::Zilla::Role::PluginBundle::Easy)
Requires:       perl(Dist::Zilla::Role::PluginBundle::PluginRemover)
Requires:       perl(Dist::Zilla::Role::TextTemplate)
# Additional plugins defined in META, this is a plugin bundle:
Requires:       perl(Dist::Zilla::Plugin::CheckChangesHasContent)
Requires:       perl(Dist::Zilla::Plugin::ConfirmRelease)
Requires:       perl(Dist::Zilla::Plugin::CopyFilesFromBuild) >= 0.163040
Requires:       perl(Dist::Zilla::Plugin::CopyFilesFromRelease)
Requires:       perl(Dist::Zilla::Plugin::ExecDir)
Requires:       perl(Dist::Zilla::Plugin::ExtraTests)
Requires:       perl(Dist::Zilla::Plugin::Git::Contributors) >= 0.009
Requires:       perl(Dist::Zilla::Plugin::Git::GatherDir)
Requires:       perl(Dist::Zilla::Plugin::Git::Init) >= 2.012
Requires:       perl(Dist::Zilla::Plugin::GithubMeta)
Requires:       perl(Dist::Zilla::Plugin::License)
Requires:       perl(Dist::Zilla::Plugin::LicenseFromModule) >= 0.05
Requires:       perl(Dist::Zilla::Plugin::Manifest)
Requires:       perl(Dist::Zilla::Plugin::MetaJSON)
Requires:       perl(Dist::Zilla::Plugin::MetaYAML)
Requires:       perl(Dist::Zilla::Plugin::ModuleBuildTiny)
Requires:       perl(Dist::Zilla::Plugin::NameFromDirectory) >= 0.04
Requires:       perl(Dist::Zilla::Plugin::NextRelease)
Requires:       perl(Dist::Zilla::Plugin::PodSyntaxTests)
Requires:       perl(Dist::Zilla::Plugin::Prereqs::FromCPANfile) >= 0.06
Requires:       perl(Dist::Zilla::Plugin::ReadmeAnyFromPod)
Requires:       perl(Dist::Zilla::Plugin::ReadmeFromPod)
Requires:       perl(Dist::Zilla::Plugin::ReversionOnRelease) >= 0.04
Requires:       perl(Dist::Zilla::Plugin::ShareDir)
Requires:       perl(Dist::Zilla::Plugin::Test::Compile)
Requires:       perl(Dist::Zilla::Plugin::TestRelease)
Requires:       perl(Dist::Zilla::Plugin::UploadToCPAN)
Requires:       perl(Dist::Zilla::Plugin::VersionFromMainModule)
Requires:       perl(Dist::Zilla::PluginBundle::Git)
Requires:       perl(Module::CPANfile) >= 0.9025

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Dist::Zilla::App\\)$

%description
Milla is a Dist::Zilla profile. It is a collection of Dist::Zilla plugin
bundle, Dist::Zilla minting profile and a command line wrapper. It is designed
around the "Convention over Configuration" philosophy, and by default doesn't
rewrite module files nor requires you to change your work flow at all.

%prep
%setup -q -n Dist-Milla-v%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
# Remove an unintentional manual,
# <https://github.com/miyagawa/Dist-Milla/issues/45>
rm $RPM_BUILD_ROOT/%{_mandir}/man3/auto::share::module::Dist-Zilla-MintingProfile-Milla::default::Module.pm.template.3pm

%check
./Build test

%files
%license LICENSE
%doc Changes README
%{_bindir}/milla
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.20-8
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.20-5
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.20-2
- Perl 5.28 rebuild

* Tue Apr 24 2018 Petr Pisar <ppisar@redhat.com> - 1.0.20-1
- 1.0.20 bump

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Petr Pisar <ppisar@redhat.com> - 1.0.18-1
- 1.0.18 bump

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.17-2
- Perl 5.26 rebuild

* Fri Mar 10 2017 Petr Pisar <ppisar@redhat.com> 1.0.17-1
- Specfile autogenerated by cpanspec 1.78.
