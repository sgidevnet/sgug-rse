#                        TO WHOM IT MAY CONCERN
#
# 1) Care futzing with this - easy to break an installation
# 2) Get a 2nd someone to double sanity check ALL changes, please
#

Summary: SGUG specific rpm configuration files
Name: sgug-rpm-config
Version: 1
Release: 5%{?dist}
# No version specified.
License: GPL+
URL: https://github.com/sgidevnet/sgug-rse/

# Core rpm settings
Source0: sgug-etc-rpm-macros

BuildRequires: coreutils

Provides: sgug-rpm-config = %{version}-%{release}

%global rpmetcdir %{_sysconfdir}/rpm

%description
SGUG specific rpm configuration files.

%prep
# Not strictly necessary but allows working on file names instead
# of source numbers in install section
%setup -c -T
cp -p %{sources} .
mv sgug-etc-rpm-macros macros

%install
mkdir -p %{buildroot}%{rpmetcdir}
install -p -m 644 -t %{buildroot}%{rpmetcdir} macros

%files
%dir %{rpmetcdir}
%{rpmetcdir}/macros

%changelog
* Tue Jul 14 2020 Daniel Hams <daniel.hams@gmail.com> - 1-5
- Version bump for prerelease temporary dist

* Fri May 22 2020 Daniel Hams <daniel.hams@gmail.com> - 1-4
- Disable the hardcoded "bootstrap" of perl in the macros

* Sat Apr 25 2020 Daniel Hams <daniel.hams@gmail.com> - 1-3
- Switch over to zstd compression

* Thur Apr 16 2020 Daniel Hams <daniel.hams@gmail.com> - 1-2
- Fix incorrect mandir (/usr/sgug/man -> /usr/sgug/share/man)

* Sun Feb 09 2020 Daniel Hams <daniel.hams@gmail.com> - 1-1
- First try as a package
