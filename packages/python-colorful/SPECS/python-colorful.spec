# what it's called on pypi
%global srcname colorful
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}


Name:           python-%{pkgname}
Version:        0.5.0
Release:        6%{?dist}
Summary:        Terminal string styling done right
License:        MIT
URL:            https://github.com/timofurrer/colorful
# pypi tarball missing tests and license
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# downstream only patch to permit the use of older setuptools
Patch0:         remove-setuptools-environment-marker.patch
# https://github.com/timofurrer/colorful/pull/20
Patch1:         add-skipif-for-tests-that-fail-without-a-tty.patch
BuildArch:      noarch


%description
%{summary}.


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-pytest
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname}
%{summary}.


%prep
%autosetup -n %{srcname}-%{version} -p 1


%build
%py3_build


%install
%py3_install


%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose tests


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Carl George <carl@george.computer> - 0.5.0-1
- Initial package
