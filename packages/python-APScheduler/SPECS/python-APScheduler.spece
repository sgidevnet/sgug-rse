%global srcname APScheduler
%global _description %{expand:
Advanced Python Scheduler (APScheduler) is a Python library that lets you
schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.}

Name:           python-APScheduler
Version:        3.6.3
Release:        2%{?dist}
Summary:        In-process task scheduler with Cron-like capabilities

License:        MIT
URL:            http://pythonhosted.org/APScheduler/
Source0:        %pypi_source

BuildArch:      noarch

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-tornado
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-tornado
BuildRequires:  python3-twisted
BuildRequires:  python3-redis
BuildRequires:  python3-kazoo
BuildRequires:  python3-gevent
BuildRequires:  python3-sqlalchemy
BuildRequires:  python3-pymongo
BuildRequires:  python3-pytz
BuildRequires:  python3-tzlocal
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version} -p1
# Remove that test as it require services (redis, zookeeper, ...)
# up and running. Upstream provides a docker compose to spawn
# services before running these tests.
rm tests/test_jobstores.py

%build
%py3_build

%install
%py3_install

%check
# Default timezone to UTC otherwise unit tests fail.
export TZ=UTC
%{python3} -m pytest -s tests

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/apscheduler/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Fabien Boucher <fboucher@redhat.com> - 3.6.3-1
- Inport from SF packaging and bump to 3.6.3 (#1813957)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-4
- Rebuilt for Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-2
- Subpackage python2-APScheduler has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 20 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 3.5.3-1
- Upstream 3.5.3 (RHBZ#1605579)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-9
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.5-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Paul Belanger <pabelanger@redhat.com> - 3.0.5-1
- Initial packaging (#1218410)
