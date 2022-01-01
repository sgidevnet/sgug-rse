Summary: SGUG Environment Shell
Name: sgugshell
Version: 0.1.0
Release: 4%{?dist}
License: GPLv3+
URL: https://github.com/sgidevnet/sgug-rse
Source: sgugshell

BuildRequires: bash, coreutils

%description
A utility shell that sets a correct started environment for developing with
the SGUG RPM software environment.

%prep
%setup -c -T
cp -p %{sources} .

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 -t %{buildroot}%{_bindir} sgugshell

%files
%{_bindir}/sgugshell

%changelog
* Sat Jan 01 2022 J16bit <> - 0.1.0-4
- Clean up args to calling external programs

* Fri Jan 01 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0-2
- Unset "HOST" variable (see issue with netsurf).

* Sat Dec 12 2020 Daniel Hams <daniel.hams@gmail.com> - 0.1.0-1
- First Package
