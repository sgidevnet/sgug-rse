%global srcname sphinxcontrib-openapi
%global _description %{expand:
Sphinx extension to generate APIs docs from OpenAPI (fka Swagger) spec.
It depends on sphinxcontrib-httpdomain that provides an HTTP domain
for describing RESTful HTTP APIs, so we don’t need to reinvent the wheel.}

Name:           python-%{srcname}
Version:        0.6.0
Release:        2%{?dist}
Summary:        OpenAPI spec renderer for Sphinx

# There are test files under the ASL 2.0 license, but we don't ship them in the built RPM
License:        BSD
URL:            https://sphinxcontrib-openapi.readthedocs.io/
Source0:        %pypi_source

BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx
BuildRequires:  python3-pyyaml
BuildRequires:  python3-jsonschema
BuildRequires:  python3-sphinxcontrib-httpdomain
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} -m pytest tests/ --strict

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/sphinxcontrib/openapi*
%{python3_sitelib}/sphinxcontrib_openapi*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.6.0-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Fabien Boucher <fboucher@redhat.com> - 0.6.0-1
- Adapt packaging for Rawhide from Software Factory packaging.

* Wed Aug 14 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 0.4.0-1
- Initial packaging
