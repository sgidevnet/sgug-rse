%if 0%{?fedora}
%global with_python2 0
%global with_python3 1
%endif

%global pypi_name cachez

Name:           python-%{pypi_name}
Version:        0.1.2
Release:        14%{?dist}
Summary:        Cache decorator for global or instance level memoize

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/cachez
Source0:        https://pypi.io/packages/source/%(n=%{pypi_name}; echo ${n:0:1})/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Cache decorator for global or instance level memoize.

%if 0%{?with_python2}
%package -n python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-hamcrest
BuildRequires:  python2-pytest

%description -n python2-%{pypi_name}
Cache decorator for global or instance level memoize.

%endif

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-hamcrest
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description -n python3-%{pypi_name}
Cache decorator for global or instance level memoize.

%endif

%prep
%setup -n %{pypi_name}-%{version}

%build
%if 0%{?with_python2}
%py2_build
%endif

%if 0%{?with_python3}
%py3_build
%endif

%install
%if 0%{?with_python2}
%py2_install
%endif

%if 0%{?with_python3}
%py3_install
%endif

%check
%if 0%{?with_python2}
py.test-2 cachez_test.py
%endif
%if 0%{?with_python3}
py.test-3 cachez_test.py
%endif

%if 0%{?with_python2}
%files -n python2-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python2_sitelib}/*
%endif

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/*
%endif

%changelog
* Tue Jun 23 2020 Eric Harney <eharney@redhat.com> - 0.1.2-14
- Add python3-setuptools BuildRequires

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-13
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 03 2018 Eric Harney <eharney@redhat.com> - 0.1.2-7
- Remove Python 2 packages for Fedora

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.1.2-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Eric Harney <eharney@redhat.com> - 0.1.2-1
- Update to 0.1.2

* Fri Feb 10 2017 Eric Harney <eharney@redhat.com> - 0.1.1-1
- Update to 0.1.1
- Run unit tests

* Wed Feb 01 2017 Eric Harney <eharney@redhat.com> - 0.1.0-2
- Initial package
