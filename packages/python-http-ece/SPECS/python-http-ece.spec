%global modname http-ece

Name:               python-http-ece
Version:            1.1.0
Release:            3%{?dist}
Summary:            A simple implementation of the encrypted content-encoding

License:            MIT
URL:                https://github.com/web-push-libs/encrypted-content-encoding
Source0:            %{url}/archive/v%{version}/encrypted-content-encoding-%{version}.tar.gz
BuildArch:          noarch

%description
%{summary}.

%package -n python%{python3_pkgversion}-%{modname}
Summary:            %{summary}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}
BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-nose
BuildRequires:      python%{python3_pkgversion}-mock
BuildRequires:      python%{python3_pkgversion}-coverage
BuildRequires:      python%{python3_pkgversion}-cryptography
%{?python_enable_dependency_generator}

%description -n python%{python3_pkgversion}-%{modname}
%{summary}.

Python %{python3_version} version.

%prep
%autosetup -n encrypted-content-encoding-%{version}

%build
cd python
%py3_build

%install
cd python
%py3_install

%check
cd python
nosetests-%{python3_version} -v

%files -n python%{python3_pkgversion}-%{modname}
%doc python/README.rst python/*.md
%license LICENSE
%{python3_sitelib}/http_ece/
%{python3_sitelib}/http_ece-*.egg-info/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 23 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.1.0-1
- 1.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.5-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.0.5-2
- BR/R fixes, enable tests.

* Fri Sep 28 2018 Gwyn Ciesla <limburgher@gmail.com> - 1.0.5-1
- Initial package.
