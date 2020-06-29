# what it's called on pypi
%global srcname asgiref
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global common_description %{expand:
ASGI is a standard for Python asynchronous web apps and servers to communicate
with each other, and positioned as an asynchronous successor to WSGI.  This
package includes ASGI base libraries, such as:

* Sync-to-async and async-to-sync function wrappers, asgiref.sync
* Server base classes, asgiref.server
* A WSGI-to-ASGI adapter, in asgiref.wsgi}

%bcond_without  tests


Name:           python-%{pkgname}
Version:        3.2.10
Release:        1%{?dist}
Summary:        ASGI specs, helper code, and adapters
# This is BSD + bundled async-timeout ASL 2.0
License:        BSD and ASL 2.0
URL:            https://github.com/django/asgiref
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{common_description}


%package -n python3-%{pkgname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist setuptools}
%if %{with tests}
BuildRequires:  %{py3_dist pytest pytest-asyncio}
%endif
# https://github.com/django/asgiref/commit/9c6df6e02700092eb19adefff3552d44388f69b8
Provides:       bundled(python3dist(async-timeout)) == 3.0.1
%{?python_provide:%python_provide python3-%{pkgname}}


%description -n python3-%{pkgname} %{common_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests
%endif


%files -n python3-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Thu Jun 18 2020 Carl George <carl@george.computer> - 3.2.10-1
- Latest upstream

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 3.2.7-2
- Rebuilt for Python 3.9

* Thu Apr 09 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.7-1
- Update to 3.2.7

* Sat Mar 21 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 3.2.5-1
- Update to 3.2.5 (rhbz #1764824)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Miro Hrončok <mhroncok@redhat.com> - 3.2.2-1
- Update to 3.2.2 (#1691128)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.3.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Carl George <carl@george.computer> - 2.3.2-1
- Initial package
