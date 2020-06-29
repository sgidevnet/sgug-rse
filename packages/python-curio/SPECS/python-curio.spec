# what it's called on pypi
%global srcname curio
# what it's imported as
%global libname curio
# name of egg info directory
%global eggname curio
# package name fragment
%global pkgname curio

%global _description \
Curio is a library of building blocks for performing concurrent I/O and common\
system programming tasks such as launching subprocesses, working with files,\
and farming work out to thread and process pools.  It uses Python coroutines\
and the explicit async/await syntax introduced in Python 3.5.  Its programming\
model is based on cooperative multitasking and existing programming\
abstractions such as threads, sockets, files, subprocesses, locks, and queues.\
You'll find it to be small, fast, and fun.  Curio has no third-party\
dependencies and does not use the standard asyncio module.  Most users will\
probably find it to be a bit too-low level--it's probably best to think of it\
as a library for building libraries.  Although you might not use it directly,\
many of its ideas have influenced other libraries with similar functionality.

%bcond_without tests


Name:           python-%{pkgname}
Version:        1.1
Release:        2%{?dist}
Summary:        Building blocks for performing concurrent I/O
License:        BSD
URL:            https://github.com/dabeaz/curio
Source0:        %pypi_source
# https://github.com/dabeaz/curio/issues/320
Patch0:         add-custom-marker-for-tests-that-require-internet.patch
BuildArch:      noarch


%description %{_description}


%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
%endif
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -rf %{eggname}.egg-info


%build
%py3_build


%install
%py3_install


%if %{with tests}
%check
PYTHONPATH=%{buildroot}%{python3_sitelib} py.test-%{python3_version} --verbose -m 'not internet'
%endif


%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{libname}
%{python3_sitelib}/%{eggname}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1-2
- Rebuilt for Python 3.9

* Wed Mar 18 2020 Carl George <carl@george.computer> - 1.1-1
- Latest upstream
- Add patch0 to skip tests that require internet

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep 12 2018 Carl George <carl@george.computer> - 0.9-1
- Initial package
