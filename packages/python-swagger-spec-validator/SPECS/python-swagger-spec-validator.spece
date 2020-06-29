%global srcname swagger-spec-validator

Name:           python-%{srcname}
Version:        2.4.3
Release:        2%{?dist}
Summary:        Validation of Swagger specifications

License:        ASL 2.0
URL:            https://github.com/Yelp/swagger_spec_validator
Source0:        %{pypi_source}
Source1:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:      %{url}/commit/69f4e8039ec9bf42dbaea953babcb2d62d409786.patch#/0001-Fix-tests.validator20.validate_spec_test.test_compli.patch

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(jsonschema)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(pytest) >= 3.1.0
BuildRequires:  python3dist(httpretty)
BuildRequires:  python3dist(mock)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -N
rm -vr *.egg-info
tar -xvf %{S:1} --strip-components=1 --wildcards \
  'swagger_spec_validator-%{version}/LICENSE.txt' \
  'swagger_spec_validator-%{version}/CHANGELOG.rst' \
  'swagger_spec_validator-%{version}/tests/' \
  %{nil}
%autopatch -p1

%build
%py3_build

%install
%py3_install

%check
%python3 -m pytest tests

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md CHANGELOG.rst
%{python3_sitelib}/swagger_spec_validator/
%{python3_sitelib}/swagger_spec_validator-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.4.3-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.4.3-1
- Initial package
