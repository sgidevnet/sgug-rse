%global pypi_name magic-wormhole-mailbox-server

%global common_description %{expand:
This package holds the code for the main server that Magic-Wormhole
clients connect to. The server performs store-and-forward delivery for
small key-exchange and control messages. Bulk data is sent over a direct
TCP connection, or through a transit-relay.

Clients connect with WebSockets, for low-latency delivery in the happy
case where both clients are attached at the same time. Message are
stored to enable non-simultaneous clients to make forward progress. The
server uses a small SQLite database for persistence (and clients will
reconnect automatically, allowing the server to be rebooted without
losing state). An optional “usage DB” tracks historical activity for
status monitoring and operational maintenance.}

Name:           python-%{pypi_name}
Summary:        Securely transfer data between computers
Version:        0.4.1
Release:        3%{?dist}
License:        MIT

URL:            https://github.com/warner/magic-wormhole-mailbox-server
Source0:        %{pypi_source}

# remove usage of "universal newlines" mode when opening a file
# the "u" mode is deprecated and will be removed in a future python version
Patch0:         00-no-universal-newlines-mode.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)

# dependencies for building the docs
BuildRequires:  python3dist(recommonmark)
BuildRequires:  python3dist(sphinx)

# dependencies for running the tests
BuildRequires:  python3dist(autobahn) >= 0.14.1
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(service-identity)
BuildRequires:  python3dist(treq)
BuildRequires:  python3dist(twisted) >= 17.5

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%package -n     python-%{pypi_name}-doc
Summary:        Documentation for %{name}
%description -n python-%{pypi_name}-doc %{common_description}

This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%py3_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html

# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%py3_install


%check
%{__python3} setup.py test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/twisted/plugins/*
%{python3_sitelib}/wormhole_mailbox_server/
%{python3_sitelib}/magic_wormhole_mailbox_server-%{version}-py?.?.egg-info


%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.1-3
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-2
- Remove usage of universal newlines mode when opening a file.

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 0.4.1-1
- Update to version 0.4.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 12 2019 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-3
- Add missing python3-mock dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 21 2018 Fabio Valentini <decathorpe@gmail.com> - 0.3.1-1
- Initial package.

