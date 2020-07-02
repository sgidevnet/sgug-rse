%global modname github3py
%global srcname github3.py
%global altname github3

# Tests require internet connection to github.com
%bcond_with tests

Name:           python-%{modname}
Version:        1.3.0
Release:        3%{?dist}
Summary:        Python wrapper for the GitHub API

License:        BSD
URL:            https://github3py.readthedocs.org
Source0:        https://github.com/sigmavirus24/%{srcname}/archive/%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

BuildArch:      noarch

%global _description \
github3.py is a comprehensive, actively developed and extraordinarily stable\
wrapper around the GitHub API (v3).

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{srcname}}
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-pytest
BuildRequires:  python3-betamax
BuildRequires:  python3-betamax-matchers
BuildRequires:  python3-jwcrypto
BuildRequires:  python3-mock
BuildRequires:  python3-requests
BuildRequires:  python3-uritemplate
%endif

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version}%{?rctag:%{rctag}}

%build
%py3_build

%install
%py3_install

%if %{with tests}
%check
py.test-%{python3_version} -v
%endif

%files -n python3-%{modname}
%license LICENSE
%doc AUTHORS.rst README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{altname}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.3.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 François Cami <fcami@fedoraproject.org> - 1.3.0-1
- Update to 1.3.0 (rhbz#1775954, #1770701, #1770832)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.13a4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.12a4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.11a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.10a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.0-0.9a4
- Subpackage python2-github3py has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.8a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.7a4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.6a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.5a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-0.4a4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.0-0.3a4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2a4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-0.1a4
- Initial package
