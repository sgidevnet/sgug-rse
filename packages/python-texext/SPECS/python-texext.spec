%global srcname texext

Name:           python-%{srcname}
Version:        0.6.6
Release:        2%{?dist}
Summary:        Sphinx extensions for working with LaTeX math

License:        BSD
URL:            https://github.com/matthew-brett/%{srcname}
Source0:        %pypi_source

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinxtesters)
BuildRequires:  python3dist(sympy)

%description
This package contains Sphinx extensions for working with LaTeX math.

%package -n     python3-%{srcname}
Summary:        Sphinx extensions for working with LaTeX math

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This package contains Sphinx extensions for working with LaTeX math.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build
rst2html --no-datestamp README.rst README.html

%install
%py3_install

%check
pytest-%{python3_version}

%files -n python3-%{srcname}
%doc README.html
%license LICENSE
%{python3_sitelib}/%{srcname}*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.6-2
- Rebuilt for Python 3.9

* Sun Apr 12 2020 Jerry James <loganjerry@gmail.com> - 0.6.6-1
- Version 0.6.6

* Fri Mar  6 2020 Jerry James <loganjerry@gmail.com> - 0.6.5-1
- Version 0.6.5
- All patches have been upstreamed; drop them all

* Fri Jan 31 2020 Jerry James <loganjerry@gmail.com> - 0.6.1-8
- Add -still-more-sphinx2 patch to fix FTBFS in Rawhide

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov  4 2019 Jerry James <loganjerry@gmail.com> - 0.6.1-7
- Add -more-sphinx2 patch
- Ship README in html form instead of rst

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.1-5
- Rebuilt for Python 3.8

* Tue Aug 13 2019 Jerry James <loganjerry@gmail.com> - 0.6.1-4
- Add -sphinx2 patch to fix FTBFS (bz 1736543)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 22 2018 Jerry James <loganjerry@gmail.com> - 0.6.1-2
- Drop python2 subpackage (bz 1651177)
- Add -escape patch

* Mon Sep  3 2018 Jerry James <loganjerry@gmail.com> - 0.6.1-1
- Initial RPM
