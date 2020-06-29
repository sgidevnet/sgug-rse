%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name retryz


Name:           python-%{pypi_name}
Version:        0.1.9
Release:        13%{?dist}
Summary:        Retry decorator with a bunch of configuration parameters

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/retryz
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Retry decorator with a bunch of configuration parameters.

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2

BuildRequires:  python2-devel

# for running tests
BuildRequires:  python2-pytest
BuildRequires:  python2-hamcrest


%description -n python2-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# for running tests
BuildRequires:  python3-pytest
BuildRequires:  python3-hamcrest

%description -n python3-%{pypi_name}
Retry decorator with a bunch of configuration parameters.

%endif

%prep
%setup -q -n %{pypi_name}-%{upstream_version}

%build
%if 0%{?with_python2}
%py2_build
%endif
%if 0%{?with_python3}
%py3_build
%endif

%check
%if 0%{?with_python2}
PYTHONPATH=. py.test-2.7
%endif
%if 0%{?with_python3}
PYTHONPATH=. py.test-3
%endif


%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/retryz*
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/retryz*
%endif

%changelog
* Tue Jun 23 2020 Eric Harney <eharney@redhat.com> - 0.1.9-13
- Add python3-setuptools BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-12
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Eric Harney <eharney@redhat.com> - 0.1.9-6
- Remove Python 2 package for Fedora

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.9-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 22 2017 Eric Harney <eharney@redhat.com> - 0.1.9-1
- Update to 0.1.9

* Wed Feb 01 2017 Eric Harney <eharney@redhat.com> - 0.1.8-1
- Initial package
