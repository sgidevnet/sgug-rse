%global pypi_name django-configurations

Name:           python-%{pypi_name}
Version:        2.2
Release:        4%{?dist}
Summary:        A helper for organizing Django settings

License:        BSD
URL:            https://django-configurations.readthedocs.io/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
django-configurations eases Django project configuration by relying on the
composability of Python classes. It extends the notion of Django's module
based settings loading with well established object oriented programming
patterns.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-django-database-url
BuildRequires:  python3-django-email-url
BuildRequires:  python3-django-search-url
BuildRequires:  python3-django-cache-url
BuildRequires:  python3-django
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-six

%description -n python3-%{pypi_name}
django-configurations eases Django project configuration by relying on the
composability of Python classes. It extends the notion of Django's module
based settings loading with well established object oriented programming
patterns.

%package -n python-%{pypi_name}-doc
Summary:        The documentation for %{name}

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
Documentation for %{name}.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

# Tests are failing
# https://github.com/jazzband/django-configurations/issues/249
#%check
#export DJANGO_CONFIGURATION="Test"
#export DJANGO_SETTINGS_MODULE="tests.settings.main"
#PYTHONPATH=%{buildroot}%{python3_sitelib} %{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/django-cadmin
%{python3_sitelib}/configurations
%{python3_sitelib}/django_configurations-%{version}-py*.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-2
- Use var for source URL
- Better use of wildcards (rhbz#1786875)

* Sat Dec 28 2019 Fabian Affolter <mail@fabian-affolter.ch> - 2.2-1
- Initial package for Fedora 
