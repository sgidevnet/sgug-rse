%global pypi_name hidapi
%global py_setup_args --with-system-hidapi
%if 0%{?python3_version_nodots} > 37
%global py3_so_suffix cpython-%{python3_version_nodots}-%{_arch}-%{_target_os}%{?_gnu}
%else
%global py3_so_suffix cpython-%{python3_version_nodots}m-%{_arch}-%{_target_os}%{?_gnu}
%endif


Name:		python-%{pypi_name}
Version:	0.7.99.post20
Release:	16%{?dist}
Summary:	Interface to the %{pypi_name} library

License:	GPLv3+ or BSD or Public Domain
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	hidapi-devel
BuildRequires:	libusb-devel
BuildRequires:	libudev-devel

%description
%{summary}.


%package -n python3-%{pypi_name}
Summary:	%{summary}

BuildRequires:	python3-Cython
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{summary}.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove pre-built and bundled crap.
%{__rm} -fr %{pypi_name} %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
export PYTHONPATH="%{buildroot}%{python3_sitearch}"
%{__python3} tests.py


%files -n python3-%{pypi_name}
%license LICENSE*.txt
%doc PKG-INFO README.rst try.py
%{python3_sitearch}/hid.%{py3_so_suffix}.so
%{python3_sitearch}/hidraw.%{py3_so_suffix}.so
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-16
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-14
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-11
- Subpackage python2-hidapi has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com>
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com>
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.99.post20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.99.post20-3
- Rebuild for Python 3.6

* Sun Nov 06 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post20-2
- Rebuilt for ppc64

* Sat Oct 29 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post20-1
- Update to new release v0.7.99.post20
- Build against system hidapi
- Run testsuite
- Remove license-files from github, included in upstream-tarball

* Sat Oct 22 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post19-1
- Initial import (rhbz 1387837)

* Fri Oct 21 2016 Björn Esser <fedora@besser82.io> - 0.7.99.post19-0.1
- Initial package (rhbz 1387837)
