%global pypi_name molten

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        1%{?dist}
Summary:        A minimal, extensible, fast and productive API framework

License:        LGPLv3+
URL:            https://github.com/Bogdanp/molten
Source0:        %{url}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) < 4.0
BuildRequires:  python3dist(typing-extensions) >= 3.6
BuildRequires:  python3dist(typing-inspect) >= 0.3.1
BuildRequires:  python3dist(gunicorn) > 19.8
BuildRequires:  python3dist(jinja2) >= 2.10
BuildRequires:  python3dist(jinja2) < 3.0
BuildRequires:  python3dist(toml) > 0.9
BuildRequires:  python3dist(msgpack) > 0.5
BuildRequires:  python3dist(sqlalchemy) > 1.2
BuildRequires:  python3dist(sqlalchemy) < 2.0

%global _description %{expand:
Minimal, extensible, fast and productive API framework for Python 3.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i 's/\"typing-inspect>=0.3.1,<.*/"typing-inspect>=0.3.1"/' setup.py

%build
%py3_build

%install
%py3_install

%check
# ignoring some tests that require modules that aren't available in Fedora
# ignoring OpenAPI tests because of https://github.com/Bogdanp/molten/issues/38
# stop ignoring when the issue will be resolved
%{__python3} -m pytest --ignore=tests/contrib/test_{cors,dramatiq,websockets,prometheus}.py  --ignore=tests/openapi

%files -n python3-%{pypi_name}
%doc README.md
# COPYING file with GPL license is not included since no source files are licenced under GPL
%license COPYING.LESSER
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%changelog
* Mon Jun 22 2020 Anna Khaitovich <akhaitov@redhat.com> - 1.0.1-1
- Update to 1.0.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 04 2019 Anna Khaitovich <akhaitov@redhat.com> - 0.7.4-1
- Initial package.
