%global srcname django-prometheus

Name:           python-%{srcname}
Version:        2.0.0
Release:        2%{?dist}
Summary:        Django middlewares to monitor your application with Prometheus.io

License:        ASL 2.0
URL:            https://github.com/korfuri/django-prometheus
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
%{summary}.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest-runner)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-django)
BuildRequires:  python3dist(django)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(prometheus-client) >= 0.7

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%check
%python3 setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/django_prometheus-*.egg-info/
%{python3_sitelib}/django_prometheus/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.0.0-1
- Update to 2.0.0

* Sat Sep 07 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.15-1
- Initial package
