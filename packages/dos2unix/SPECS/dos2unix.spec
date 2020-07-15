Summary: Text file format converters
Name: dos2unix
Version: 7.4.0
Release: 10%{?dist}
License: BSD
URL: http://waterlan.home.xs4all.nl/dos2unix.html
Source: http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz

Patch100: dos2unix.sgifixes.patch

BuildRequires: gcc
BuildRequires: gettext
# perl modules, required for tests
BuildRequires: perl-Test-Harness perl-Test-Simple
Provides: unix2dos = %{version}-%{release}
Obsoletes: unix2dos < 5.1-1

%description
Convert text files with DOS or Mac line endings to Unix line endings and 
vice versa.

%prep
%setup -q

%patch100 -p1

# For patch generation
#exit 1

%build
export CC=mips-sgi-irix6.5-gcc
export CXX=mips-sgi-irix6.5-g++
make %{?_smp_mflags} LDFLAGS="%{build_ldflags} -lintl -lgen"

%install
make DESTDIR=$RPM_BUILD_ROOT install

# We add doc files manually to %%doc
rm -rf $RPM_BUILD_ROOT%{_docdir}

%find_lang %{name} --with-man --all-name

%check
make test

%files -f %{name}.lang
%doc man/man1/dos2unix.htm  ChangeLog.txt COPYING.txt
%doc NEWS.txt README.txt TODO.txt
%{_bindir}/dos2unix
%{_bindir}/mac2unix
%{_bindir}/unix2dos
%{_bindir}/unix2mac
%{_mandir}/man1/*.1*

%changelog
* Mon Jun 01 2020 Daniel Hams <daniel.hams@gmail.com> - 7.4.0-10
- Fix version + include docs + which compiler hints

* Sun May 24 2020  Alexander Tafarte <notes2@gmx.de> -7.4.0-9 
- compiles on Irix 6.5 with sgug-rse gcc 9.2.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 06 2019 Than Ngo <than@redhat.com> - 7.4.0-7
- Enable tests

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild
