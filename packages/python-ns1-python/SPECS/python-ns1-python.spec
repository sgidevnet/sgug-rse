%global srcname ns1-python

Name:           python-%{srcname}
Version:        0.15.0
Release:        2%{?dist}
Summary:        Python SDK for the NS1 DNS platform

License:        MIT
URL:            https://github.com/ns1/ns1-python
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
This package provides a python SDK for accessing the NS1 DNS platform
and includes both a simple NS1 REST API wrapper as well as a higher level
interface for managing zones, records, data feeds, and more.
It supports synchronous and asynchronous transports.}

%description %{_description}

%package     -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Recommends:     python%{python3_version}dist(requests)
Suggests:       python%{python3_version}dist(twisted)

%description -n python3-%{srcname} %{_description}

Python 3 version.

%prep
%autosetup -n %{srcname}-%{version} -p1
rm -vrf *.egg-info
# Tests are not distributed on PyPI
sed -i -e '/setup_requires/d' setup.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE
%doc README.rst
%{python3_sitelib}/ns1_python-*.egg-info/
%{python3_sitelib}/ns1/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15.0-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 0.15.0-1
- Update to 0.15.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.12.0-1
- Update to 0.12.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.11.0-2
- Rebuilt for Python 3.8

* Mon Aug 05 18:52:42 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.11.0-1
- Update to 0.11.0

* Thu Aug 01 08:23:57 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-3
- Backport fix for use_client_subnet option

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 16 20:49:58 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0

* Sat Jul 13 23:02:48 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.9.19-1
- Initial package
