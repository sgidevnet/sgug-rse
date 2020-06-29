%global srcname ntlm-auth
%global pypi_name %{srcname}
%global gh_owner jborean93
%global library_name ntlm_auth

Name:           python-%{srcname}
Version:        1.1.0
Release:        10%{?dist}
Summary:        Python 3 compatible NTLM library

License:        LGPLv3+
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        https://github.com/%{gh_owner}/%{pypi_name}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch0:         ntlm-auth-epel-setuptools.patch
BuildArch:      noarch

BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

# For tests
BuildRequires:  python3-pytest
BuildRequires:  python3-requests

%description
 This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.

%package -n     python3-%{srcname}
Obsoletes:      python3-ntlm3 < 1.0.3-1
Provides:       python3-ntlm3 = %{version}-%{release}
Summary:        Python 3 compatible NTLM library
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
 This package allows Python clients running on any operating system to provide
NTLM authentication to a supporting server.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} -m pytest --ignore=tests/functional/test_iis.py tests

%files -n python3-%{srcname}
%doc CHANGES.md README.md
%license LICENSE
%{python3_sitelib}/%{library_name}
%{python3_sitelib}/%{library_name}-%{version}-py?.?.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-10
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 11 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Subpackage python2-ntlm-auth has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 James Hogarth <james.hogarth@gmail.com> = 1.1.0-1
* Upstream update to 1.1.0
* Mon Oct 10 2016 James Hogarth <james.hogarth@gmail.com> - 1.0.2-1
- Initial package.
