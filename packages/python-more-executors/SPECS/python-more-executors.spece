%global srcname more-executors
%global srcname_py more_executors

Summary: A library of composable Python executors and futures
Name: python-%{srcname}
Version: 2.5.1
Release: 2%{?dist}
License: GPLv3+
BuildArch: noarch
URL: https://github.com/rohanpm/%{srcname}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

%{?python_enable_dependency_generator}

%description
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

# dependencies for test suite
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(pyhamcrest)
BuildRequires:	python3dist(monotonic)
BuildRequires:	python3dist(six)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library is intended for use with the concurrent.futures module.
It includes a collection of Executor implementations in order to extend
the behavior of Future objects.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{srcname}
%doc README.md
%license LICENSE

%{python3_sitelib}/%{srcname_py}*.egg-info/
%{python3_sitelib}/%{srcname_py}/

%changelog
* Fri Jun 26 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 2.5.1-2
- Explicitly BuildRequires python3-setuptools

* Mon Jun 01 2020 Rohan McGovern <rohanpm@fedoraproject.org> 2.5.1-1
- Update to 2.5.1

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.5.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.5.0-1
- Update to 2.5.0

* Sun Sep 15 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.4.0-1
- Update to 2.4.0

* Sat Sep 07 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.3.0-1
- Update to 2.3.0

* Sat Aug 31 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.2.0-1
- Update to 2.2.0

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.1.2-1
- Update to 2.1.2

* Sun Jun 16 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.1.1-1
- Update to 2.1.1

* Thu Jun 06 2019 Rohan McGovern <rohanpm@fedoraproject.org> 2.1.0-1
- Update to 2.1.0

* Fri May 03 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 2.0.2-1
- New upstream release
- Fix build with Python 3.8 (#1705459)

* Sat Apr 06 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 2.0.1-1
- New upstream release

* Fri Apr 05 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 2.0.0-2
- Run test suite during build

* Sun Mar 17 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 2.0.0-1
- New upstream release

* Sat Feb 23 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 1.20.2-1
- New upstream release

* Sun Feb 17 2019 Rohan McGovern <rohan@mcgovern.id.au> - 1.20.1-1
- Initial RPM release
