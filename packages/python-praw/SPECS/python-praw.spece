%bcond_with docs
%global pypi_name praw

Name:           python-%{pypi_name}
Version:        7.1.0
Release:        1%{?dist}
Summary:        Python module that allows for simple access to reddit's API

License:        GPLv3+
URL:            https://praw.readthedocs.org
Source0:        https://github.com/praw-dev/praw/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PRAW, an acronym for "Python Reddit API Wrapper", is a python package that
allows for simple access to reddit's API.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3-prawcore
BuildRequires:  mock
BuildRequires:  python3-mock
BuildRequires:  python3-betamax
BuildRequires:  python3-betamax-matchers
BuildRequires:  python3-betamax-serializers
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-runner
BuildRequires:  python3-websocket-client
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PRAW, an acronym for "Python Reddit API Wrapper", is a python package that
allows for simple access to reddit's API.

%if %{with docs}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for %{summary}

BuildRequires:  python3-sphinx

%description -n python-%{pypi_name}-doc
PRAW, an acronym for "Python Reddit API Wrapper", is a python package that
allows for simple access to reddit's API.
%endif

%prep
%autosetup -n %{pypi_name}-%{version}
# The RPM package should not provide this feature
sed -i -e '/"update_checker >=0.17"/d' setup.py

%build
%py3_build
%if %{with docs}
sphinx-build docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc AUTHORS.rst CHANGES.rst CODE_OF_CONDUCT.md README.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info

%if %{with docs}
%files -n python-%{pypi_name}-doc
%doc html
%endif

%changelog
* Tue Jun 23 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.1.0-1
- Update to latest upstream release 7.1.0 (rhbz#1849859)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-2
- Rebuilt for Python 3.9

* Sat May 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.0.0-1
- Update to latest upstream release 7.0.0 (rhbz#1827865)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 10 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.5.1-1
- Better use of wildcards
- Update to latest upstream release 6.5.1

* Mon Jan 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 6.5.0-1
- Update source URL
- Update to latest upstream release 6.5.0 (rhbz#1787988)

* Wed Sep 25 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.4.0-1
- Update to latest upstream release 6.4.0 (rhbz#1754213)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.3.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 23 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.3.1-2
- Add new BR

* Fri Jun 21 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.3.1-1
- Update to latest upstream release 6.3.1 (rhbz#1425652)
- Fix conflict (rhbz#1661208)
- Support for Python 3.8 (rhbz#716516)

* Tue Jun 11 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.3.0-1
- Update to latest upstream release 6.3.0 (rhbz#1425652)

* Thu May 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 6.2.0-1
- Update to latest upstream release 6.2.0 (rhbz#1425652)

* Fri Feb 22 2019 Fabian Affolter <mail@fabian-affolter.ch> - 3.6.2-2
- Update comments

* Tue Feb 12 2019 Ben Rosser <rosser.bjr@gmail.com> - 3.6.2-1
- Update to latest upstream release (rhbz#1661208, rhbz#1624628)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.6.0-7
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.6.0-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.6.0-2
- Rebuild for Python 3.6

* Wed Nov 16 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.6.0-1
- Update to latest upstream release 3.6.0

* Fri Aug 26 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 3.5.0-1
- Update to 3.5.0
- SPEC refactor

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 3.4.0-1
- Update to latest upstream release 3.4.0 (rhbz#1310641)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Nov  6 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 3.3.0-2
- Only include the scipt in the python3 package.  The one in the python2
  package wouldn't function without manual intervention because it would
  require the python3-praw package but there was no dependency to it.
  Simply dropping it from the python-praw package also fixes the python-praw
  package to not require /usr/bin/python3

* Tue Oct 06 2015 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0-1
- Update to latest upstream release 3.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.21-1
- Update to latest upstream release 2.1.21 (rhbz#1206410)

* Fri Jan 23 2015 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.20-1
- Update to latest upstream release (rhbz#1185340)

* Sun Dec 07 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.19-2
- Add requirement python-requests (rhbz#1171444)

* Wed Nov 05 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.19-1
- Update to new upstream release (rhbz#1070176)
- Update patch0

* Sun Sep 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.18-2
- Add python3 subpackage (rhbz#1135689)

* Sat Aug 23 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.18-1
- Update to latest upstream version 2.1.18

* Mon Jul 14 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.17-1
- Disable update_checker (rhbz#1103097)
- Update to latest upstream version 2.1.17

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Fabian Affolter <mail@fabian-affolter.ch> - 2.1.16-1
- Spec file update
- Update to latest upstream version 2.1.16

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 10 2012 Elad Alfassa <elad@fedoraproject.org> - 1.0.15-3
- Fix more issues from review

* Sat Nov 10 2012 Elad Alfassa <elad@fedoraproject.org> - 1.0.15-2
- Fix few minor problems from review

* Sat Nov 10 2012 Elad Alfassa <elad@fedoraproject.org> - 1.0.15-1
- Initial packaging for Feora

