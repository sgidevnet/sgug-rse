%global srcname django-rq

Name:           python-%{srcname}
Version:        2.2.0
Release:        2%{?dist}
Summary:        App that provides django integration for RQ (Redis Queue)

License:        MIT
URL:            https://github.com/rq/django-rq
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Django integration with RQ, a Redis based Python queuing library.
Django-RQ is a simple app that allows you to configure your queues
in django's settings.py and easily use them in your project.}

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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/django_rq-*.egg-info/
%{python3_sitelib}/django_rq/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.2.0-2
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Initial package
