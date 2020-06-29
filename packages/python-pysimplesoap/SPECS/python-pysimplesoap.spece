%global pypi_name PySimpleSOAP
%global rpmname pysimplesoap

Name:           python-%{rpmname}
Version:        1.16.2
Release:        8%{?dist}
Summary:        Python simple and lightweight SOAP Library

License:        LGPLv3+
URL:            https://github.com/pysimplesoap/pysimplesoap
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/pysimplesoap/pysimplesoap/master/license.txt
Patch0:         httplib2.patch 
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Python simple and lightweight SOAP library for client and
server web services interfaces, aimed to be as small and easy
as possible, supporting most common functionality. 

%package -n     python3-%{rpmname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{rpmname}
Python simple and lightweight SOAP library for client and 
server web services interfaces, aimed to be as small and easy 
as possible, supporting most common functionality. 

%prep
%autosetup -n %{pypi_name}-%{version} -p1
for lib in pysimplesoap/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

%build
%py3_build

%install
%py3_install

%files -n python3-%{rpmname}
%license license.txt
%{python3_sitelib}/pysimplesoap
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-8
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-6
- Apply https://github.com/pysimplesoap/pysimplesoap/pull/170

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.16.2-4
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-3
- Add license, fix some other errors

* Sun Aug 11 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-2
- Ensure there are no rpmlint warnings

* Sat Aug 10 2019 Huzaifa Sidhpurwala <huzaifas@redhat.com> - 1.16.2-1
- Initial package.
