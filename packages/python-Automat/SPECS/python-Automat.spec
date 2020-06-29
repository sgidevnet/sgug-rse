# what it's called on pypi
%global srcname Automat
# what it's imported as
%global libname automat
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
Automat is a library for concise, idiomatic Python expression of finite-state
automata (particularly deterministic finite-state transducers).}

%bcond_without  tests

Name:           python-%{pkgname}
Version:        20.2.0
Release:        3%{?dist}
Summary:        Self-service finite-state machines for the programmer on the go

License:        MIT
URL:            https://github.com/glyph/automat
Source0:        %pypi_source

BuildArch:      noarch

%description %{common_description}

%package -n     python3-%{pkgname}
Summary:        %{summary}
Provides:       python3-%{libname}
%{?python_provide:%python_provide python3-%{pkgname}}

BuildRequires:  python3-devel
BuildRequires:  python3dist(m2r)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(attrs) >= 16.1
BuildRequires:  python3dist(graphviz) > 0.5.1
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(twisted) >= 16.1.1
%endif

%description -n python3-%{pkgname} %{common_description}

%package -n python-%{pkgname}-doc
Summary:        Automat documentation
%description -n python-%{pkgname}-doc
Documentation for Automat

%prep
%autosetup  -p1 -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{eggname}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%if %{with tests}
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} --verbose automat/_test
%endif

%files -n python3-%{pkgname}
%license LICENSE
%doc README.md
%{_bindir}/automat-visualize
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pkgname}-doc
%doc html
%license LICENSE

%changelog
* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 20.2.0-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 20.2.0-2
- Bootstrap for Python 3.9

* Wed Feb 19 03:32:18 CET 2020 Robert-André Mauchin <zebob.m@gmail.com> - 20.2.0-1
- Update to 20.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Dec 14 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.8.0-1
- Update to 0.8.0 (#1763502)

* Sun Oct 13 23:16:43 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-8
- Drop Python 2 support (#1761207)

* Wed Sep 18 2019 Petr Viktorin <pviktori@redhat.com> - 0.7.0-7
- Python 2: Remove tests and test dependencies

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-6
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-5
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 21:26:47 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-3
- Add patch supporting for positional only arguments for Python 3.8

* Sat Apr 06 2019 Carl George <carl@george.computer> - 0.7.0-2
- Add provides for lowercase name
- Run tests with pytest like upstream does

* Mon Mar 11 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.7.0-1
- Release 0.7.0 (#1687495)

* Fri Mar 08 2019 Jeroen van Meeuwen <vanmeeuwen+fedora@kolabsys.com> - 0.6.0-5
 - Add bcond_without tests

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.7

* Fri Apr 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.6.0-1
- Initial package.
