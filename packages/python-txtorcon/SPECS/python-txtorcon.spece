%{?python_enable_dependency_generator}

%global pypi_name txtorcon

%global common_description %{expand:
txtorcon is an implementation of the control-spec for Tor using the
Twisted networking library for Python.

This is useful for writing utilities to control or make use of Tor in
event-based Python programs. If your Twisted program supports endpoints
(like twistd does) your server or client can make use of Tor
immediately, with no code changes. Start your own Tor or connect to one
and get live stream, circuit, relay updates; read and change config;
monitor events; build circuits; create onion services; etcetera.}

Name:           python-%{pypi_name}
Summary:        Twisted-based Tor controller client
Version:        20.0.0
Release:        2%{?dist}

# code: MIT; alabaster sphinx theme: BSD
License:        MIT and BSD

URL:            https://github.com/meejah/txtorcon
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  python3dist(setuptools) >= 36.2
BuildRequires:  python3dist(twisted) >= 15.5

# dependencies for building the docs
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(repoze.sphinx.autointerface) >= 0.4
BuildRequires:  python3dist(sphinx)

# dependencies for running the tests
BuildRequires:  lsof
BuildRequires:  python3dist(geoip)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(service-identity)

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%package -n     python-%{pypi_name}-doc
Summary:        txtorcon documentation
%description -n python-%{pypi_name}-doc %{common_description}

This package contains the documentation.


%prep
%autosetup -n %{pypi_name}-%{version} -p1

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

# remove duplicate documentation and examples installed by setup.py
rm -r %{buildroot}/%{_datadir}/txtorcon/


%check
PYTHONPATH=. trial-3 --reporter=text test


%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst

%{python3_sitelib}/twisted/plugins/*
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/


%files -n python-%{pypi_name}-doc
%license LICENSE
%doc html


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 20.0.0-2
- Rebuilt for Python 3.9

* Sun Apr 05 2020 Fabio Valentini <decathorpe@gmail.com> - 20.0.0-1
- Update to version 20.0.0.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 19.1.0-1
- Update to version 19.1.0.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 19.0.0-6
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fabio Valentini <decathorpe@gmail.com> - 19.0.0-5
- Include upstream patch fixing compatibility with twisted 19.2.1.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 19.0.0-2
- Enable python dependency generator

* Sun Jan 20 2019 Fabio Valentini <decathorpe@gmail.com> - 19.0.0-1
- Update to version 19.0.0.

* Thu Nov 22 2018 Fabio Valentini <decathorpe@gmail.com> - 18.3.0-1
- Initial package.

