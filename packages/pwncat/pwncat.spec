%global pypi_name pwncat

Name:           %{pypi_name}
Version:        0.1.0
Release:        2%{?dist}
Summary:        TCP/UDP communication suite

License:        MIT
URL:            https://github.com/cytopia/pwncat
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-%{pypi_name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description
TCP/UDP communication suite for firewall and IDS/IPS evasion, bind and
reverse shell, self-injecting shell and port forwarding magic. pwncat is
fully scriptable with Python (PSE).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
TCP/UDP communication suite for firewall and IDS/IPS evasion, bind and
reverse shell, self-injecting shell and port forwarding magic. pwncat is
fully scriptable with Python (PSE).

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
install -Dp -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc docs/
%{_mandir}/man1/%{name}.*
%{_bindir}/pwncat

%files -n python3-%{pypi_name}
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Aug 21 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-2
- Fix review issues (rhbz#1856904)

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.0-1
- Initial package for Fedora
