# headers-only library
%global debug_package %{nil}

Name:           ell
Version:        0
Release:        0.15.20130617svn%{?dist}
Summary:        Header-only C++ library to write EBNF grammars

License:        LGPLv3+
URL:            http://code.google.com/p/ell/

# this pristine source is the result of:
# svn export -r r282 http://ell.googlecode.com/svn/trunk ell-20130617
# tar -cJvf ell-20130617.tar.xz ell-20130617
Source0:        ell-20130617.tar.xz

%description
Embedded LL library is pure-header library to write EBNF grammars as C++ code.
It eases the development of parser or similar applications, while removing the
need to write a lexer.

%package        devel
BuildArch:      noarch
Summary:        Development files for ELL

# to track the usage of this library
Provides:       %{name}-static = %{version}-%{release}

%description devel
%{name}-devel is only required for building software that uses the ELL library.
Because ELL is a header-only library, there is no matching run-time package.

%prep
%setup -q -n ell-20130617

%build

# workaround to fix FTBFS, disable tests
#check
#export CFLAGS="%{optflags}"
#make test

%install
mkdir -p %{buildroot}%{_includedir}/ell
cp -pr libELL/Include/ell/*.h %{buildroot}%{_includedir}/ell

%files devel
%doc COPYING.LESSER
%dir %{_includedir}/ell
%{_includedir}/ell/*.h

%changelog
* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-0.12.20130617svn
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 06 2016 Filipe Rosset <rosset.filipe@gmail.com> - 0-0.7.20130617svn
- Rebuilt to fix FTBFS, disabled tests, fixes RHBZ #1307446

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.20130617svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Aug 14 2013 Jonathan De Wachter <sonkun@fedoraproject.org> - 0-0.2.20130617svn
- Add dist tag to the package
- Copy explicitly headers (*.h) only
- Preserve timestamps, mode and ownership
- Add noarch tag to the -devel package
- Add an empty % build section (albeit only to silence rpmlint)
- Include directories with the %%dir macro

* Tue Aug 6 2013 Jonathan De Wachter <sonkun@fedoraproject.org> - 0-0.1.20130617svn
- Initial RPM release
