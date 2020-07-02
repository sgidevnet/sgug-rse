Name:           python-raven

Version:        6.10.0
Release:        7%{?dist}
Summary:        Python client for Sentry

License:        BSD
URL:            https://pypi.python.org/pypi/raven/
Source0:        https://files.pythonhosted.org/packages/source/r/raven/raven-%{version}.tar.gz
Patch0:         raven-use-system-cacert.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#needed for check:
#BuildRequires:  python3-contextlib2
#BuildRequires:  python3-flask-login
#BuildRequires:  python3-blinker
#BuildRequires:  python3-anyjson
#BuildRequires:  python3-webtest
#BuildRequires:  python3-tornado
#BuildRequires:  python3-requests
#BuildRequires:  python3-pytest

%global _description\
Raven is a Python client for Sentry <http://getsentry.com>. It provides full\
out-of-the-box support for many of the popular frameworks, including Django,\
and Flask. Raven also includes drop-in support for any WSGI-compatible web\
application.

%description %_description

%package -n python3-raven
Summary:        Python client for Sentry
%{?python_provide:%python_provide python3-raven}

%description -n python3-raven
Raven is a Python client for Sentry <http://getsentry.com>. It provides full
out-of-the-box support for many of the popular frameworks, including Django,
and Flask. Raven also includes drop-in support for any WSGI-compatible web
application.

%prep
%setup -q -n raven-%{version}
%patch0 -p1

rm raven/data/cacert.pem
rmdir raven/data

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root=%{buildroot}

%check
#Disable check for now because of missing dependency pytest-timeout
#%%{__python3} setup.py test

%files -n python3-raven
%doc README.rst
%license LICENSE
%{_bindir}/raven
%{python3_sitelib}/*

%changelog
* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 6.10.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 6.10.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 6.10.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 23 2019 Sander Hoentjen <sander@hoentjen.eu> - 6.10.0-2
- Remove python2 subpackage
  (https://fedoraproject.org/wiki/Changes/F31_Mass_Python_2_Package_Removal)

* Mon Jul 22 2019 Sander Hoentjen <sander@hoentjen.eu> - 6.10.0-1
- New upstream release
- Change /usr/bin/raven to python 3
  (See https://fedoraproject.org/wiki/Changes/Python_means_Python3)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 6.9.0-2
- Rebuilt for Python 3.7

* Tue Jun 05 2018 Sander Hoentjen <sander@hoentjen.eu> - 6.9.0-1
- New upstream release

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 6.0.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.0.0-3
- Python 2 binary package renamed to python2-raven
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Sander Hoentjen <sander@hoentjen.eu> - 6.0.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 5.27.1-2
- Rebuild for Python 3.6

* Tue Sep 20 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.27.1-1
- New upstream release

* Mon Sep 19 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.27.0-1
- New upstream release

* Thu Sep 01 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.26.0-1
- New upstream release

* Mon Aug 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.24.2-1
- Update to 5.24.2

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.22.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Jul 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.22.0-1
- Update to 5.22.0

* Fri Jun 17 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.21.0-1
- Update to 5.21.0

* Thu Jun 16 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.20.0-1
- Update to 5.20.0

* Fri May 20 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.18.0-1
- Update to 5.18.0

* Wed Mar 30 2016 Sander Hoentjen <sander@hoentjen.eu> 5.12.0-1
- Update to 5.12.0 (#1313113)

* Sun Mar 27 2016 Sander Hoentjen <sander@hoentjen.eu> 5.11.2-1
- Update to 5.11.2 (#1313113)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.10.2-2
- add requires on python-contextlib2

* Thu Jan 28 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.10.2-1
- Update to 5.10.2 (#1298402)

* Fri Jan 22 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.10.1-1
- Update to 5.10.1 (#1298402)

* Sat Jan 16 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.10.0-1
- Update to 5.10.0 (#1298402)
- Use %%license tag for LICENSE
- Use system cacerts
- add check section but disabled for now, because of missing pytest-timeout dependency

* Fri Jan 08 2016 Sander Hoentjen <sander@hoentjen.eu> - 5.9.2-1
- Update to new upstream release 5.9.2
- Define __python2 if it's undefined (EPEL6 compatibility) <ewoud@kohlvanwijngaarden.nl>
- Correctly define python2_sitelib macro if it's undefined <ewoud@kohlvanwijngaarden.nl>

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 02 2014 Xavier Queralt <xqueralt@redhat.com> - 4.1.1-1
- Update to new upstream release 4.1.1

* Tue Jan 21 2014 Xavier Queralt <xqueralt@redhat.com> - 4.0.3-1
- Update to new upstream release 4.0.3

* Wed Oct 16 2013 Xavier Queralt <xqueralt@redhat.com> - 3.5.0-2
- Don't build python3 package in RHEL
- Define the python2_sitelib macro if it is not defined

* Tue Oct 15 2013 Xavier Queralt <xqueralt@redhat.com> - 3.5.0-1
- initial package
