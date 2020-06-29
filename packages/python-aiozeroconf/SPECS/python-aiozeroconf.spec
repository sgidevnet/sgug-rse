%global pypi_name aiozeroconf

Name:           python-%{pypi_name}
Version:        0.1.8
Release:        7%{?dist}
Summary:        An asyncio/pure Python implementation of mDNS service discovery

License:        LGPLv2+
URL:            https://github.com/frawau/aiozeroconf
Source0:        https://github.com/frawau/aiozeroconf/archive/%{version}.tar.gz#/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A pure Python Multicast DNS Service Discovery Library.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-Cython
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A pure Python Multicast DNS Service Discovery Library.

%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/^#!\//, 1d' {aiozeroconf/*.py,examples/*.py}
chmod -x examples/*.py

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst examples/
%license COPYING
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-7
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.8-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.8-2
- Add license and docs (rhbz#1713906)

* Sun May 12 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.8-1
- Initial package for Fedora
