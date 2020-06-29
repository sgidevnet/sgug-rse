%global srcname fastpurge

Summary: A Python client for the Akamai Fast Purge API
Name: python-%{srcname}
Version: 1.0.2
Release: 8%{?dist}
URL: https://github.com/release-engineering/%{name}
Source0: %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
License: GPLv3+
BuildArch: noarch

%description
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

# Dependencies for test suite
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(edgegrid-python)
BuildRequires:	python3dist(monotonic)
BuildRequires:	python3dist(more-executors)
BuildRequires:	python3dist(mock)
BuildRequires:	python3dist(requests-mock)

# for Requires we rely on the automatic Python dep generator
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This library provides a simple asynchronous Python wrapper for the Fast
Purge API, including authentication and error recovery.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest -v

%files -n python3-%{srcname}
%doc README.md
%doc CHANGELOG.md
%license LICENSE

%{python3_sitelib}/%{srcname}*.egg-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Fri Jun 26 2020 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-8
- Explicitly BuildRequires python3-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 04 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-2
- Run test suite during build

* Sat Mar 30 2019 Rohan McGovern <rohanpm@fedoraproject.org> - 1.0.2-1
- Initial RPM release
