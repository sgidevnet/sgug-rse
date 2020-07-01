%global srcname logzero
%global sum Robust and effective logging for Python 2 and 3

Name:           python-%{srcname}
Version:        1.5.0
Release:        8%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel python3-setuptools

%description
Robust and effective logging for Python 2 and 3.

%package -n python3-%{srcname}
Summary:        %{sum}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Robust and effective logging for Python 3.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst AUTHORS.rst CONTRIBUTING.rst HISTORY.rst
%{python3_sitelib}/*

%changelog
* Thu Jun 25 2020 Gabriel L. Somlo <gsomlo@gmail.com> - 1.5.0-8
- added setuptools build dependency

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.5.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 10 2018 Gabriel L. Somlo <gsomlo@gmail.com> - 1.5.0-1
- update to upstream 1.5.0
- remove python2 subpackage (#1627368)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-4
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.1-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 22 2017 Gabriel L. Somlo <gsomlo@gmail.com> - 1.3.1-1
- initial RPM package
