%global srcname colorlog
%global desc "colorlog.ColoredFormatter is a formatter for use with Python's logging module that outputs records using terminal colors."

Name:           python-%{srcname}
Version:        4.1.0
Release:        4%{?dist}
Summary:        Colored formatter for the Python logging module

License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?rhel} && 0%{?rhel} < 8
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%else
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
%{desc}

%if 0%{?rhel} && 0%{?rhel} < 8
%package -n python2-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
%{desc}
%else
%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
%{desc}
%endif

%prep
%autosetup -n %{name}-%{version}

%build
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_build
%else
%py3_build
%endif

%install
%if 0%{?rhel} && 0%{?rhel} < 8
%py2_install
%else
%py3_install
%endif

%if 0%{?rhel} && 0%{?rhel} < 8
%files -n python2-%{srcname}
%doc README.md
%license LICENSE
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}*.egg-info/
%exclude %{python2_sitelib}/%{srcname}/tests/
%else
%files -n python3-%{srcname}
%doc README.md
%license LICENSE
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}*.egg-info/
%exclude %{python3_sitelib}/%{srcname}/tests/
%endif

%changelog
* Fri Jun 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-4
- Add python3-setuptools as BR

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 05 2019 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Update to latest upstream release 4.1.0 (rhbz#1753875)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 4.0.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 10 2019 Marek Goldmann <mgoldman@redhat.com> - 4.0.1-3
- Add support for EPEL 7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 17 2018 Fabian Affolter <mail@fabian-affolter.ch> - 4.0.1-1
- Update to latest upstream release 4.0.1

* Wed Oct 10 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-4
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.4-2
- Rebuilt for Python 3.7

* Sat May 05 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.4-1
- Update to latest upstream release 3.1.4 (rhbz#1568639)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.2-1
- Update to latest upstream release 3.1.2 (rhbz#1539019)

* Sat Jul 29 2017 Fabian Affolter <mail@fabian-affolter.ch> - 3.1.0-1
- Update to latest upstream release 3.1.0 (rhbz#1476423)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.9.0-2
- Rebuild for Python 3.6

* Tue Nov 22 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.9.0-1
- Add license file
- Update to latest upstream release 2.9.0

* Tue Nov 15 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-2
- Fix ownership

* Mon Nov 14 2016 Fabian Affolter <mail@fabian-affolter.ch> - 2.7.0-1
- Initial version
