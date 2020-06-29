%global srcname minidb

Name:           python-%{srcname}
Version:        2.0.4
Release:        2%{?dist}
Summary:        Simple python object store

License:        ISC
URL:            https://github.com/thp/minidb
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

%description
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%package -n python3-%{srcname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
minidb 2 makes it easy to store Python objects in a SQLite 3 database and
work with the data in an easy way with concise syntax.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v test

%files -n python3-%{srcname}
%doc README
%{python3_sitelib}/%{srcname}.py*
%{python3_sitelib}/%{srcname}*.egg-info
%{python3_sitelib}/__pycache__/*

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.0.4-2
- Rebuilt for Python 3.9

* Sun May 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.4-1
- Enable tests
- Update to latest upstream release 2.0.4 (rhbz#1830649)

* Fri Apr 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.3-1
- Update to latest upstream release 2.0.3 (rhbz#1816339)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0.2-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 11 2017 Fabian Affolter <mail@fabian-affolter.ch> - 2.0.2-1
- Initial version
