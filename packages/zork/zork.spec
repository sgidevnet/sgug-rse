Name:           zork
Version:        1.0.2
Release:        3%{?dist}
Summary:        Public Domain original DUNGEON game (Zork I)

License:        Public Domain
URL:            https://github.com/devshane/zork
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:         zork-tweak-makefile.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel


%description
Public Domain source code to the original DUNGEON game (Zork I). Released to
the PD by Infocom. Includes source files, headers, and information.

This version of Dungeon was modified from FORTRAN to C. The original was
written in DEC FORTRAN, translated from MDL. It was then translated to f77 for
UN*X systems, from which it was translated to C. The C translation was done
with the help of f2c, the FORTRAN to C translator written by David Gay (AT&T
Bell Labs), Stu Feldman (Bellcore), Mark Maimone (Carnegie-Mellon University),
and Norm Schryer (AT&T Bell Labs).


%prep
%global _hardened_build 1
%autosetup

%build
%make_build \
    CFLAGS="%{optflags}" \
    DATADIR="%{_datadir}/%{name}" \
    LDFLAGS="%{__global_ldflags}"

%install
%make_install \
    BINDIR="%{buildroot}%{_bindir}" \
    DATADIR="%{buildroot}%{_datadir}/%{name}/" \
    LIBDIR="%{buildroot}%{_datadir}" \
    MANDIR="%{buildroot}%{_mandir}"
echo ".so dungeon.6" > %{buildroot}%{_mandir}/man6/zork.6


%files
%doc history
%doc README.md
%license readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/dtextc.dat
%{_mandir}/man6/dungeon.6.gz
%{_mandir}/man6/zork.6*


%changelog
* Tue Mar 03 2020 Justin W. Flory <jflory7@fedoraproject.org> - 1.0.2-3
- Add manpage alias for zork, to match binary executable
- Add upstream 'history' file as a doc

* Tue Apr 30 2019 Justin W. Flory <jflory7@fedoraproject.org> - 1.0.2-2
- Use Fedora CFLAGS during compilation

* Mon Apr 29 2019 Justin W. Flory <jflory7@fedoraproject.org> - 1.0.2-1
- First zork package
