Name:     scdoc
Version:  1.9.6
Release:  2%{?dist}
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup -q

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
%if 0%{?el7}
%make_install PREFIX=%{_prefix} PCDIR=%{buildroot}%{_datarootdir}/pkgconfig INSTALL="%{__install} -p"
%else
%make_install PREFIX=%{_prefix} PCDIR=%{buildroot}%{_datarootdir}/pkgconfig
%endif

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%{_datarootdir}/pkgconfig/%{name}.pc

%changelog
* Thu Aug 01 2019 Timothée Floure <fnux@fedoraproject.org> - 1.9.6-2
- Explicitly specifiy INSTALL environment variable for EL7 builds

* Wed Jul 31 2019 Timothée Floure <fnux@fedoraproject.org> - 1.9.6-1
- New upstream release

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Timothée Floure <fnux@fedoraproject.org> - 1.9.4-3
- Remove useless PCDIR variable definition in build section
- Fix erroneous dates in last two changelog entries

* Mon Mar 11 2019 Hristo Venev <hristo@venev.name> - 1.9.4-2
- Fix pkgconfig file.

* Mon Mar 11 2019 Timothée Floure <fnux@fedoraproject.org> - 1.9.4-1
- Remove some Makefile patches (applied upstream)
- New upstream release

* Tue Feb 05 2019 Timothée Floure <fnux@fedoraproject.org> - 1.8.1-1
- New upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 20 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.1-1
- New upstream release

* Wed Jan 16 2019 Timothée Floure <fnux@fedoraproject.org> - 1.6.0-1
- New upstream release

* Mon Oct 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.2-1
- New upstream release
- Fix broken source URL

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.4-1
- Update to 1.3.4

* Sat May 26 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.3-1
- Let there be package
