%global modname boxsdk

Name:               python-boxsdk
Version:            2.9.0
Release:            1%{?dist}
Summary:            Python wrapper for the Box API


License:            ASL 2.0
URL:                https://github.com/box/box-python-sdk
Source0:            %{url}/archive/v%{version}/%{modname}-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-requests
BuildRequires:      python%{python3_pkgversion}-six
BuildRequires:      python%{python3_pkgversion}-wrapt
BuildRequires:      python%{python3_pkgversion}-requests-toolbelt
BuildRequires:      python%{python3_pkgversion}-attrs
# Tests don't pass at the moment.
# https://github.com/box/box-python-sdk/issues/494
#BuildRequires:      python%%{python3_pkgversion}-pytest
#BuildRequires:      python%%{python3_pkgversion}-bottle
#BuildRequires:      python%%{python3_pkgversion}-redis
#BuildRequires:      python%%{python3_pkgversion}-mock
#BuildRequires:      python%%{python3_pkgversion}-sqlalchemy
#BuildRequires:      python%%{python3_pkgversion}-jsonpatch
#BuildRequires:      python%%{python3_pkgversion}-cryptography
#BuildRequires:      python%%{python3_pkgversion}-pytz
#BuildRequires:      python%%{python3_pkgversion}-jwt

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n box-python-sdk-%{version}

%build
%py3_build

%install
%py3_install

#%%check
#pytest-3

%files -n python%{python3_pkgversion}-%{modname}
%doc *.rst
%license LICENSE
%{python3_sitelib}/boxsdk/
%{python3_sitelib}/%{modname}-*.egg-info/

%changelog
* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.9.0-1
- 2.9.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.8.0-2
- Rebuilt for Python 3.9

* Fri Apr 24 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.8.0-1
- 2.8.0

* Thu Mar 26 2020 Gwyn Ciesla <gwync@protonmail.com> - 2.7.1-1
- Initial build
