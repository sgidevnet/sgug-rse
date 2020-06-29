%global srcname fastcache

Name:           python-%{srcname}
Version:        1.1.0
Release:        7%{?dist}
Summary:        C implementation of python3 lru_cache

License:        MIT
URL:            https://github.com/pbrady/%{srcname}
Source0:        https://github.com/pbrady/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(pycmd)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
This package contains a C implementation of the python 3 lru_cache.  It
passes all tests in the standard library for functools.lru_cache.

%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        C implementation of python3 lru_cache

%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
This package contains a C implementation of the python 3 lru_cache.  It
passes all tests in the standard library for functools.lru_cache.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build "--define=WITH_THREAD"

%install
%py3_install
chmod 0755 %{buildroot}%{python3_sitearch}/%{srcname}/*.so

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
mkdir -p empty
cd empty
%{__python3} << EOF
import fastcache
if not fastcache.test():
    raise Exception('Tests failed')
EOF
cd -

%files -n python%{python3_pkgversion}-%{srcname}
%doc CHANGELOG README.md
%license LICENSE
%{python3_sitearch}/%{srcname}/
%{python3_sitearch}/%{srcname}*.egg-info/
%exclude %{python3_sitearch}/%{srcname}/tests

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 1.1.0-1
- New upstream version
- Drop python 2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-13
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-8
- Build python3 for EPEL
- Use single build directory
- Run tests as upstream does

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-7
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 1.0.2-4
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.2-4
- Use python2/3_version macros

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Dec  1 2014 Jerry James <loganjerry@gmail.com> - 1.0.2-2
- Be more verbose in the file listing
- Run the tests verbosely

* Fri Nov 21 2014 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Initial RPM
