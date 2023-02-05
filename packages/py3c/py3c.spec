# A header-only library has no debuginfo
%global debug_package %{nil}

Name:           py3c
Version:        1.0
Release:        6%{?dist}
Summary:        Guide and compatibility macros for porting extensions to Python 3

# Licences differ for subpackages
License:        MIT and CC-BY-SA

URL:            http://py3c.readthedocs.io/

Source0:        https://github.com/encukou/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python2-devel
BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
py3c helps you port C extensions to Python 3.

It provides a detailed guide, and a set of macros to make porting easy
and reduce boilerplate.

%package        devel
License:        MIT
Summary:        Header files for py3c

# Do not *require* python?-devel, because some projects can drop support
# for one of the Python versions, but still use the compat macros.
Suggests:       python2-devel
Suggests:       python3-devel

# A header-only library counts as static
Provides:       %{name}-static = %{version}-%{release}
%{?_isa:Provides: %{name}-static%{?_isa} = %{version}-%{release}}

%description devel
%{name}-devel is only required for building software that uses py3c.
Because py3c is a header-only library, there is no matching run-time package.

%package        doc
BuildArch:      noarch
License:        CC-BY-SA
Summary:        Guide for porting C extensions to Python 3

Requires:       python3-sphinx_rtd_theme

%description doc
Guide for porting CPython extensions from Python 2 to Python 3, using the
py3c macros.

%prep
%setup -q

%build
make %{?_smp_mflags} py3c.pc includedir=%{_includedir}

make %{?_smp_mflags} doc SPHINXBUILD=sphinx-build-3

# unbundle fonts provided by the theme package
bundledfonts=doc/build/html/_static/fonts
themefonts=%{python3_sitelib}/sphinx_rtd_theme/static/fonts
diff -r $bundledfonts $themefonts
rm -rv $bundledfonts
ln -s $themefonts $bundledfonts

%check
export CFLAGS="%{optflags}"
make %{?_smp_mflags} test-python2
make %{?_smp_mflags} test-python3

%install
make install prefix=%{buildroot}%{_prefix} includedir=%{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_pkgdocdir}
cp -rv doc/build/html/* %{buildroot}%{_pkgdocdir}

# Strip buildroot name from the pkgconfig file
sed --in-place -e's!%{buildroot}!!' %{buildroot}%{_datadir}/pkgconfig/py3c.pc

%files devel
%license LICENSE.MIT
%doc README.rst
%{_includedir}/py3c.h
%{_includedir}/py3c/
%{_datadir}/pkgconfig/py3c.pc

%files doc
%license doc/LICENSE.CC-BY-SA-3.0
%doc %{_pkgdocdir}/

%changelog
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.7

* Mon Feb 19 2018 Petr Viktorin <pviktori@redhat.com> - 1.0-2
- Add BuildRequires: gcc

* Sun Feb 11 2018 Petr Viktorin <pviktorin@redhat.com> - 1.0-1
- Update to 1.0 (adds Py_UNREACHABLE, Py_RETURN_RICHCOMPARE, Py_UNUSED)
- Strip buildroot name from the pkgconfig file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild


* Wed Feb 01 2017 Petr Viktorin <pviktorin@redhat.com> - 0.8-1
- Update to 0.8:
- Add backports for PyMem_Raw*

* Thu May 19 2016 Petr Viktorin <pviktorin@redhat.com> - 0.7-1
- Update to 0.7:
- Fix file shim tests on big endian architectures
  (bug in the test suite only, does not affect behavior)

* Thu May 19 2016 Petr Viktorin <pviktorin@redhat.com> - 0.6-2
- Initial package
