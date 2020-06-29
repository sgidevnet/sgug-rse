%global pypi_name python-ipmi
%global srcname ipmi

Name:           python-%{srcname}
Version:        0.4.2
Release:        4%{?dist}
Summary:        Pure python IPMI library

License:        LGPLv2+
URL:            https://github.com/kontron/python-ipmi
Source0:        %{url}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

# Fix compatibility with Python 3.9
# Resolved upstream: https://github.com/kontron/python-ipmi/pull/73
Patch0:         fix-py39-compat.patch

%?python_enable_dependency_generator

BuildRequires: python3-devel
BuildRequires: python3dist(future)
BuildRequires: python3dist(markdown)
BuildRequires: python3dist(setuptools)
BuildRequires: python3dist(mock)
BuildRequires: python3dist(nose)

%description
Pure Python IPMI Library.

%package -n     python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure Python IPMI Library.

%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find . -type f -name "*.py" -exec sed -i '/^#![  ]*\/usr\/bin\/env.*$/ d' {} ';'

%build
%py3_build

%install
%py3_install 

%check
export PYTHONPATH=$RPM_BUILD_ROOT/%{python3_sitelib}
nosetests-%{python3_version} -v tests

%files -n python3-%{srcname}
%doc README.rst
%{_bindir}/ipmitool.py
%{python3_sitelib}/pyipmi
%{python3_sitelib}/tests
%{python3_sitelib}/*-py?.?.egg-info

%changelog
* Tue Jun 16 2020 Charalampos Stratakis <cstratak@redhat.com> - 0.4.2-4
- Fix compatibility with Python 3.9 (#1792985)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 23 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.2-1
- New upstream version

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 20 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.1-2
- Fix comment #1 BZ #1676987

* Wed Feb 13 2019 Luis Bazan <lbazan@fedoraproject.org> - 0.4.1-1
- Initial package
