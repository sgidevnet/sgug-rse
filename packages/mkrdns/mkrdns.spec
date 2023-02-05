%global commit 6b3f3a40e2d5607e04edb6d1954c068c3b1a693f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global debug_package %{nil}

Name:          mkrdns
Version:       3.3
Release:       1.20190902git%{shortcommit}%{?dist}
Summary:       Automatic reverse DNS zone generator

License:       GPLv2+
URL:           https://github.com/oasys/%{name}
Source0:       https://github.com/oasys/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:     noarch
BuildRequires: perl-podlators
Requires:      perl-Getopt-Long

%description
mkrdns automates the tedious procedure of editing both forward and reverse 
zones when making changes to your zones with likely no changes to your current 
configuration file.

mkrdns does this by reading through all of the primary/secondary (master/slave) 
zones in your configuration file (either named.boot or named.conf). It will 
then automatically generate the reverse zone entries (IN PTR) for the networks 
for which you are the primary/master. It is now possible to simply edit the 
forward map, run mkrdns, and reload the zone. Clean, simple, and best of all, 
automatic.

mkrdns also acts as a limited lint-like program, issuing warnings and errors if 
there are problems with your configuration or zone files.

%prep
%autosetup -n %{name}-%{commit}

%build
# Nothing to build

%install
install -Dp -m 0755 mkrdns %{buildroot}%{_bindir}/mkrdns
mkdir -p %{buildroot}%{_mandir}/man1
pod2man mkrdns %{buildroot}%{_mandir}/man1/mkrdns.1

%files
%doc README.md
%{_bindir}/mkrdns
%{_mandir}/man1/mkrdns.1.gz

%changelog
* Mon Sep 2 2019 Christian Schuermann <spike@fedoraproject.org> 3.3-1.20190902git6b3f3a4
- Initial package

