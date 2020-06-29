%global pypi_name license-expression

Name:           python-%{pypi_name}
Version:        1.0
Release:        3%{?dist}
Summary:        Library to parse, compare, simplify and normalize license expressions
# `irc-notify.py` in the tarball is licensed under GPL, but not re-distributed
License:        ASL 2.0
URL:            https://github.com/nexB/license-expression/
Source0:        %pypi_source

BuildArch:      noarch

%global _description \
This module defines a mini language to parse, validate, simplify, normalize and\
compare license expressions using a boolean logic engine.\
\
This supports SPDX license expressions and also accepts other license naming\
conventions and license identifiers aliases to resolve and normalize licenses.\
\
Using boolean logic, license expressions can be tested for equality,\
containment, equivalence and can be normalized or simplified.

%description %{_description}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist boolean.py}

%description -n python%{python3_pkgversion}-%{pypi_name} %{_description}

Python 3 version.

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -r src/*.egg-info/
rm PKG-INFO

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} -v

%files -n python%{python3_pkgversion}-%{pypi_name}
%license apache-2.0.LICENSE NOTICE
%doc README.rst
%{python3_sitelib}/license_expression*.egg-info/
%{python3_sitelib}/license_expression/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 1.0-1
- new version

* Mon Sep 02 2019 Carmen Bianca Bakker <carmenbianca@fedoraproject.org> - 0.999-1
- New package.
