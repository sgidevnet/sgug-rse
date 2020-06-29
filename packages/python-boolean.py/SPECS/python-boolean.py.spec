%global pypi_name boolean.py

Name:           python-%{pypi_name}
Version:        3.8
Release:        1%{?dist}
Summary:        Define boolean algebras, and create and parse boolean expressions

License:        BSD
URL:            https://github.com/bastikr/boolean.py
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
"boolean.py" is a small library implementing a boolean algebra. It defines\
two base elements, TRUE and FALSE, and a Symbol class that can take on one of\
these two values. Calculations are done in terms of AND, OR and NOT - other\
compositions like XOR and NAND are not implemented but can be emulated with\
AND or and NOT. Expressions are constructed from parsed strings or in Python.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist Sphinx}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
sphinx-build-%{python3_version} docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst html/
%{python3_sitelib}/boolean.py*.egg-info/
%{python3_sitelib}/boolean/

%changelog
* Fri Jun 26 2020 Charalampos Stratakis <cstratak@redhat.com> - 3.8-1
- Update to 3.8 (#1846144)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.7-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 3.7-1
- new version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.6-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 08 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 3.6-1
- New package.
