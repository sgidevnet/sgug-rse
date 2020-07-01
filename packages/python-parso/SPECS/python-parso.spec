# what it's called on pypi
%global srcname parso
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Parso is a Python parser that supports error recovery and round-trip parsing
for different Python versions (in multiple Python versions). Parso is also able
to list multiple syntax errors in your python file.  Parso has been
battle-tested by jedi. It was pulled out of jedi to be useful for other
projects as well.  Parso consists of a small API to parse Python and analyse
the syntax tree.}

%if (%{defined fedora} && 0%{?fedora} < 31) || (%{defined rhel} && 0%{?rhel} < 8)
%bcond_without  python2
%endif

# test suite fixtures use yield statements, only available in pytest 3
%if (%{defined fedora} && 0%{?fedora} >= 26) || (%{defined rhel} && 0%{?rhel} >= 8)
%bcond_without tests
%endif

Name:           python-%{pkgname}
Version:        0.6.2
Release:        2%{?dist}
Summary:        Parser that supports error recovery and round-trip parsing
License:        MIT and Python
URL:            https://parso.readthedocs.io
Source0:        %pypi_source
# https://github.com/davidhalter/parso/issues/103
Patch0:         python-3.8.2-error-message.patch
BuildArch:      noarch


%description %{common_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%if %{with tests}
BuildRequires:  python2-pytest >= 3.0.7
%endif
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{common_description}
%endif


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest >= 3.0.7
%endif
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%build
%{?with_python2:%py2_build}
%py3_build


%install
%{?with_python2:%py2_install}
%py3_install


%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitelib} py.test-%{python2_version} --verbose}
# https://github.com/davidhalter/parso/issues/123
# https://bugzilla.redhat.com/show_bug.cgi?id=1830965
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose -k "not test_python_exception_matches"
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/%{libname}
%{python2_sitelib}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%files -n python3-%{pkgname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.2-2
- Rebuilt for Python 3.9

* Tue Mar 17 2020 Carl George <carl@george.computer> - 0.6.2-1
- Latest upstream
- Add patch0 to fix test suite on Python 3.8.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream

* Thu Oct 17 2019 Carl George <carl@george.computer> - 0.5.1-4
- Run tests on el8

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.1-2
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Carl George <carl@george.computer> - 0.5.1-1
- Latest upstream
- Drop EPEL python34 subpackage
- Disable python2 package on F31+ and EL8+ rhbz#1733248

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Carl George <carl@george.computer> - 0.5.0-1
- Latest upstream

* Mon Apr 08 2019 Carl George <carl@george.computer> - 0.4.0-1
- Latest upstream rhbz#1668959
- Don't use common documentation directory between subpackages

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 08 2018 Carl George <carl@george.computer> - 0.3.1-1
- Latest upstream
- Use common documentation directory
- Enable python36 subpackage for EPEL

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.7

* Mon May 21 2018 Carl George <carl@george.computer> - 0.2.1-1
- Latest upstream

* Mon Apr 16 2018 Carl George <carl@george.computer> - 0.2.0-1
- Latest upstream

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 30 2017 Carl George <carl@george.computer> - 0.1.1-2
- Be more explicit with the files in site-packages

* Tue Dec 26 2017 Carl George <carl@george.computer> - 0.1.1-1
- Initial package
