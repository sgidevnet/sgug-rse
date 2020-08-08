Summary: SGUG RPM Tools
Name: sgug-rpm-tools
Version: 0.1.5
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/sgidevnet/sgug-rpm-tools
Source: https://github.com/sgidevnet/sgug-rpm-tools/releases/download/v%{version}/sgug-rpm-tools-%{version}.tar.gz

BuildRequires: g++
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: rpm-build, rpm-devel

%description
Some utility programs to help with release / dependency management.

%prep
%setup -q

%build
%{configure}
make %{?_smp_mflags}

%check
make check

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} INSTALL='install -p'

%files
%{_bindir}/sgug_minimal_computer
%{_bindir}/sgug_world_builder

%changelog
* Tue Jul 25 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.5
- Upgrade to 0.1.5 with sgug_world_rebuilder usability fix

* Tue Jul 14 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.4
- Tools upgrade that includes parsing specs from the sgug git repo

* Fri Apr 10 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.2
- Upgrade to include tar,bzip2,gzip,xz,unzip in the minimum ball

* Mon Mar 23 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.1
- Upgrade to include git and sgug-rpm-tools in the minimum ball

* Sun Mar 8 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0
- First build
