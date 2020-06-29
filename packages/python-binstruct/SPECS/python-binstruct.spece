
%global pypi_name binstruct
%global global_desc							\
The binstruct library allows you to access binary data using a		\
predefined structure.  The binary data can be provided in any form	\
that allows an indexed access to single bytes.  This could for example	\
be a memory-mapped file.  The data structure itself is defined in way	\
similar to Django database table definitions by declaring a new class	\
with its fields.


Name:		python-%{pypi_name}
Version:	1.0.1
Release:	14%{?dist}
Summary:	Library for read/write access of binary data via structures

License:	GPLv3+
URL:		https://pypi.python.org/pypi/%{pypi_name}
Source0:	https://files.pythonhosted.org/packages/source/b/%{pypi_name}/%{pypi_name}-%{version}.zip

BuildArch:	noarch

BuildRequires:	dos2unix

%description
%{global_desc}


%package -n python3-%{pypi_name}
Summary:	%{summary}

BuildRequires:	python3-devel
BuildRequires:	python3-nose
BuildRequires:	python3-pytest
BuildRequires:	python3-setuptools

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}


%prep
%autosetup -n %{pypi_name}-%{version}
%{_bindir}/find . -type f -print0 |					\
	%{_bindir}/xargs -0 --max-args=1 %{_bindir}/dos2unix -ascii -k -s


%build
%py3_build


%install
%py3_install


%check
%{_bindir}/nosetests-%{python3_version} -vv


%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc PKG-INFO README.rst
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/__pycache__/%{pypi_name}.cpython-%{python3_version_nodots}*.pyc


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-11
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-8
- Subpackage python2-binstruct has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuild for Python 3.6

* Mon Oct 24 2016 Björn Esser <fedora@besser82.io> - 1.0.1-1
- Initial import (rhbz 1387835)

* Sat Oct 22 2016 Björn Esser <fedora@besser82.io> - 1.0.1-0.1
- Initial package (rhbz 1387835)
