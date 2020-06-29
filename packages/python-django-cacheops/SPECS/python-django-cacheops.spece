%global srcname django-cacheops

Name:           python-%{srcname}
Version:        4.1
Release:        3%{?dist}
Summary:        ORM cache with automatic granular event-driven invalidation for Django

License:        BSD
URL:            https://github.com/Suor/django-cacheops
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
A slick app that supports automatic or manual queryset caching
and automatic granular event-driven invalidation.

It uses redis as backend for ORM cache and redis or filesystem
for simple time-invalidated one.

And there is more to it:

  * decorators to cache any user function or view as a queryset or by time
  * extensions for django and jinja2 templates
  * transparent transaction support
  * dog-pile prevention mechanism
  * a couple of hacks to make django faster}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vr *.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst CHANGELOG
%{python3_sitelib}/django_cacheops-*.egg-info/
%{python3_sitelib}/cacheops/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 31 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1-1
- Initial package
