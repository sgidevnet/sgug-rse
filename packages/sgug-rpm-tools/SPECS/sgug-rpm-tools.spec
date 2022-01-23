%global debug 0

%if 0%{debug}
%global __strip /bin/true
%else
# This package is able to use optimised linker flags.
%global build_ldflags %{sgug_optimised_ldflags}
%endif

Summary: SGUG RPM Tools
Name: sgug-rpm-tools
Version: 0.2.3
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/sgidevnet/sgug-rpm-tools
Source: https://github.com/sgidevnet/sgug-rpm-tools/releases/download/v%{version}/sgug-rpm-tools-%{version}.tar.gz
Patch100: sgug-rpm-tools.sgifixes.patch

BuildRequires: g++
BuildRequires: automake, autoconf, libtool, pkgconfig
BuildRequires: rpm-build, rpm-devel

%description
Some utility programs to help with release / dependency management.

%prep
%autosetup -p1

%build
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-Wl,-z,relro -Wl,-z,now"
%endif
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
* Sat Jan 22 2022 Eric Dodd <eric.e.dodd@gmail.com> - 0.2.3
- Added rpmbuild dir parameter for worldrebuilder.sh for safety

* Thu Dec 17 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.2
- Upgrade to 0.2.2 with info and desktop-file-utils in minimal

* Tue Dec 15 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.1
- Upgrade to 0.2.1 with libiconv, openssh clients too

* Tue Dec 15 2020 Daniel Hams <daniel.hams@gmail.com> - 0.2.0
- Upgrade to 0.2.0 with sgugrse repo packages in ball

* Sat Dec 12 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.9
- Upgrade to 0.1.9 with sgugshell in minimal ball

* Wed Dec 09 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.8
- Upgrade to 0.1.8 which includes per-package build logs

* Sat Dec 05 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.7
- Upgrade to 0.1.7 with better diagnostics of missing deps

* Sat Dec 05 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.6
- Upgrade to 0.1.6 with microdnf/tdnf in minimal set

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
