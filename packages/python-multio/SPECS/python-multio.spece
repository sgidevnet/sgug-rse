# what it's called on pypi
%global srcname multio
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global _description \
multio is a convenience wrapper for curio and trio, that unifies their apis\
such that they can be used willy-nilly.

%if 0%{?fedora} >= 30
# https://github.com/theelous3/multio/issues/22
# tests fail with pytest 3.7.0+
%bcond_with tests
%else
%bcond_without tests
%endif


Name:           python-%{pkgname}
Version:        0.2.4
Release:        7%{?dist}
Summary:        Unified async library for curio and trio
License:        MIT
URL:            https://github.com/theelous3/multio
# PyPI tarball doesn't have tests
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-curio >= 0.7.0
BuildRequires:  python%{python3_pkgversion}-trio >= 0.2.0
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version}


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
%{__python3} -m pytest --color yes --verbose multio/tests
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENCE.txt
%doc README.md
%{python3_sitelib}/%{libname}
%exclude %{python3_sitelib}/%{libname}/tests
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 17 2018 Carl George <carl@george.computer> - 0.2.4-1
- Initial package
