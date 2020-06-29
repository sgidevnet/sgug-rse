%global pypi_name npyscreen

Name:           python-%{pypi_name}
Version:        4.10.5
Release:        4%{?dist}
Summary:        Writing user interfaces without all that ugly mucking about in hyperspace

License:        BSD
URL:            http://www.npcole.com/npyscreen/
Source0:        %{pypi_source}
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This library provides a framework for developing console applications using
Python and curses. This framework should be powerful enough to create everything
from quick, simple programs to complex, multi-screen applications.


%prep
%autosetup -n %{pypi_name}-%{version}
for i in $(find . -name '*.py')
do
        sed -i -e"s/#\!\/usr\/bin\/python//" $i
        sed -i -e"s/#\!\/usr\/bin\/env python//" $i
        sed -i -e"s/#\!\/usr\/bin\/env pyton//" $i
done

%build
%py3_build

%install
%py3_install
mv LICENCE LICENSE

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.10.5-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Neil Horman <nhorman@redhat.com> - 4.10.5-2
- Updated to use %pypi_source
- Updated to include license file
- Fixed spelling typo in License file
- Shortened descriptions
- Fixed egg-info glob

* Thu Dec 12 2019 Neil Horman <nhorman@redhat.com> - 4.10.5-1
- Initial package

