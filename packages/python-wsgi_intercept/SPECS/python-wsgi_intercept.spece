%global pypi_name wsgi_intercept


Name:           python-%{pypi_name}
Version:        1.9.2
Release:        2%{?dist}
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing

License:        MIT
URL:            https://github.com/cdent/wsgi-intercept
Source0:        https://pypi.python.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
It installs a WSGI application in place of a real URI for testing.
Testing a WSGI application normally involves starting a server at
a local host and port, then pointing your test code to that address.
Instead,this library lets you intercept calls to any specific host/port
combination and redirect them into a `WSGI application`_ importable by
your test program.

%package -n python-%{pypi_name}-doc
Summary:        Documentation for the wsgi-intercept module
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description -n python-%{pypi_name}-doc
Documentation for the wsgi-intercept module

%package -n python3-%{pypi_name}
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-httplib2
BuildRequires:  python3-requests

Requires:       python3-setuptools

%description -n python3-%{pypi_name}
It installs a WSGI application in place of a real URI for testing.
Testing a WSGI application normally involves starting a server at
a local host and port, then pointing your test code to that address.
Instead,this library lets you intercept calls to any specific host/port
combination and redirect them into a `WSGI application`_ importable by
your test program.

%prep
%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

# generate html docs
export PYTHONPATH="$( pwd ):$PYTHONPATH"
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# fix file encoding
sed -i 's/\r$//' html/_static/jquery.js

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc README
%license LICENSE
%{python3_sitelib}/%{pypi_name}*
%exclude %{python3_sitelib}/test

%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.9.2-2
- Rebuilt for Python 3.9

* Tue Feb 11 2020 Yatin Karel <ykarel@redhat.com> - 1.9.2-1
- Update to 1.9.2 (Resolves #1429737)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-15
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 09 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-12
- Subpackage python2-wsgi_intercept has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-9
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.2.2-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.2-7
- Escape macros in %%changelog

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.2.2-4
- Rebuild for Python 3.6

* Wed May 11 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-3
- Added missing python3 macro in %%check

* Wed May 11 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-2
- Applied python3 Alan Pevec patch

* Wed May 05 2016 Chandan Kumar <chkumar246@gmail.com> - 1.2.2-1
- Bumped to version 1.2.2

* Mon Sep 21 2015 Chandan Kumar <chkumar246@gmail.com> - 0.10.3-2
- Fixed import error
- Removed test folder

* Wed Sep 16 2015 Chandan Kumar <chkumar246@gmail.com> - 0.10.3-1
- Initial package.
