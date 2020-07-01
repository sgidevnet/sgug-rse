%global pypi_name CoAPthon3

Name:           python-coapthon3
Version:        1.0.1
Release:        7%{?dist}
Summary:        Python library for the CoAP protocol

License:        MIT
URL:            https://github.com/Tanganelli/CoAPthon3
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A Python library to the CoAP protocol.

%package -n python3-coapthon3
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-cachetools
%{?python_provide:%python_provide python3-coapthon3}

%description -n python3-coapthon3
A Python library for the CoAP protocol.

%package -n coapthon3
Summary:        Command-line tools for %{name}
Requires:       python3-coapthon3

%description -n coapthon3
Command-line tools for %{pypi_name}.

%prep
%autosetup -n %{pypi_name}-%{version}
# https://github.com/Tanganelli/CoAPthon3/pull/23
sed -i -e '1d;2i#!/usr/bin/python3' exampleresources.py

%build
%py3_build

%install
%py3_install

%files -n python3-coapthon3
# Doc files are missing in the releases on PyPI
# https://github.com/Tanganelli/CoAPthon3/issues/22
%{python3_sitelib}/coapthon/
%{python3_sitelib}/%{pypi_name}*.egg-info

%files -n coapthon3
%{_bindir}/*.py

%changelog
* Tue Jun 02 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-7
- Add runtime requirement (rhbz#1826566)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-6
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-3
- Rebuilt for Python 3.8

* Mon Aug 19 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-2
- Update name
- Add shebang (rhbz#1733059)

* Wed Jul 24 2019 Fabian Affolter <mail@fabian-affolter.ch> - 1.0.1-1
- Initial package for Fedora
