%global debug 0

%if 0%{debug}
%global __strip /bin/true
%endif

%global libdnf_version 0.43.1

Name:           microdnf
Version:        3.4.0
Release:        4%{?dist}
Summary:        Minimal C implementation of DNF tweaked for IRIX

License:        GPLv3+
URL:            https://github.com/rpm-software-management/microdnf
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch100:       microdnf.sgifixes.patch

BuildRequires:  gcc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.20.0
BuildRequires:  pkgconfig(libdnf) >= %{libdnf_version}
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  help2man

BuildRequires:  libsmartcols-devel >= 2.34-5
BuildRequires:  libsolv-devel >= 0.7.14-3
BuildRequires:  glib2 >= 2.62.6-8

Requires:       libdnf%{?_isa} >= %{libdnf_version}

Requires:       glib2-fam

%description
Micro DNF is a very minimal C implementation of DNFs install, upgrade,
remove, repolist, and clean commands, designed to be used for doing simple
packaging actions in containers when you dont need full-blown DNF and
you want the tiniest useful containers possible.

That is, you dont want any interpreter stack and you want the most
minimal environment possible so you can build up to exactly what you need.

This is not a substitute for DNF for real systems, and many of DNFs
capabilities are intentionally not implemented in Micro DNF.


%prep
%autosetup -p1

# A place to generate the sgug patch
#exit 1

%build
export CPPFLAGS="-I%{_includedir}/libdicl-0.1 -D_SGI_SOURCE -D_SGI_MP_SOURCE -D_SGI_REENTRANT_FUNCTIONS"
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
%if 0%{debug}
export CFLAGS="-g -Og"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-ldicl-0.1 -Wl,-z,relro -Wl,-z,now"
%else
export LDFLAGS="-ldicl-0.1 $RPM_LD_FLAGS"
%endif
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_mandir}/man8/microdnf.8*
%{_bindir}/%{name}

%changelog
* Tue Dec 15 2020 Daniel Hams <daniel.hams@gmail.com> - 3.4.0-4
- Include dependency on glib2-fam for file/dir monitoring

* Mon Dec 14 2020 Daniel Hams <daniel.hams@gmail.com> - 3.4.0-3
- Depend on necessary smartcols, libsolv, glib2 versions

* Sun Nov 29 2020 Daniel Hams <daniel.hams@gmail.com> - 3.4.0-2
- Move over to C++ and fix some variable init placement issues

* Tue Nov 10 2020 Daniel Hams <daniel.hams@gmail.com> - 3.4.0-1
- Porting into sgugrse

* Wed Jan 15 2020 Ales Matej <amatej@redhat.com> - 3.4.0-1
- Add reinstall command
- Add "--setopt=tsflags=test" support
- Add "--setopt=reposdir=<path>" and "--setopt=varsdir=<path1>,<path2>,..." support
- Add "--config=<path_to_config_file>" support
- Add "--disableplugin", "--enableplugin" support (RhBug:1781126)
- Add "--noplugins" support
- Add "--setopt=cachedir=<path_to_cache_directory>" support
- Add "--installroot=<path_to_installroot_directory>" support
- Add "--refresh" support
- Support "install_weak_deps" conf option and "--setopt=install_weak_deps=0/1"
- Respect reposdir from conf file
- Respect "metadata_expire" conf file opton (RhBug:1771147)
- Fix: Dont print lines with (null) in transaction report (RhBug:1691353)
- [repolist] Print padding spaces only if output is terminal
