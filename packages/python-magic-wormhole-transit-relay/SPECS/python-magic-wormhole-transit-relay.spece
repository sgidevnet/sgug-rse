%global pypi_name magic-wormhole-transit-relay

%global common_description %{expand:
This package contains the Magic-Wormhole "Transit Relay", a server that
helps clients establish bulk-data transit connections even when both are
behind NAT boxes. Each side makes a TCP connection to this server and
presents a handshake. Two connections with identical handshakes are
glued together, allowing them to pretend they have a direct connection.

This server used to be included in the magic-wormhole repository, but
was split out into a separate repo to aid deployment and development.}

Name:           python-%{pypi_name}
Summary:        Transit Relay server for Magic-Wormhole
Version:        0.2.1
Release:        2%{?dist}
License:        MIT

URL:            https://github.com/warner/magic-wormhole-transit-relay
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# dependencies for running the tests
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(twisted) >= 17.5

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/twisted/plugins/*
%{python3_sitelib}/wormhole_transit_relay/
%{python3_sitelib}/magic_wormhole_transit_relay-%{version}-py?.?.egg-info


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.2.1-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.2.1-1
- Update to version 0.2.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.1.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.1.2-1
- Initial package.

