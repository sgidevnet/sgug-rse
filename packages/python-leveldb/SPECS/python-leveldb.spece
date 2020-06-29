# what it's called on pypi
%global srcname leveldb
# what it's imported as
%global libname %{srcname}
# name of egg info directory
%global eggname %{srcname}
# package name fragment
%global pkgname %{srcname}

%global _description \
Thread-safe Python bindings for LevelDB.  Features everything from the LevelDB\
API, except for arbitrary key comparison and all iteration except for\
single-step forward/backwards.

%bcond_without python3

%if %{defined rhel}
%bcond_without python2
%bcond_without python3_other
%endif

%bcond_without tests


Name:           python-%{pkgname}
Version:        0.201
Release:        3%{?dist}
Summary:        Python bindings for leveldb database library
License:        BSD
URL:            https://github.com/rjpower/py-leveldb
Source0:        %pypi_source
Patch0:         use-system-leveldb.patch
BuildRequires:  gcc-c++
BuildRequires:  leveldb-devel
BuildRequires:  snappy-devel


%description %{_description}


%if %{with python2}
%package -n python2-%{pkgname}
Summary:        %{summary}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%{?python_provide:%python_provide python2-%{pkgname}}


%description -n python2-%{pkgname} %{_description}
%endif


%if %{with python3}
%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pkgname}}


%description -n python%{python3_pkgversion}-%{pkgname} %{_description}
%endif


%if %{with python3_other}
%package -n python%{python3_other_pkgversion}-%{pkgname}
Summary:        %{summary}
BuildRequires:  python%{python3_other_pkgversion}-devel
BuildRequires:  python%{python3_other_pkgversion}-setuptools


%description -n python%{python3_other_pkgversion}-%{pkgname} %{_description}
%endif


%prep
%autosetup -n %{srcname}-%{version} -p 1
rm -r %{eggname}.egg-info
# remove bundled libraries
rm -r snappy leveldb
# rpmlint fix
chmod -x README


%build
%{?with_python2:%py2_build}
%{?with_python3:%py3_build}
%{?with_python3_other:%py3_other_build}


%install
%{?with_python2:%py2_install}
%{?with_python3:%py3_install}
%{?with_python3_other:%py3_other_install}


%if %{with tests}
%check
%{?with_python2:PYTHONPATH=%{buildroot}%{python2_sitearch} %{__python2} test/test.py}
%{?with_python3:PYTHONPATH=%{buildroot}%{python3_sitearch} %{__python3} test/test.py}
%{?with_python3_other:PYTHONPATH=%{buildroot}%{python3_other_sitearch} %{__python3_other} test/test.py}
%endif


%if %{with python2}
%files -n python2-%{pkgname}
%license LICENSE
%doc README
%{python2_sitearch}/%{libname}.so
%{python2_sitearch}/%{eggname}-%{version}-py%{python2_version}.egg-info
%endif


%if %{with python3}
%files -n python%{python3_pkgversion}-%{pkgname}
%license LICENSE
%doc README
%{python3_sitearch}/%{libname}.cpython-%{python3_version_nodots}*.so
%{python3_sitearch}/%{eggname}-%{version}-py%{python3_version}.egg-info
%endif


%if %{with python3_other}
%files -n python%{python3_other_pkgversion}-%{pkgname}
%license LICENSE
%doc README
%{python3_other_sitearch}/%{libname}.cpython-%{python3_other_version_nodots}*.so
%{python3_other_sitearch}/%{eggname}-%{version}-py%{python3_other_version}.egg-info
%endif


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.201-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 17 2019 Carl George <carl@george.computer> - 0.201-1
- Latest upstream

* Sun Sep 08 2019 Carl George <carl@george.computer> - 0.194-5
- Add patch2 to fix Python 3.8 build

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.194-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.194-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.194-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Carl George <carl@george.computer> - 0.194-1
- Initial package
