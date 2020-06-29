%global pypi_name resumable-urlretrieve

%global desc %{expand: \
Small library to fetch files over HTTP and resume their download.}

Name:           python-%{pypi_name}
Version:        0.1.6
Release:        6%{?dist}
Summary:        Small library to fetch files over HTTP and resume their download

License:        MIT
URL:            https://github.com/berdario/resumable-urlretrieve
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%?python_enable_dependency_generator

BuildRequires: python3-devel
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(requests)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(rangehttpserver)

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
%description -n python3-%{pypi_name}
%{desc}

%prep
%autosetup -n %{pypi_name}-%{version}

# Comment out to remove /usr/bin/env shebangs
# Can use something similar to correct/remove /usr/bin/python shebangs also
find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} 2>/dev/null ';'

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=. pytest-3

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/resumable
%{python3_sitelib}/resumable_urlretrieve-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.6-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 26 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.1.6-1
- Unorphaned
- New upstream version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.1.5-1
- Update to 0.1.5 (#1433337)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 19 2017 Mathieu Bridon <bochecha@daitauha.fr> - 0.1.4-1
- New upstream version, which now includes the README file (which contains the
  license text).

* Mon Dec 12 2016 Mathieu Bridon <bochecha@daitauha.fr> - 0.1.3-1
- New upstream version.

* Sat Oct 15 2016 Mathieu Bridon <bochecha@daitauha.fr> - 0.1.2-1
- New upstream version.
- Add the test requirements, and properly run the tests.

* Thu Jan 28 2016 Mathieu Bridon <bochecha@daitauha.fr> - 0.1.1-1
- Initial package for Fedora.
